# Raspberri Pi 5 Initial Setup

## Preinstalation

```
ip=192.168.1.200::192.168.1.1:255.255.255.0:rpi:eth0:off
```

## Post Instalation

1. EEPROM update

```
rpi-eeprom-update
```

2. OS update

```
apt-get update && apt-get upgrade -y
```

## Network Setting

### Identify network setting

1. check connection status

```
nmcli device status
```

2. check connection name

```
nmcli connection show
```

```
nmcli connection show --active
```

### If wlan0 not available

1. configure ifupdown in `/etc/NetworkManager/NetworkManager.conf` using following configuration

```
[ifupdown]
managed=true
```

2. restart the NetworkManager service

```
systemctl restart NetworkManager
```

3. Confirm the registration of wlan0 in the device status

```
nmcli device status
```

4. Add wlan0 as managed connection, change `YOUR_SSID` to your wifi ssid

```
nmcli connection add type wifi ifname wlan0 con-name wlan0 ssid "YOUR_SSID"
```

### Network configuration

1. rename network name if the default name is not "wlan0" and "eth0"

```
nmcli connection modify "preconfigured" connection.id wlan0
nmcli connection modify "Wired connection 1" connection.id eth0
```

2. Configure eth0 static ip, gateway and dns server

```
nmcli connection modify eth0 ipv4.addresses 192.168.1.200/24 ipv4.gateway 192.168.1.1 ipv4.dns "8.8.8.8,8.8.4.4" ipv4.method manual && nmcli connection up eth0
```

3. Configure wlan0 static ip, gateway and dns server

```
nmcli connection modify wlan0 ipv4.addresses 192.168.1.201/24 ipv4.gateway 192.168.1.1 ipv4.dns "8.8.8.8,8.8.4.4" ipv4.method manual && nmcli connection up wlan0
```

4. Confirm the configuration is corectly applied

```
nmcli device show eth0
nmcli device show wlan0
```

5. Make Sure the Changes Persist After Reboot

```
nmcli connection modify eth0 autoconnect yes && nmcli connection modify wlan0 autoconnect yes
```

6. Restart the NetworkManager to ensure the configuration is applied

```
systemctl restart NetworkManager
```

```
sudo nmcli device wifi connect "SSID1" password "PASSWORD1"
sudo nmcli device wifi connect "SSID2" password "PASSWORD2"
sudo nmcli device wifi connect "SSID3" password "PASSWORD3"
```

```
nmcli connection modify "SSID1" connection.autoconnect-priority 10
nmcli connection modify "SSID2" connection.autoconnect-priority 5
```

### Unblock WIFI connection

1. Validate WIFI Blockage

```
rfkill list all
```

2. unblock the soft Block

```
rfkill unblock wifi
```

3. Uplink wlan0

```
ip link set wlan0 up
```

```
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
country=ID

network={
    ssid="SSID1"
    psk="PSK1"
    key_mgmt=WPA-PSK
    priority=10
}

network={
    ssid="SSID2"
    psk="PSK2"
    key_mgmt=WPA-PSK
    priority=5
}

network={
    ssid="SSID3"
    psk="PSK3"
    key_mgmt=WPA-PSK
    priority=2
}
```
