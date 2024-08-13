  #!/bin/bash 
  # Installation script
  # Applications
  cd #
  sudo apt install firefox-esr git vim tmux keepassxc curl recutils mpv cmus unzip newsboat nextcloud-desktop tlp tlp-rdw
  # Firefox extensions
  # Decentraleyes, UBlock origin, Ghostery, NoScript

  # Optional
  # sudo apt install cwm picom feh xinput xscreensaver emacs
  # vim plugins
  curl -fLo ~/.vim/autoload/plug.vim --create-dirs https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
  # tmux plugins
  git clone https://github.com/tmux-plugins/tpm ~/.tmux/plugins/tpm
  # fzf
  git clone --depth 1 https://github.com/junegunn/fzf.git ~/.fzf
  ~/.fzf/install
  # configs
  ln -s ~/Nextcloud/linux_conf/antoblock/.vimrc ~/.vimrc
  ln -s ~/Nextcloud/linux_conf/antoblock/.tmux.conf ~/.tmux.conf
  ln -s ~/Nextcloud/linux_conf/antoblock/.bash_aliases ~/.bash_aliases
  ln -s ~/Nextcloud/linux_conf/antoblock/.emacs ~/.emacs
  ln -s ~/Nextcloud/linux_conf/antoblock/rss-urls-newsboat ~/.newsboat/urls
  # bash
  # echo 'source ~/.bash_aliases >> ~/.bashrc'
  # unzip notes
  # unzip ~/org/data/sys/notes-archive.zip -d ~/Documents/notes-archive
  # git
  git config --global user.name "nyk0si"
  git config --global user.email "nicksiv@disroot.org"


