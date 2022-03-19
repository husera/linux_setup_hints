# Setting Up my Raspberry PI 4 B+
## Basic packages

### Update apt repos
```
sudo apt -y update
sudo apt -y dist-upgrade
```

### Add OS packages
```
sudo apt install -y chkrootkit unrar mc iotop zram-tools rsync
```

## Configure zswap
```
sudo sed -i 's/#SIZE=256/SIZE=512/g' /etc/default/zramswap
sudo systemctl restart zramswap
```
#### check
```
zramswap status
```

## Log 2 Ram
[See on Github](https://github.com/azlux/log2ram)

```
echo "deb [signed-by=/usr/share/keyrings/azlux-archive-keyring.gpg] http://packages.azlux.fr/debian/ bullseye main" | sudo tee /etc/apt/sources.list.d/azlux.list
sudo wget -O /usr/share/keyrings/azlux-archive-keyring.gpg  https://azlux.fr/repo.gpg
sudo apt update
sudo apt install log2ram

# Change Size to 100M and also enable compression (requires zram)
sudo sed -i 's/SIZE=40M/SIZE=100M/' /etc/log2ram.conf
sudo sed -i 's/ZL2R=false/ZL2R=true/' /etc/log2ram.conf

# Change Systemd journal maxsize to 25M
sudo sed -i 's/#SystemMaxUse=/SystemMaxUse=25M/' /etc/systemd/journald.conf
sudo systemctl restart systemd-journald

# Finally reboot to activate
sudo reboot
```
