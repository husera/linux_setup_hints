# Setting Up my Raspberry PI 4 B+
## Basic packages

### Update apt repos
```
sudo apt -y update
sudo apt -y dist-upgrade
```

### Add OS packages
```
sudo apt install -y chkrootkit unrar mc iotop zram-tools
```

### Configure zswap
```
sudo sed -i 's/#SIZE=256/SIZE=512/g' /etc/default/zramswap
sudo systemctl restart zramswap
```
#### check
```
zramswap status
```