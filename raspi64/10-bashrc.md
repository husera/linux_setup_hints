# Setting Up my Raspberry PI 4 B+
## All my bash alias

### #Set apt alias
```
sudo tee /etc/profile.d/apt.sh << EOF
# Apt-get
alias install='sudo /usr/bin/apt install'
alias remove='sudo /usr/bin/apt remove'
alias autoremove='sudo /usr/bin/apt autoremove --purge'
alias purge='sudo /usr/bin/apt purge'
alias update='sudo /usr/bin/apt update -y && apt list --upgradable'
alias upgrade='sudo /usr/bin/apt full-upgrade'
alias search='/usr/bin/apt-cache search'
alias clean='sudo /usr/bin/apt autoclean'
EOF
```

### #Set system alias ( show something )
```
sudo tee /etc/profile.d/sys-alias.sh << EOF
#
# systemctl
alias sh-services='systemctl list-unit-files --no-pager --state enabled,disabled'
alias sh-timers='sudo systemctl --type timer'
alias sh-logs='journalctl -xn50'
alias sh-status='systemctl status'
alias sh-ps='ps -axfw'
#
# Show system parts
alias sh-ip-ext='curl ipinfo.io/ip'
alias sh-ip='ip addr show scope global | grep inet'
alias sh-ports='sudo netstat -plte --numeric-ports --numeric-hosts'
alias sh-mounts='mount | sort -k 3 | column -t'
alias sh-df='df -h -txfs -text4 | sort -rk5n,2'
alias sh-du='du -d1s -h'
alias sh-mem='free -hlmt'
alias sh-cpu='lscpu'
alias sh-blk="lsblk -S ; lsblk -f"
alias sh-temp='head -n 1 /sys/class/thermal/thermal_zone0/temp | xargs -I{} awk "BEGIN {printf \"%.2f\n\", {}/1000}"'
#
# Easy access to std commands
alias ff='find . -type f -iname'
alias ping="ping -c10 -i.2"
EOF
```

### #Set command defaults and navigation
```
sudo tee /etc/profile.d/defaults.sh << EOF
# Comand defaults
alias df='df -Hl'
alias du='du -hd1'
alias h="history | cut -c 8-"
alias ping='ping -c 5'
alias wget='wget -c'
# Navigating the system
alias ~='cd ~'
alias ..='cd ..'
alias ll='ls -lhas'
alias profile='echo \"load profile ...\" ; for file in  /etc/profile.d/*.sh; do source \${file}; done'
alias ,='echo \"load profile ...\" ; for file in  /etc/profile.d/*.sh; do source \${file}; done'
EOF
```
### finally load the alias:
for file in  /etc/profile.d/*.sh; do source ${file}; done
