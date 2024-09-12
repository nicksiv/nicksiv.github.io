# Mutt notes and GPG encryption

The whole muttrc file will be setup after running my custom `install` script.
The only thing needed to be generated on a new machine, is the file `~/.mutt/pwd` which contains sensitive info.

## Contents of the password file (pwd)
```
# My credentials
set smtp_url = 'smtps://<Gmail Username>@gmail.com@smtp.gmail.com:465/'
set smtp_pass = '<Password>'
set imap_user = '<Gmail Username>@gmail.com'
set imap_pass = '<Password>'
```
After creation, you need to create a gpg key to encrypt the file into the file `~/.mutt/pwd.gpg`

## Safely store password
* <https://unix.stackexchange.com/questions/20570/mutt-how-to-safely-store-password>

First of all, we need to create a public/private key pair
`gpg --gen-key`
Enter email, name and encryption key

Then, after creating the passwords file, encrypt it:
`gpg -r your.email@example.com -e ~/.mutt/passwords`
A new passwords.gpg will be created. Then we can erase the old unencrypted file:

```
shred ~/.mutt/passwords
rm ~/.mutt/passwords
```
Now into the `~/muttrc` file we need to have this line instead of our credentials:
`source "gpg -d ~/.mutt/passwords.gpg |"`

*(this will not be necessary if you're using the ready made .muttrc from my github repo)*

## Transferring gpg keys
Log in to old user:
`gpg -a --export-secret-keys >myprivatekeys.asc`
Copy myprivatekeys.asc to the new user's computer/folder

From the new user's accounts:
`gpg --import myprivatekeys.asc`
`gpg -K'


## colorscheme
* <https://www.sthu.org/code/codesnippets/mutt-gruvbox.html>

## References
* <https://github.com/nicksiv/dot>
* https://stevelosh.com/blog/2012/10/the-homely-mutt/#s5-why-local-email

    #software #cli #linux
