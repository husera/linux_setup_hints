#    Setting Up my Raspberry PI 4 B+
## Node RED


### Add OS packages for NodeRed and install from GIT
```
sudo apt-get install -y build-essential

bash <(curl -sL https://raw.githubusercontent.com/node-red/linux-installers/master/deb/update-nodejs-and-nodered)
node-red admin init
```

### Start NodeRed as a service
```
sudo systemctl enable nodered.service
sudo systemctl start nodered.service
```

### Bash file for NodeRed
```
sudo tee /etc/profile.d/nodered.sh << EOF
#nodered
alias red-nfo='systemctl status nodered'
alias red-stop='sudo systemctl stop nodered'
alias red-start='sudo systemctl start nodered'
alias red-restart='sudo systemctl restart nodered'
alias red-log='journalctl -u nodered -n100 -f'
EOF
```
