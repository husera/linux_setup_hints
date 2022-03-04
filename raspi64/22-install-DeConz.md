# Setting Up my Raspberry PI 4 B+
## Deconz

### See also:
[Phoscon](https://phoscon.de/en/raspbee/install#connection)  
[Install](https://phoscon.de/en/conbee/install#raspbian)  




### Configure Serial interface
```
sudo raspi-config
```
> Interfacing Options → Serial  
>   
> Would you like a login shell accessible over serial? → No  
> Would you like the serial port hardware to be enabled? → Yes  
> Note: Changes to access rights only become active after a restart.  

Also disable hciuart
```
sudo systemctl disable hciuart
```

### Give access rights to the serial device by adding the user to the correct groups
```
sudo gpasswd -a $USER dialout
```

### Add OS packages for ZigBee2mqtt
```
sudo apt-get install -y nodejs npm git make g++ gcc
```

Verify that the correct nodejs and npm (automatically installed with nodejs) version has been installed:
```
node --version  # Should output v10.X, v12.X, v14.X, v15.X or V16.X
npm --version  # Should output 6.X or 7.X
```

### Add the Key and the repo to apt
```
wget -O - http://phoscon.de/apt/deconz.pub.key | \
sudo apt-key add -

sudo sh -c "echo 'deb http://phoscon.de/apt/deconz \
$(lsb_release -cs) main' > \
/etc/apt/sources.list.d/deconz.list"
```

### Install dependencies (as user "pi")
```
sudo apt update
sudo apt install deconz
```

### Change the port of the service (so we can use nginx as a reverse proxy)
```
/etc/systemd/system/deconz.service.d/override.conf

sudo tee<<EOF
[Service]
ExecStart=
ExecStart=/usr/bin/deCONZ -platform minimal --http-port=8080 --ws-port=8081 --auto-connect=1
EOF

sudo systemctl daemon-reload
```


### Enable and start the service
```
sudo systemctl enable deconz.service
sudo systemctl start deconz.service
```


### Add shell alias for zigbee2mqtt
```
sudo tee /etc/profile.d/zigbee2mqtt.sh << EOF
#zigbee2mqtt
alias de-nfo='systemctl status deconz'
alias de-stop='sudo systemctl stop deconz'
alias de-start='sudo systemctl start deconz'
alias de-restart='sudo systemctl restart deconz'
alias de-log='journalctl -u deconz -n100 -f'
EOF
```
