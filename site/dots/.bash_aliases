alias upd="sudo apt update && sudo apt upgrade && sudo apt autoremove"
alias off="sudo shutdown -h now"
alias v="vim"
alias weather="curl wttr.in/Thessaloniki"
alias ll="ls -al --color=auto"
alias netreset="sudo systemctl restart NetworkManager"
export EDITOR="/usr/bin/vim"
alias ppl="people"
alias em="emacs -nw"
alias fc="python3 ~/Nextcloud/linux_conf/antoblock/ledger.py $1 $2"
alias site="python3 ~/nicksiv.github.io/generate.py"

# Backup
bup() {

zip -re /tmp/zippedFiles/T420.zip ~/Nextcloud/linux_conf/antoblock/ ~/Documents/ ~/nicksiv.github.io/ && rsync -av --delete /tmp/zippedFiles/ /media/antoblock/Cruizer/T420/
    
    }

# Radio player
radio() {
  echo '============='
  echo 'PLAYING RADIO'
  echo '============='
  echo 'use < and > for previous/next station, p for pause, q for quit'
  mpv ~/Nextcloud/linux_conf/antoblock/radio.md
}

# People (glossary finder)
people() {
   dbfile=~/Nextcloud/inbox/people.rec
   case "$1" in
	   help) echo "enter name of entry to find"
		 echo "edit:     edit db file"
		   ;;

	   all) recsel -C -P Name $dbfile
		   ;;

	   edit) vim $dbfile
		   ;;
	   *) recsel -ie "Name ~ '$1'" $dbfile
		   ;;
   esac

    }

# Keepass utility
pass() {
   passfile=~/Nextcloud/accounts.kdbx
   case "$1" in
           open) keepassxc-cli open $passfile
	     ;;
	   view) keepassxc-cli show -s $passfile "$2"
		   ;;
	   search) keepassxc-cli search $passfile "$2"
		   ;;
	   copy) keepassxc-cli clip -b $passfile "$2" 15
		   ;;
	   ls) keepassxc-cli ls $passfile | more
		   ;;
	   *) echo "view     : View a known pass"
	      echo "search   : Search for passes"
	      echo "copy     : Copy a specific pass"
	      echo "ls       : list all entries"
		   ;;
   esac

}

[ ! -t 0 ] && xset b off

