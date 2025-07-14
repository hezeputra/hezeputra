# Custom Boot Splash Screen on Linux

## Plymouth installation

1. Install plymouth

```
apt install plymouth-themes
```

2. Check plymouth theme list

for debian and its derivative

```
plymouth-set-default-theme --list
```

for ubuntu and its derivative

```
update-alternatives --config default.plymouth
```

3. Apply changes

for X86 Linux

```
update-initramfs -u
```

for Raspberry Pi OS

```
sudo update-initramfs -c -k $(uname -r)
```

## Create New Plymouth

1. Create the plymouth theme configuration file

```
touch {your-theme}.plymouth
```

2. Edit your custom configuration file with your config

```
nano {your-theme}.plymouth
```

```
[Plymouth Theme]
Name={Plymouth Theme Name}
Description={Plymouth Theme Description}
ModuleName=script

[script]
ImageDir=/usr/share/plymouth/themes/{your-theme}
ScriptFile=/usr/share/plymouth/themes/{your-theme}/{your-theme}.script
```

3. Install splash screen into plymouth

After you have the Plymouth theme installed into the directory, you will need to add the theme to the default.plymouth

```
update-alternatives --install /usr/share/plymouth/themes/default.plymouth default.plymouth /usr/share/plymouth/themes/{your-theme}/{your-theme}.plymouth 100
```

> [!IMPORTANT]
>
> The theme .plymouth file path is /usr/share/plymouth/themes/{your-theme}/{your-theme}.plymouth
> The "100" config at the last param is priority of your theme, the default is 100

## Remove the Boot Text ("Quiet Splash")

1. Edit GRUB configuration

```
nano /etc/default/grub
```

2. turn of splash

```
GRUB_CMDLINE_LINUX_DEFAULT="quiet splash"
```

> [!IMPORTANT]
>
> Optional: Remove Boot Messages
> GRUB_CMDLINE_LINUX_DEFAULT="quiet splash loglevel=0"
> Optional: Completely remove boot log
> GRUB_CMDLINE_LINUX_DEFAULT="quiet splash loglevel=0 rd.systemd.show_status=auto vt.global_cursor_default=0"

3. Disable the GRUB Menu (auto-boot into Ubuntu)

```
GRUB_TIMEOUT=0
```

4. Update GRUB configuration

```
update-grub
```

## Disable the GRUB Menu (auto-boot into Ubuntu)

## Apply boot

```
sudo plymouth-set-default-theme spinner
```

## Reference

[^1]: [**_How do I manually install Plymouth Theme?_** - by Bacchus](https://ubuntu-mate.community/t/how-do-i-manually-install-plymouth-theme/15924)
[^2]: [**_Plymouth_** - by Ubuntu Manual](https://manpages.ubuntu.com/manpages/focal/man1/plymouth.1.html)
[^3]: [**_Plymouth_** - by Ubuntu Wiki](https://wiki.ubuntu.com/Plymouth)
[^3]: [**_Plymouth Script_** - by Freedesktop](https://www.freedesktop.org/wiki/Software/Plymouth/Scripts/)
