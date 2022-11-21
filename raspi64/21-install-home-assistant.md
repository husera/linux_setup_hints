# Setting Up my Raspberry PI 4 B+
## Home Assistant Core
https://www.home-assistant.io/installation/raspberrypi#install-home-assistant-core

### See also:
[Phoscon](https://phoscon.de/en/raspbee/install#connection)  
[Install](www.home-assistant.io/installation/raspberrypi#install-home-assistant-core)  

### Install dependencies

```
sudo apt install -y python3 python3-dev python3-venv python3-pip bluez libffi-dev libssl-dev \
libjpeg-dev zlib1g-dev autoconf build-essential libopenjp2-7 libtiff5 libturbojpeg0-dev tzdata
```

### Tecnical user "homeassistant"
Create the account:
```
sudo useradd -rm homeassistant -G dialout,gpio,i2c
```

Create the virtual environment:
```
sudo mkdir /srv/homeassistant
sudo chown homeassistant:homeassistant /srv/homeassistant
```
As homeassistant user:
```
sudo -u homeassistant -H -i
cd /srv/homeassistant
python3 -m venv .
source bin/activate
```
Inside the venv:
```
python3 -m pip install wheel
```
Finally install the CORE
```
pip3 install homeassistant
```

### Systemd startup
[reference](https://community.home-assistant.io/t/autostart-using-systemd/199497)
as "pi" user do:
```
sudo tee /etc/systemd/system/home-assistant@homeassistant.service << EOF
[Unit]
Description=Home Assistant
After=network-online.target

[Service]
Type=simple
User=%i
WorkingDirectory=/home/%i/.homeassistant
ExecStart=/srv/homeassistant/bin/hass -c "/home/%i/.homeassistant"
RestartForceExitStatus=100

[Install]
WantedBy=multi-user.target
EOF
```
Now activate it:
```
sudo systemctl --system daemon-reload
sudo systemctl enable home-assistant@homeassistant
sudo systemctl start home-assistant@homeassistant
```


### Change the shell env for homeassistant for more comfort
```
sudo tee /etc/profile.d/homeassistant.sh << EOF
# Comand defaults
alias homeassistant="sudo -u homeassistant -H -i"
EOF
```

