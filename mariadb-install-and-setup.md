# mariadb-server setup

## installation

1. Prepare the pgp key

```
apt install apt-transport-https curl
mkdir -p /etc/apt/keyrings
curl -o /etc/apt/keyrings/mariadb-keyring.pgp 'https://mariadb.org/mariadb_release_signing_key.pgp'
```

2. create mariadb list in `/etc/apt/sources.list.d/mariadb.sources` using the following configuration

```
# MariaDB 11.4 repository list - created 2024-08-01 04:28 UTC
# https://mariadb.org/download/
X-Repolib-Name: MariaDB
Types: deb
# deb.mariadb.org is a dynamic mirror if your preferred mirror goes offline. See https://mariadb.org/mirrorbits/ for details.
# URIs: https://deb.mariadb.org/11.4/ubuntu
URIs: https://download.nus.edu.sg/mirror/mariadb/repo/11.4/ubuntu
Suites: jammy
Components: main main/debug
Signed-By: /etc/apt/keyrings/mariadb-keyring.pgp
```

3. install mariadb

```
apt update
apt install mariadb-server
mysql_secure_installation
```

## Connect to the Remote MariaDB

1. Modify the `/etc/mysql/mariadb.conf.d/50-server.cnf` using the following configuration.

```
bind-address = 0.0.0.0
```

2. restart the mariadb server

```
systemctl restart mariadb
```

## SQL Account Management

1. login into mariadb cli.
2. Change `newuser` with new user name `newuserspassword`with new user password and replace `localhost` with external ip address incase the database storage is exist in remote server. Dont delete the singgle quote `''` in new user name and new user ip.

```
CREATE USER 'newuser'@'localhost' IDENTIFIED BY 'newuserspassword';
```

4. Grant privilege specific database.

```
GRANT ALL PRIVILEGES ON yourdatabase.\* TO 'username'@'localhost';
FLUSH PRIVILEGES;

```

5. To grant privilege to all database exist in the server, please use syntax as follows.

```

GRANT ALL PRIVILEGES ON \*.\* TO 'username'@'localhost' WITH GRANT OPTION;
FLUSH PRIVILEGES;

```

## Back-Up and Restore mariadb Database

1. To dump the database or specific table, please change `username` with your username, use `-h dbhost` if your mariadb server is running in remote server and skip it if your mariadb running in localhost, replace `dbname` with your database name, replace `tablename` with your table name and skip it if you want to dump all the table in your database, and replace `sqlfile` with your output file name.

```
mariadb-dump -u username -h dbhost -p dbname tablename > sqlfile.sql --single-transaction --skip-lock-tables

```

## reload back up sql database

2. To restore the database or specific table, please change `username` with your username, use `-h dbhost` if your mariadb server is running in remote server and skip it if your mariadb running in localhost, replace `dbname` with your database name, replace `tablename` with your table name and skip it if you restore all the table in your database, and replace `sqlfile` with your backup file name.

```
mariadb -h dbhost -u username -p dbname tablename < sqlfile.sql
```
