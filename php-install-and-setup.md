# PHP Runtime Instalation and Multiple PHP Version in One Server

## PHP Install

1. check the available php module. You can replace 8.0 version to another version, e.g. 8.1, 8.2, etc.

```
apt-cache search php|grep ^php8.0
```

2. install the php-fpm and its module

```
apt install php8.0-fpm php8.0-xml php8.0-curl php8.0-mysql php8.0-cli php8.0-opcache php8.0-mbstring php8.0-gd php8.0-cgi php8.0-common php8.0-ldap php8.0-zip php8.0-bcmath
```

## Multiple PHP Version

```
apt install software-properties-common -y
add-apt-repository ppa:ondrej/php
apt update -y
update-alternatives --config `php select default php cli`
```

**_Install other php version after running this command_**

## PHP Integrate Nginx

1. uncomment the `location ~ \.php$ { include snippets/fastcgi-php.conf; fastcgi_pass unix:/run/php/php8.1-fpm.sock; }`
2. reload the nginx `systemctl reload nginx`

## PHP Install Composer

1. install composer for package manager, see in [composer](https://getcomposer.org/download/)

## PHP Install phpmyadmin

```
apt install phpmyadmin php-mbstring php-zip php-gd php-json php-curl
ln -s /usr/share/phpmyadmin /var/www/phpmyadmin
```

## PHP Laravel Must Read

### Modify the owner and permission of laravel's log folder

```
chmod -R ug+rwx storage bootstrap/cache
chgrp -R www-data storage bootstrap/cache
```

### Alternative command to modify the owner and permission of laravel's log folder

Modify the permission storage log folder and its sub folder

```
chown -R root:www-data storage
chown -R root:www-data storage/*
chmod 775 storage
chmod 775 storage/*
```

### Additional command

Generate the jwt key and app key

```
php artisan jwt:secret
php artisan key:generate
```
