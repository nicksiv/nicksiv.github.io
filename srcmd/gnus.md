nyk0-nomikon - Emacs Gnus

## Emacs Gnus

If you live inside emacs, having a simple way to check your email can be\
a life savior. Sometimes when I don\'t have my browser open and working\
inside a buffer, it is so simple to fire up gnus, which I have bound to\
a shortcut for quick access.

Making gnus to work under Gmail is pretty simple. I followed a tutorial\
from [emacswiki](https://www.emacswiki.org/emacs/GnusTutorial) and worked like a charm.

The configuration is split in two parts. The first part goes into the emacs config (\~/.emacs or init.el).

    (setq gnus-select-method '(nnimap "gmail"
    (nnimap-address "imap.gmail.com"); it could also be imap.googlemail.com if that's your server.
    (nnimap-server-port 993)
    (nnimap-stream ssl)))
    (setq message-send-mail-function 'smtpmail-send-it
    smtpmail-starttls-credentials '(("smtp.gmail.com" 587 nil nil))
    smtpmail-auth-credentials '(("smtp.gmail.com" 587 "your_email@gmail.com" nil))
    smtpmail-default-smtp-server "smtp.gmail.com"
    smtpmail-smtp-server "smtp.gmail.com"
    smtpmail-smtp-service 587
    smtpmail-local-domain "yourdomain")
    (global-set-key [f8] 'gnus)

The last command is my personal keybinding for running gnus.

Secondly, a new file should be created, the `~/.authinfo`, which will\
contain sensitive login info. That\'s why I thought it is better to have\
this encrypted, so I saved it as `~/.authinfo.gpg`. Below is the file\'s\
contents:\
`machine imap.gmail.com login youremail password secret port 993`

Just edit the youremail and secret with your email and password. Now\
everytime you get to open gnus you will be prompted for the encryption\
key which you can save into your keyring.

### Some basic gnus keybindings

-   B-DEL : delete message
-   B-m : Move message to another group
-   GG : Find message on selected group
-   /o : Show all mails in message view
-   Cc Cs RET Cd : Sort newest to olders in message view
-   Cc Cs Ca : Sort by author
-   Cc Cs Cs : Sort by subject
-   g : Refresh (receive new mail)
-   c : catch up with folder (mark all as read)
-   L/l : Show all groups/unread groups
-   Gc : Customize group
-   ! or u : mark msg as important (always show)
