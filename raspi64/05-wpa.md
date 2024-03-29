# Setting Up my Raspberry PI 4 B+
## Wifi Setup

### Set NetWork WPA settings
```
sudo tee /etc/wpa_supplicant/wpa_supplicant.conf <<EOF
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
ap_scan=1
country=CH

network={
        ssid="ALEX-01"
        psk=xxxxxxxxxxxxxxxxx
        id_str="ZenBook"
        priority=1
}

network={
        ssid="PlanetExpressBase"
        psk=xxxxxxxxxxxxxxxxxx
        id_str="Home"
        priority=1
}
EOF
```
#### to check
```
sudo more /etc/wpa_supplicant/wpa_supplicant.conf
```


### Generate PSK passwords:
- sample:
```
wpa_passphrase "My-Wifi" "MyPassword"
```
- Sample output:
```
   network={
        ssid="My-Wifi"
        #psk="MyPassword"
        psk=e26fc64ab78c240890766a8c9872e3a284ab5344821377667cc24513fb60745c
   }
```
- -> add passwords manually to the file !

### Set the new interfaces to dhcp -> reserved in the dhcp-server
```
sudo tee /etc/network/interfaces.d/wpa-instefaces <<EOF
iface ZenBook inet dhcp
iface Home inet dhcp
EOF
```

### disable random mac address for NetworkManager ###
not needed since NM is not in use 
```
# sudo mkdir -p /etc/NetworkManager/conf.d/
# sudo tee /etc/NetworkManager/conf.d/30-mac-randomization.conf <<EOF
# [device-mac-randomization]
# wifi.scan-rand-mac-address=no
# 
# [connection-mac-randomization]
# ethernet.cloned-mac-address=permanent
# wifi.cloned-mac-address=permanent
EOF
```
### Static ETH
```
sudo tee /etc/network/interfaces.d/eth0 <<EOF
# The loopback network interface
auto lo
iface lo inet loopback

auto eth0
iface eth0 inet static
 address 172.16.69.6
 netmask 255.255.255.0
 gateway 172.16.69.1
 dns-nameservers 172.16.69.5 1.1.1.1
EOF
```
