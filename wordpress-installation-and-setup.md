# Wordpress Installation and Setup

## Wordpress Download and Configuration

```
wget https://wordpress.org/latest.tar.gz
tar -xvzf latest.tar.gz
rm latest.tar.gz
mv wordpress /var/www/html
```

## Wordpress configuration

1. Grant permission for wordpress file.

```
chown -R www-data:www-data /var/www/html
chmod -R 755 /var/www/html
```

2. Configuration for wp-config to connect the application into DBMS.

```
cp wp-config-sample.php wp-config.php
nano wp-config.php
```

```
define( 'DB_NAME', 'wordpress_db' );
define( 'DB_USER', 'wordpress_user' );
define( 'DB_PASSWORD', 'your_strong_password' );
define( 'DB_HOST', 'localhost' );
define( 'DB_CHARSET', 'utf8mb4' );
define( 'DB_COLLATE', '' );
```

3. Setting up Nginx server block before certbot ssl installation.

```
server {
    listen 80;
    server_name yourdomain.com www.yourdomain.com;
    root /var/www/html;
    index index.php index.html index.htm;

    location / {
        try_files $uri $uri/ /index.php?$args;
    }

    location ~ \.php$ {
        include snippets/fastcgi-php.conf;
        fastcgi_pass unix:/run/php/php8.1-fpm.sock;
        fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
        include fastcgi_params;
    }

    location ~* \.(jpg|jpeg|png|gif|ico|css|js|svg|woff|woff2|ttf|otf|eot|mp4|webm|ogg|mp3|wav|flac|aac|zip|rar|7z|gz|bz2|tar|tiff|tif)$ {
        expires max;
        log_not_found off;
    }
}
```
