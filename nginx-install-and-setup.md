# NginX Installation and Setup

## Instalation

```
wget http://nginx.org/keys/nginx_signing.key
apt-key add nginx_signing.key
echo "deb http://nginx.org/packages/mainline/ubuntu `lsb_release -cs` nginx" | tee /etc/apt/sources.list.d/nginx.list
apt update
apt install nginx
```

**Please ensure the nginx auto start on system reboot any turn on nginx auto start if it is not enabled.**

## Certbot Installation

### Installation by snapd

1. Certbot installation

```
apt install snapd
snap install core
snap refresh core
snap install --classic certbot
ln -s /snap/bin/certbot /usr/bin/certbot
```

2. Test the domain without wasting the certificate quote

```
certbot --nginx --test-cert
```

3. Acctually display the SSL certificat

```
certbot --nginx
```

4. Delete the certificate if needed

```
certbot delete --cert-name example.com
```

### Installation by apt

1. Alternatif install using apt

```
apt install -y certbot python3-certbot-nginx
```

2. Generate an SSL certificate:

```
certbot --nginx -d yourdomain.com -d www.yourdomain.com
```

3. Setting up auto-renew SSL:

```
certbot renew --dry-run
```

**select 2: Renew & replace the certificate (may be subject to CA rate limits) when installing certbot after test the certificate.**

## Gzip Compression on

Add gzip configuration in nginx.conf file using the following configuration :

```
gzip on;
gzip_types text/plain application/javascript application/x-javascript text/javascript text/xml text/css;
gzip_proxied no-cache no-store private expired auth;
```

## Header for Alternative Service http/3 and HSTS setup

Add header for http/3 negotiation and activate HSTS in server block in sites-available using the following configuration :

```
add_header Alt-Svc 'h3=":443"; ma=3600';
add_header Strict-Transport-Security "max-age=63072000; includeSubDomains; preload" always;
```

## Nginx Config

1. Nginx config for Nginx 1.27

```
user                                    www-data;
worker_processes                        auto;
pid                                     /run/nginx.pid;
include                                 /etc/nginx/modules-enabled/*.conf;

events {
    worker_connections                  1024;
}

http {
    ##
    # Basic Settings
    ##
    include                         /etc/nginx/mime.types;
    default_type                    application/octet-stream;
    sendfile                        on;
    tcp_nopush                      on;
    types_hash_max_size             2048;
    keepalive_timeout               65;

    ##
    # Log Setting
    ##
    # access_log                      /var/log/nginx/general/access.log;
    # error_log                       /var/log/nginx/general/error.log debug;
    # log_format escape=json
    #             '{'
    #                     '"time_local":"$time_local",'
    #                     '"remote_addr":"$remote_addr",'
    #                     '"remote_user":"$remote_user",'
    #                     '"request":"$request",'
    #                     '"status": "$status",'
    #                     '"body_bytes_sent":"$body_bytes_sent",'
    #                     '"request_time":"$request_time",'
    #                     '"http_referrer":"$http_referer",'
    #                     '"http_user_agent":"$http_user_agent"'
    #             '}';

    ##
    # GZIP Setting
    ##
    gzip                            on;
    gzip_comp_level                 5;
    gzip_buffers                    16 8k;
    gzip_types text/plain application/javascript application/x-javascript text/javascript text/xml text/css;
    gzip_proxied no-cache no-store private expired auth;

    ##
    # HTTP Version Setting
    ##
    http2                           on;
    http3                           on;
    http3_hq                        off;
    quic_retry                      off;
    quic_gso                        off;

    # SSL Setting
    # intermediate configuration
    ssl_protocols                   TLSv1 TLSv1.1 TLSv1.2 TLSv1.3;
    ssl_prefer_server_ciphers       on;
    ssl_early_data                  on;
    ssl_session_timeout             1d;
    # OCSP stapling
    ssl_stapling                    on;
    ssl_stapling_verify             on;

    # Add Alt-Svc headers to negotiate HTTP/3
    add_header Alt-Svc 'h3=":443"; ma=86400' always;
    add_header Strict-Transport-Security "max-age=63072000; includeSubDomains; preload" always;

    # Virtual Host Configs
    include                         /etc/nginx/conf.d/*.conf;
    include                         /etc/nginx/sites-enabled/*;
}
```

2. Nginx config for Nginx 1.18 (stable)

```
user                                    www-data;
worker_processes                        auto;
pid                                     /run/nginx.pid;
include                                 /etc/nginx/modules-enabled/*.conf;

events {
    worker_connections                  768;
}

http {
    ##
    # Basic Settings
    ##
    include                         /etc/nginx/mime.types;
    default_type                    application/octet-stream;
    sendfile                        on;
    tcp_nopush                      on;
    types_hash_max_size             2048;
    keepalive_timeout               65;

    ##
    # Log Setting
    ##
    # access_log                      /var/log/nginx/general/access.log;
    # error_log                       /var/log/nginx/general/error.log debug;
    # log_format escape=json
    #            '{'
    #                    '"time_local":"$time_local",'
    #                    '"remote_addr":"$remote_addr",'
    #                    '"remote_user":"$remote_user",'
    #                    '"request":"$request",'
    #                    '"status": "$status",'
    #                    '"body_bytes_sent":"$body_bytes_sent",'
    #                    '"request_time":"$request_time",'
    #                    '"http_referrer":"$http_referer",'
    #                    '"http_user_agent":"$http_user_agent"'
    #            '}';

    ##
    # GZIP Setting
    ##
    gzip                            on;
    gzip_comp_level                 5;
    gzip_buffers                    16 8k;
    gzip_types text/plain application/javascript application/x-javascript text/javascript text/xml text/css;
    gzip_proxied no-cache no-store private expired auth;

    # SSL Setting
    # intermediate configuration
    ssl_protocols                   TLSv1 TLSv1.1 TLSv1.2 TLSv1.3;
    ssl_prefer_server_ciphers       on;
    ssl_early_data                  on;
    ssl_session_timeout             1d;
    # OCSP stapling
    ssl_stapling                    on;
    ssl_stapling_verify             on;

    # Add Alt-Svc headers to negotiate HTTP/3
    add_header Alt-Svc 'h2=":443"; ma=86400' always;
    add_header Strict-Transport-Security "max-age=63072000; includeSubDomains; preload" always;

    # Virtual Host Configs
    include                         /etc/nginx/conf.d/*.conf;
    include                         /etc/nginx/sites-enabled/*;
}
```
