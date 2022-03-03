# Setting Up my Raspberry PI 4 B+
## Start and sysctl


### Hints and docs:
- [Pi imager](https://www.raspberrypi.com/news/raspberry-pi-imager-imaging-utility)
- [Git cheatsheet](https://education.github.com/git-cheat-sheet-education.pdf)


#### write custom sysctl file
```
sudo tee /etc/sysctl.d/01-alex.conf <<EOF
# Do less swapping
vm.swappiness = 5
# Improve cache management - ok if more than 1 GB Ram"
vm.vfs_cache_pressure=50
vm.dirty_ratio = 50
vm.dirty_background_ratio = 5
# Disable IP V6 - check first if my network is V4 only
et.ipv6.conf.all.disable_ipv6 = 1
net.ipv6.conf.default.disable_ipv6 = 1
net.ipv6.conf.lo.disable_ipv6 = 1
EOF
```

#### load new sysctl file
```
sudo sysctl -q --system
```
