# Custom profile modifications for MSOAR
umask 022

alias ls='ls --color=auto'
alias l='ls -alhF'
alias la='ls -lah'
alias ll='ls -lh'

alias md='mkdir -p'
alias rd='rmdir'

alias egrep='egrep --color=auto'
alias fgrep='fgrep --color=auto'
alias grep='grep --color=auto'

alias -- +='pushd .'
alias -- -='popd'

alias ..='cd ..'
alias ...='cd ../..'
alias cd..='cd ..'

alias o='less'
alias vlm='less +F /var/log/messages'

alias psa='ps waux'
alias netlist='netstat -an | grep LIST|less'

alias chksv='systemctl status'
alias lssv='systemctl list-unit-files'
alias chklog='journalctl -xn'

alias demisto="sudo su - demisto"
