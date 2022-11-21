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
sudo -u homeassistant -H -s
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


### Change the shell env for homeassistant
```
sudo tee /etc/profile.d/homeassistant.sh << EOF
# Comand defaults
alias homeassistant="sudo -u homeassistant -s"
EOF
```

