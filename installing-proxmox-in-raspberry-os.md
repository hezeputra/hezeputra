### Installing Proxmox in Raspberry Pi OS

This is my note to install Proxmox VE port for Arm64 in Raspberry Pi OS. The latest version that I install is Proxmox 8.3 in a Raspberry Pi OS (Bookworm Deb 12.8) on Raspberry Pi 5 in January 2025. This note doesn't use UEFI boot that is showed by several tech enthusiast [^1] [^2], instead the proxmox running on top of Raspberry Pi OS. Huge credit I give to enjikaka's instruction at Github Gists as my main reference[^3].

## Step 1 - Flashing the OS (headless instalation)

I prefer to use headless installation on Raspberry Pi OS Lite 64 Bit. When you intend to use NVMe SSD as your primary boot device from a fresh new Raspberry Pi, please boot from Micro SD first and update the boot order. This step would trigger EEPROM update for the Raspberry Pi.

### Step 1.1 Booting from Micro SD Card

The installation will be verry simple and straightforward. Install "RPi OS Lite 64-bit" with [Raspberry Pi Imager](https://www.raspberrypi.com/software/). Please don't forget to prepare external Micro SD card reader if your laptop or PC doesn't have it built in. There are four main parameter to install the Raspberry Pi OS as follows:

1. **Chose Device**, chose your Raspberry Pi device;
2. **Chose OS**, in this case chose **"RPi OS Lite 64-bit"** under **"Raspberry Pi OS (Other)"** OS list;
3. **Chose Storage**, chose your Micro SD Card; and
4. **Advance Option**, you can leave it all default, but I recommend you to update the device **hostname**, **username and password**, **enable SSH**, and **authorized_keys (to lazy to type password every time I access the device via SSH)**.

### Step 1.2 Booting from NVMe SSD

## Step 2 - Network configuration

[^1] [**_I built a Proxmox home lab using my Raspberry Pi - here's how I did it_** - by Ayush Pande at xda-developers.com](https://www.xda-developers.com/install-proxmox-on-raspberry-pi/)
[^2] [**_Installing Proxmox 8.1 on Raspberry Pi 5_** - by Novaspirit Tech at youtube](https://www.youtube.com/watch?v=oe1_JVl63a0&ab_channel=NovaspiritTech)
[^3] [**_Installing Proxmox on Raspberry Pi 4 and 5_** - by enjikaka at Github Gists](https://gist.github.com/enjikaka/52d62c9c5462748dbe35abe3c7e37f9a)
