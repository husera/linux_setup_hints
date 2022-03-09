# Setting Up my Raspberry PI 4 B+
## Install Grafana and influxdb and Telegraf

### Doc
    # https://grafana.com/tutorials/install-grafana-on-raspberry-pi/


### Add OS packages for grafana
    sudo wget -q -O - https://packages.grafana.com/gpg.key | sudo apt-key add -
    echo "deb https://packages.grafana.com/oss/deb stable main" | sudo tee /etc/apt/sources.list.d/grafana.list

    sudo apt-get update
    sudo apt-get install -y grafana
    
### change config to serve behind a nginx proxy
    # Hint: https://lvinsf.medium.com/grafana-behind-nginx-reverse-proxy-24ef08da7ad9
    sudo sed -i 's#;serve_from_sub_path = false#serve_from_sub_path = true#' /etc/grafana/grafana.ini
    sudo sed -i 's#;root_url = %(protocol)s://%(domain)s:%(http_port)s/#root_url = %(protocol)s://%(domain)s:%(http_port)s/grafana/#' /etc/grafana/grafana.ini
    
### Grafana: Enable Dashboards Public Access
    sudo vi /etc/grafana/grafana.ini
    ## Search for [auth.anonymous]  -> change to: "enabled = true"
    ## and
    ## "hide_version = true"
    

    
### Autostart service on boot
    sudo /bin/systemctl enable grafana-server
    sudo /bin/systemctl start grafana-server


### Add nginx bash alias
sudo tee /etc/profile.d/grafana.sh << EOF
#nginx
alias g-nfo='systemctl status grafana-server'
alias g-stop='sudo systemctl stop grafana-server'
alias g-start='sudo systemctl start grafana-server'
alias g-restart='sudo systemctl restart grafana-server'
alias g-log='journalctl -u grafana-server -n100 -f'
EOF


### Note
    # Login  admin:admin

### Plugins
    sudo grafana-cli plugins install grafana-simple-json-datasource
    sudo grafana-cli plugins install yesoreyeram-infinity-datasource
    sudo grafana-cli plugins install volkovlabs-rss-datasource
    sudo grafana-cli plugins install frser-sqlite-datasource
    sudo grafana-cli plugins install fetzerch-sunandmoon-datasource
    sudo grafana-cli plugins install andig-darksky-datasource
    sudo grafana-cli plugins install grafana-singlestat-panel
    sudo grafana-cli plugins install speakyourcode-button-panel
    sudo grafana-cli plugins install grafana-clock-panel
    sudo grafana-cli plugins install flant-statusmap-panel
    sudo grafana-cli plugins install snuids-trafficlights-panel
    sudo grafana-cli plugins install corpglory-progresslist-panel
    sudo grafana-cli plugins install marcusolsson-dynamictext-panel
    sudo grafana-cli plugins install mxswat-separator-panel
    sudo grafana-cli plugins install gretamosa-topology-panel

### Finally restart grafana
    sudo systemctl restart grafana-server
    
 ---
 
 ## Influx
 wget -qO- https://repos.influxdata.com/influxdb.key | gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/influxdb.gpg > /dev/null
export DISTRIB_ID=$(lsb_release -si); export DISTRIB_CODENAME=$(lsb_release -sc)
echo "deb [signed-by=/etc/apt/trusted.gpg.d/influxdb.gpg] https://repos.influxdata.com/${DISTRIB_ID,,} ${DISTRIB_CODENAME} stable" | sudo tee /etc/apt/sources.list.d/influxdb.list > /dev/null

sudo apt-get update && sudo apt-get install influxdb2



