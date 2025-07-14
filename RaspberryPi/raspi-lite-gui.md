# Raspi Lite GUI

> [!IMPORTANT]
>
> perform every command at your `user` environment. Do not perform any command at root environment or under `sudo -i` or any other environment related to the root user. Unless, your configuration will never going to be work.

1. setup raspberry pi auto login at raspberry pi config in menu `System Options` > `Auto Login` > `Console Autologin`

```
sudo raspi-config
```

2. update the apt repository

```
sudo apt update && sudo apt upgrade -y

```

3. install all the needed software dependencies

```
sudo apt install --no-install-recommends xserver-xorg x11-xserver-utils xinit openbox chromium-browser -y
```

4. Create startx config file

```
nano ~/.xinitrc
```

```
xset s off
xset -dpms
xset s noblank

openbox-session &

while true; do
        chromium-browser --noerrdialogs --disable-infobars --kiosk http://localhost:80
        sleep 5
done
```

5. Make the startx config file executeable

```
chmod +x ~/.xinitrc
```

6. Create startx init file

```
# If this is not a login shell, exit
[ -z "$LOGIN_SHELL" ] && [ -z "$BASH" ] && return

# Only run startx if we're on tty1 and no X session is active
if [ -z "$DISPLAY" ] && [ "$(tty)" = "/dev/tty1" ]; then
  startx
fi
```

## Hide mouse animation and display

1.  install all the needed software dependencies

```
sudo apt install unclutter
```

2. Initiate unclutter by adding line `unclutter -idle 0.01 -root &` into `~/.xinitrc`. Hence, the finale `~/.xinitrc` can be seen in the following code.

```
xset s off
xset -dpms
xset s noblank

unclutter -idle 0.01 -root &

openbox-session &

while true; do
        chromium-browser --noerrdialogs --disable-infobars --kiosk http://localhost:80
        sleep 5
done
```
