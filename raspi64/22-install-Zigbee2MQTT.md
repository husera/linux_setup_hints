# Setting Up my Raspberry PI 4 B+
## Zig Bee 2 MQtt

### See also:
[Phoscon](https://phoscon.de/en/raspbee/install#connection)  
and:  
[ZigBee2MQtt install guide](https://www.zigbee2mqtt.io/guide/installation/01_linux.html)  
[ZigBee2MQtt troubbleshooting guide](https://www.zigbee2mqtt.io/guide/installation/20_zigbee2mqtt-fails-to-start.html)

Note:
MQTT needs to be online !

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
sudo usermod -a -G dialout $USER
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

### Clone Zigbee2MQTT repository
```
git clone https://github.com/Koenkk/zigbee2mqtt.git
sudo mv zigbee2mqtt /opt/zigbee2mqtt
```

### Install dependencies (as user "pi")
```
cd /opt/zigbee2mqtt
npm ci
```

### Configuring
```
vi /opt/zigbee2mqtt/data/configuration.yaml
```
For RaspBee II:  
> serial:  
>  adapter: deconz  

### Add the service file
```
sudo tee /etc/systemd/system/zigbee2mqtt.service << EOF
[Unit]
Description=zigbee2mqtt
After=network.target

[Service]
ExecStart=/usr/bin/npm start
WorkingDirectory=/opt/zigbee2mqtt
StandardOutput=inherit
# Or use StandardOutput=null if you don't want Zigbee2MQTT messages filling syslog, for more options see systemd.exec(5)
StandardError=inherit
Restart=always
User=pi

[Install]
WantedBy=multi-user.target
EOF
```

### Add shell alias for zigbee2mqtt
```
sudo tee /etc/profile.d/zigbee2mqtt.sh << EOF
#zigbee2mqtt
alias z-nfo='systemctl status zigbee2mqtt'
alias z-stop='sudo systemctl stop zigbee2mqtt'
alias z-start='sudo systemctl start zigbee2mqtt'
alias z-restart='sudo systemctl restart zigbee2mqtt'
alias z-log='journalctl -u zigbee2mqtt -n100 -f'
EOF
```
