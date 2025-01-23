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

```
apt install snapd
snap install core
snap refresh core
snap install --classic certbot
ln -s /snap/bin/certbot /usr/bin/certbot
certbot --nginx --test-cert
certbot --nginx
certbot delete --cert-name example.com
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
