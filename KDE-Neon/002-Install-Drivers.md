# Setting Up my KDE neon
### Update PCI Database
```
sudo update-pciids
```
    # Check installed Hardware
    lspci
    # Full Report:
    sudo lshw

    # Infos about GPU:
    sudo lshw -class display
    
# nur LapTops
###################################################################################################
# You can use TLP, a tool that you install and then forget about it because it automatically tweaks
# your system for better power usage / battery life.
    sudo apt-get -y install tlp thermald linux-tools-generic

    # Start (required only the first time)
    sudo tlp start
    sudo service thermald start

    sudo systemctl enable tlp
    sudo systemctl enable thermald

# add Governor to Grub Command_Line:
    sudo vi /etc/default/grub
    # add to GRUB_CMDLINE_LINUX_DEFAULT:
        intel_pstate=enable
    sudo update-grub

    # check after REBOOT
    cpupower frequency-info


# Nvidia Drivers
###################################################################################################
#
# NVidia PPA (optional)
    sudo add-apt-repository ppa:graphics-drivers/ppa
    sudo apt update

# See options:
    ubuntu-drivers devices

# install recommended
    sudo ubuntu-drivers autoinstall
