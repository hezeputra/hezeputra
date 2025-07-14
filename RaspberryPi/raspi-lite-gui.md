# Raspi Lite GUI

> [!IMPORTANT]
>
> perform every command at your `user` environment. Do not perform any command at root environment or under `sudo -i` or any other environment related to the root user. Unless, your configuration will never going to be work.

1. setup raspberry pi auto login at raspberry pi config in menu `System Options` > `Auto Login` > `Console Autologin`

```
sudo raspi-config
```

2. Edit /boot/config.txt

```
gpu_mem=128
framebuffer_width=1920
framebuffer_height=1080
```

2. update the apt repository

```
sudo apt update && sudo apt upgrade -y

```

3. install all the needed software dependencies

```
sudo apt install xserver-xorg x11-xserver-utils xinit openbox chromium-browser unclutter netcat-openbsd -y
```

4. Create xorg modesetting device driver

```
nano /etc/X11/xorg.conf.d/99-modesetting.conf
```

```
Section "Device"
    Identifier  "Default Device"
    Driver      "modesetting"
EndSection
```

5. Create startx config file at `~/.xinitrc`

```
nano ~/.xinitrc
```

```
#!/bin/bash

xset s off
xset -dpms
xset s noblank

unclutter -idle 0.01 -root &

openbox-session &

while true; do
        chromium-browser --noerrdialogs --disable-infobars --kiosk http://localhost:80 --use-gl=egl
        sleep 5
done
```

6. Make the startx config file executeable

```
chmod +x ~/.xinitrc
```

7. Create startx init file at `~/.bash_profile`

```
nano ~/.bash_profile
```

```
#!/bin/bash

[ -z "$LOGIN_SHELL" ] && [ -z "$BASH" ] && return

while ! nc -z localhost 80; do
    sleep 0.5
done

if [ -z "$DISPLAY" ] && [ "$(tty)" = "/dev/tty1" ]; then
        while true; do
        startx >/dev/null 2>&1
        if [ $? -ne 0 ]; then
            sudo reboot
        fi
        sleep 2
    done
fi
```

8. Ensure proper permission added to the user so reboot can be done without password

```
sudo visudo
```

```
{user}     ALL=(ALL) NOPASSWD: /sbin/reboot
```

> [!IMPORTANT]

> please replace `{user}` with your username.

9. Suppress login messages

```
touch ~/.hushlogin
```
