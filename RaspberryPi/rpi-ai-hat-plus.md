# RPI AI Hat Plus Guide

## Enable PCIe Gen 3.0 [^1]

1. To enable PCIe Gen 3.0 speeds, add the following line to /boot/firmware/config.txt:

```
dtparam=pciex1_gen=3
```

2. change the raspberry pi configuration

```
raspi-config
```

3. Select `Advanced Options`

4. Select `PCIe Speed`.

5. Choose `Yes` to enable PCIe Gen 3 mode

6. Select `Finish` to exit.

7. Reboot your Raspberry Pi for your changes to take effect

```
reboot
```

## Install the correct driver [^2]

1. Install the dependencies required to use the NPU

```
apt install hailo-all
```

2. Reboot your device

```
reboot
```

3. To ensure everything is running correctly, run the following command:

```
hailortcli fw-control identify
```

If you see output similar to the following, you’ve successfully installed the NPU and its software dependencies:

```
Executing on device: 0000:01:00.0
Identifying board
Control Protocol Version: 2
Firmware Version: 4.17.0 (release,app,extended context switch buffer)
Logger Version: 0
Board Name: Hailo-8
Device Architecture: HAILO8L
Serial Number: HLDDLBB234500054
Part Number: HM21LB1C2LAE
Product Name: HAILO-8L AI ACC M.2 B+M KEY MODULE EXT TMP
```

Additionally, you can run

```
dmesg | grep -i hailo
```

to check the kernel logs, which should yield output similar to the following:

```
[    3.049657] hailo: Init module. driver version 4.17.0
[    3.051983] hailo 0000:01:00.0: Probing on: 1e60:2864...
[    3.051989] hailo 0000:01:00.0: Probing: Allocate memory for device extension, 11600
[    3.052006] hailo 0000:01:00.0: enabling device (0000 -> 0002)
[    3.052011] hailo 0000:01:00.0: Probing: Device enabled
[    3.052028] hailo 0000:01:00.0: Probing: mapped bar 0 - 000000000d8baaf1 16384
[    3.052034] hailo 0000:01:00.0: Probing: mapped bar 2 - 000000009eeaa33c 4096
[    3.052039] hailo 0000:01:00.0: Probing: mapped bar 4 - 00000000b9b3d17d 16384
[    3.052044] hailo 0000:01:00.0: Probing: Force setting max_desc_page_size to 4096 (recommended value is 16384)
[    3.052052] hailo 0000:01:00.0: Probing: Enabled 64 bit dma
[    3.052055] hailo 0000:01:00.0: Probing: Using userspace allocated vdma buffers
[    3.052059] hailo 0000:01:00.0: Disabling ASPM L0s
[    3.052070] hailo 0000:01:00.0: Successfully disabled ASPM L0s
[    3.221043] hailo 0000:01:00.0: Firmware was loaded successfully
[    3.231845] hailo 0000:01:00.0: Probing: Added board 1e60-2864, /dev/hailo0
```

## Reference

[^1]: [**_Raspberry Pi hardware_** - by Official Raspberry Pi Documentation](https://www.raspberrypi.com/documentation/computers/raspberry-pi.html#pcie-gen-3-0)
[^1]: [**_AI Kit and AI HAT+ software_** - by Official Raspberry Pi Documentation](https://www.raspberrypi.com/documentation/computers/ai.html)
