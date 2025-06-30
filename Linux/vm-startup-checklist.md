# Server Basic Start Up Checklist

## Unattended Security Update

```
apt-get update && sudo apt-get upgrade -y
apt install unattended-upgrades -y
dpkg-reconfigure --priority=low unattended-upgrades
```

### Create New User

1. Create new user

```
adduser username
```

2. Add new user into SUDO group

```
usermod -aG sudo username
```

3. Delete user

```
deluser username sudo
```

4. Test by exit and relog with new user

## Control SSH Access by Using SSH Key Pair

1. Make `.ssh` folder

```
mkdir ~/.ssh && chmod 700 ~/.ssh
```

2. Create Key Pair in your local computer and upload it to the server (**please refer to sercure-copy-procotol-scp.md**).

```
ssh-keygen -b 4096 (in your local computer)
ssh-keygen -t rsa (in your local computer)
scp -P port public_key_filename.pub username@serverip:~/.ssh/authorized_keys
```

## Harden SSH Access

1. Modify the `/etc/ssh/sshd_config` using the following configuration. Replace `xxxx` in port configuration to anything except 22.

```
port xxxx
AddressFamily inet
PermitRootLogin no
PasswordAuthentication no
```

2. Restart the ssh service

```
systemctl restart sshd
```

## Firewall Server

1. Check the active port

```
ss -tupln
```

2. Install ufw

```
apt install ufw
```

3. Check ufw status

```
ufw status
```

4. Allow ssh port. Replace `port` using the modify ssh port. Do not delete ` `` ` in the command.

```
ufw allow `ssh port`
```

5. Allow nginx port by using `Nginx HTTPS` for port 443 (HTTPS) or `Nginx Full` for both port 80 and 443 (HTTP and HTTPS)

```
ufw allow `Nginx HTTPS`
```

6. For Apache, please use the following configuration

```
ufw allow 80/tcp
ufw allow 443/tcp
```

## Block Ping Server

1. modify the `/etc/ufw/before.rules` configuration by checking for icmp codes for input and modify or add the following configuration

```
-A ufw-before-input -p icmp --icmp-type echo-request -j DROP
```
