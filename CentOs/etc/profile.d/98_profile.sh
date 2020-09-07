# Custom (login) shell config; settings may be overridden by a user individual .bashrc

PS1rootuser="$( test `whoami` == root && echo '\[\e[31m\]' )\u\[\e[0m\]"
PS1user="$( test `whoami` != root && echo '\[\e[32m\]' )\u\[\e[0m\]"
PS1colorRoot='\[\e[1;37;32m\]' # color of working directory
PS1color='\[\e[1;37;31m\]' # color of working directory

HISTTIMEFORMAT='%F %T %Z '

ID=`id | cut -f 2 -d "(" | cut -f 1 -d ")" `
export ID HISTTIMEFORMAT

# sort out shell
if test -f /proc/mounts ; then
  if ! is=$(readlink /proc/$$/exe 2>/dev/null) ; then
    case "$0" in
    *pcksh)     is=ksh  ;;
    *)          is=sh   ;;
    esac
  fi

  case "$is" in
    */bash)     is=bash
        case "$0" in
        sh|-sh|*/sh)
                is=sh   ;;
        esac            ;;
    */ash)      is=ash  ;;
    */dash)     is=ash  ;;
    */ksh)      is=ksh  ;;
    */ksh93)    is=ksh  ;;
    */pdksh)    is=ksh  ;;
    */*pcksh)   is=ksh  ;;
    */zsh)      is=zsh  ;;
    */*)        is=sh   ;;
  esac
else
 is=sh
fi

case "$is" in
    bash)
        if [ ${ID} == "root" ]; then
            export PS1="$PS1rootuser@\h:$PS1colorRoot\w\[\e[0m\]# "
            tty | grep pts > /dev/null && PS1="$PS1\[\e]0;\w - \u@\h\a\]";
        else
            export PS1="$PS1user@\h:$PS1color\w\[\e[0m\]> "
            tty | grep pts > /dev/null && PS1="$PS1\[\e]0;\w - \u@\h\a\]";
        fi
        shopt -s histappend
        ;;
esac
