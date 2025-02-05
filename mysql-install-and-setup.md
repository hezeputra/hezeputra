# mysql-server setup

## Instalation

1. install mysql-server.

```
apt install mysql-server
```

2. modify root password.

```
mysql
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'yourpassword';
FLUSH PRIVILEGES;
```

3. test new root password.

```
mysql -u root -p
```

## Connect to the Remote MySQL

1. Modify the `/etc/mysql/mysql.conf.d/mysqld.cnf` using the following configuration.

```
bind-address = 0.0.0.0
```

2. restart the mysql server

```
systemctl restart mysql
```

## uninstall sql

```
apt clean
apt purge mysql\*
apt update
```

## SQL Account Management

1. login into mysql cli.
2. check user list.

```
select user from mysql.user;
```

3.  Change `newuser` with new user name `newuserspassword`with new user password and replace `localhost` with external ip address incase the database storage is exist in remote server. Dont delete the singgle quote `''` in new user name and new user ip.

```
CREATE USER 'newuser'@'localhost' IDENTIFIED BY 'newuserspassword';
```

4. Grant privilege specific database.

```
GRANT ALL PRIVILEGES ON yourdatabase.* TO 'username'@'localhost';
FLUSH PRIVILEGES;

```

5. To grant privilege to all database exist in the server, please use syntax as follows.

```

GRANT ALL PRIVILEGES ON *.* TO 'username'@'localhost' WITH GRANT OPTION;
FLUSH PRIVILEGES;

```

## Back-Up and Restore MySQL Database

1. To dump the database or specific table, please change `username` with your username, use `-h dbhost` if your mysql server is running in remote server and skip it if your mysql running in localhost, replace `dbname` with your database name, replace `tablename` with your table name and skip it if you want to dump all the table in your database, and replace `sqlfile` with your output file name.

```
mysqldump -u username -h dbhost -p dbname tablename > sqlfile.sql --single-transaction --skip-lock-tables

```

## reload back up sql database

2. To restore the database or specific table, please change `username` with your username, use `-h dbhost` if your mysql server is running in remote server and skip it if your mysql running in localhost, replace `dbname` with your database name, replace `tablename` with your table name and skip it if you restore all the table in your database, and replace `sqlfile` with your backup file name.

```
mysql -h dbhost -u username -p dbname tablename < sqlfile.sql
```
