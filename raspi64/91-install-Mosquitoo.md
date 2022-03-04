# Setting Up my Raspberry PI 4 B+
## Install MQTT broker mosquitto

### See also here
[Mosquitoo](https://mosquitto.org)  


### Add OS packages for Mosquitoo
```
sudo apt install mosquitto mosquitto-clients
```

### Set alias for mosquitto
```
sudo tee /etc/profile.d/mosquitto.sh  << EOF
#mosquitto
alias mq-nfo='systemctl status mosquitto'
alias mq-stop='sudo systemctl stop mosquitto'
alias mq-start='sudo systemctl start mosquitto'
alias mq-restart='sudo systemctl restart mosquitto'
alias mq-log='journalctl -u mosquitto -n100 -f'
alias mq-logfile='sudo tail -100f /var/log/mosquitto/mosquitto.log'
EOF
```
