# Platform engineering bash_profile for DEMISTO
#
# Bashrc for demisto some alias refer to the sudoers file for the user demisto
# Source global definitions
if [ -f /etc/bashrc ]; then
    . /etc/bashrc
fi

# systemctl
alias get-timers='systemctl --type timer'
alias get-services="systemctl list-unit-files"
alias get-logs='journalctl -xn'
alias get-pstree='systemctl status'
alias get-ps='ps axfw'

# Maintain Package
alias mkpkg='sudo rpmbuild -bb /opt/demisto/templates/msoar.helper.spec'

# Network
alias get-pi='ip addr show scope global'
alias get-ports='netstat -plte --numeric-ports --numeric-hosts'

# Special Commands
alias now='date +"%T"'
alias nowdate='date +"%d.%m.%Y"'
alias get-df='df -h -txfs -text4 | sort -r -k 5 -i'
alias get-du='du -d1s -h | sort -h'
alias get-free='free -hmlt'
alias get-path='echo -e ${PATH//:/\\n}'

#easy access to standard commands
alias c='clear'
alias ll='ls -lahs'
alias h="history"
alias j='jobs -l'
alias ff='find . -type f -iname'
alias ping="ping -c10 -i.2"

# Demisto
alias dlog="sudo journalctl -u demisto -n 100 -f"
alias dstart="sudo systemctl start demisto"
alias dstop="sudo systemctl stop demisto"
alias dlogbackup="sudo journalctl -n 100 -f -u demisto.backup"

# directory shortcuts
alias set-bin='cd /usr/local/demisto'
alias set-dir="cd /opt/demisto"
alias set-log="cd /var/log/demisto"

# Finally go to the demisto directory
cd /opt/demisto
