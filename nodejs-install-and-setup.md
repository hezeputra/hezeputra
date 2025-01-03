# NodeJS Installation and Managing-Monitoring Application using PM2

## NodeJS Installation

1. `wget -qO- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash`
2. `nvm install node`
3. `npm install pm2@latest -g`

## Managing and Monitoring NodeJS Application using PM2

### Managing Application

to initialize app :

```
pm2 start app.js --name=app_name
```

to restart app :

```
pm2 restart app_name
```

to reload app :

```
pm2 reload app_name
```

to stopping app :

```
pm2 stop app_name
```

to delete app :

```
pm2 delete app_name
```

### Monitoring Application

to manually check the raw log file, please navigate to `~/.pm2/logs`, to watch the logs use the following command :

```
pm2 logs
```

to List the status of all application managed by PM2 :

```
pm2 [list|ls|status]
```
