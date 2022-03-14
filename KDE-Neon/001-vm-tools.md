# Setting Up my KDE Neon
### Readings
(ItsFoss guide)(https://itsfoss.com/virtualbox-guest-additions-ubuntu/)

### detect VM-Guest is running on which hypervisor
```
sudo dmidecode -s system-manufacturer
```

### install VmWare Tools
```
    sudo apt install open-vm-tools-desktop 
```

### virtual BOX Guest Additions (alternative)
```
    sudo apt-get install dkms build-essential linux-headers-generic
```    

```
# Change to the directory where your CD-ROM drive is mounted and execute as root:
    sh ./VBoxLinuxAdditions.run

```
### we need to reboot
```
    sudo reboot
```
    # Berechtigung shared folder
    sudo usermod -a -G vboxusers $USER

    # Nur beim Error:
        # SMBus base address uninitialized - upgrade bios or use force_addr=0xaddr

            #This error is caused by VM having no smbus but Ubuntu always trying to load the module.
            #It doesn't affect anything but is a bit annoying.

        # check
        sudo vi /etc/modprobe.d/blacklist.conf

        # adding the following to the end of the file:
        blacklist i2c_piix4

        # Update the initramfs
        sudo update-initramfs -u -k all
