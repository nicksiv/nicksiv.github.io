nyk0-nomikon - Set default user on Debian's logon screen (LightDM)

## Set default user on Debian's logon screen (LightDM)

After setting up Debian, and for a week, I needed to enter my user name and my password to log on to my system. This is the default behavior of LightDM (the login manager of Debian) for maximum security.

As I got tired to enter my user name again and again, I researched for a way to have LightDM fill the last entered user name for me. As it turns out it is easy to setup.

All you have to do is edit the following file:

    /usr/share/lightdm/lightdm.conf.d/01\_debian.conf

By typing in your terminal:

    sudo nano /usr/share/lightdm/lightdm.conf.d/01\_debian.conf

Then change the command greeter-hide-users from false to true.

     greeter-hide-users=true
     

Save the file (Ctrl+O) and exit (Ctrl+X)

Log out and you have fixed it.
