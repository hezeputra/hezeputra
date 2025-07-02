# Installing Proxmox in Raspberry Pi OS

This is my note to install Proxmox VE port for Arm64 in Raspberry Pi OS. The latest version that I install is **Proxmox 8.3 in a Raspberry Pi OS (Bookworm Deb 12.8) on Raspberry Pi 5 in January 2025**. This note doesn't use UEFI boot that is showed by several tech enthusiast[^1] [^2], instead the proxmox running on top of Raspberry Pi OS. Huge credit I give to enjikaka's instruction at Github Gists as my main reference[^3].

## Step 1 - Flashing the OS (headless instalation)

I prefer to use headless installation on Raspberry Pi OS Lite 64 Bit. When you intend to use NVMe SSD as your primary boot device from a fresh new Raspberry Pi, please boot from Micro SD first and update the boot order. This step would trigger EEPROM update for the Raspberry Pi.

### Step 1.1 General Installation Guide

The installation will be verry simple and straightforward. Install "RPi OS Lite 64-bit" with [Raspberry Pi Imager](https://www.raspberrypi.com/software/). There are four main parameter to install the Raspberry Pi OS as follows:

1. **Chose Device**, chose your Raspberry Pi device;
2. **Chose OS**, in this case chose **"RPi OS Lite 64-bit"** under **"Raspberry Pi OS (Other)"** OS list;
3. **Chose Storage**, chose your Micro SD Card; and
4. **Advance Option**, you can leave it all default, but I recommend you to update the device **hostname**, **username and password**, **enable SSH**, and **authorized_keys (to lazy to type password every time I access the device via SSH)**.

### Step 1.2 Booting from Micro SD Card

You can install the OS using **Step 1.1**. Please don't forget to prepare external Micro SD card reader if your laptop or PC doesn't have it built in.

### Step 1.3 Booting from NVMe SSD

if your Raspberry Pi is brand new and/or never use NVMe SSD as a boot device before, please boot from Micro SD first using **Step 1.1 and 1.2**. Please don't forget to prepare NVMe HAT to connect your NVMe SSD to your Raspberry Pi. After installing the Raspberry OS into Micro SD card, you can install the Raspberry Pi OS on your NVMe SSD using **Step 1.1**. While waiting for the Raspberry OS installation on NVMe SSD complete, you can prepare the Raspberry Pi using instruction as follows:

1. Ensure your system is up to date by running `sudo apt-get update && sudo apt-get upgrade -y`;
2. Run the latest EEPROM version by typing `sudo rpi-eeprom-update -a`;
3. Type `sudo raspi-config`;
4. Select option `6. Advance Option` in the Menu > select option `B2. NVMe/USB Boot` > select `Ok` and follow the process > Select `Finish` > reboot if your NVMe SSD is ready; and
5. Install your NVMe HAT and NVMe SSD to your Raspberry Pi.

## Step 2 - Locate your Raspberry Pi in Your Network for Headless Installation

1. access your router to locate your Raspberry Pi (typically 192.168.1.1);
2. access your device using `ssh yourusername@ipaddress`;
3. launch the network config GUI with `nmtui`; and
4. adjust your network configuration to the static ip.

> [!IMPORTANT]
>
> 1. Replace `yourusername` with the username that is set in **Step 1.1**.
> 2. Replace `ipaddress` with ip address that you locate in **Step 2 Point 1**.

## Step 3 - Install Updates

```
apt-get update && apt-get upgrade -y
```

## Step 4 - Configure your host and hostname file

1. Configure your hosts file in `nano /etc/hosts` using configuration as follows:

```
127.0.0.1 localhost yourhostname
::1 localhost ip6-localhost ip6-loopback
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters

192.168.0.XXX yourhostname
```

2. Configure your hostname file in `nano /etc/hostname` using configuration as follows:

```
yourhostname
```

3. Reboot your device to apply changes

```
reboot
```

> [!IMPORTANT]
>
> 1. Replace `192.168.0.XXX` with the static IP of your Raspberry Pi.
> 2. Replace `yourhostname` with hostname of your choice. If you already setup your hostname in **Step 1.1**, you would likely to find the `yourhostname` already filled by hostname of your choice.

## Step 5 - Add Proxmox VE Port to your apt source

1. Add proxmox port for debian bookworm

```
echo "deb [arch=arm64] https://mirrors.apqa.cn/proxmox/debian/pve bookworm port" > /etc/apt/sources.list.d/pveport.list
curl https://mirrors.apqa.cn/proxmox/debian/pveport.gpg -o /etc/apt/trusted.gpg.d/pveport.gpg
```

2. Update the apt repository

```
apt-get update
apt-get upgrade -y
apt-get full-upgrade -y
apt-get dist-upgrade -y
```

3. Download proxmox and its dependencies

```
apt-get install ifupdown2
apt-get install proxmox-ve postfix open-iscsi chrony mmc-utils usbutils
```

## Step 6 - Configure your network interface and DNS server

1. Configure your network interface in `/etc/network/interfaces` using configuration as follows:

```
# interfaces(5) file used by ifup(8) and ifdown(8)
# Include files from /etc/network/interfaces.d:
# source /etc/network/interfaces.d/*

auto lo
iface lo inet loopback

iface eth0 inet manual

auto vmbr0
iface vmbr0 inet static
    address 192.168.0.XXX/24
    gateway 192.168.0.1
    bridge-ports eth0
    bridge-stp off
    bridge-fd 0
```

2. Configure your nameserver in `/etc/resolv.conf` using configuration as follows:

```
nameserver X.X.X.X

```

3. Reboot your device to apply changes

```
reboot
```

> [!IMPORTANT]
>
> 1. Replace `192.168.0.XXX` with the static IP of your Raspberry Pi.
> 2. Replace `X.X.X.X` with nameserver of your choice, for example 8.8.8.8 (google) or 1.1.1.1 (cloudflare)

## Step 7 - Assign a password to your root user

Run `sudo -i` to access the root prompt, then run `passwd` to set your password. This will be the root password for the Proxmox UI.

## Step 8 - Done, Access the proxmox in your local network

Done. You can now reach your Proxmox UI on http://192.168.0.XXX:8006 and login with the username root and the password you set in step 7.

> [!IMPORTANT]
>
> 1. Replace `192.168.0.XXX` with the static IP of your Raspberry Pi.

## Reference

[^1]: [**_I built a Proxmox home lab using my Raspberry Pi - here's how I did it_** - by Ayush Pande at xda-developers.com](https://www.xda-developers.com/install-proxmox-on-raspberry-pi/)
[^2]: [**_Installing Proxmox 8.1 on Raspberry Pi 5_** - by Novaspirit Tech at youtube](https://www.youtube.com/watch?v=oe1_JVl63a0&ab_channel=NovaspiritTech)
[^3]: [**_Installing Proxmox on Raspberry Pi 4 and 5_** - by enjikaka at Github Gists](https://gist.github.com/enjikaka/52d62c9c5462748dbe35abe3c7e37f9a)
