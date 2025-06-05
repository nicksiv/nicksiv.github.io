nyk0-nomikon - Wikis

## Wikis

Information on different wiki systems installation

### 1. DocuWiki

<https://www.dokuwiki.org/dokuwiki>

In linux, download dokuwiki and extract into a folder (eg: Documents)

except php which is by default installed in linux, you need to install this:

`sudo apt install xml-php`

To run with the simple php server:

    php -S 127.0.0.1:8080 -t ~/Documents/dokuwiki/

### 2. The federated wiki

<https://fed.wiki.org>

Really interesting simple engine. If setup on-line it can be networked with others.

       - npm install -g wiki
       - launch with wiki command, files location ~/.wiki
       - site on: localhost:3000

### 3. MediaWiki

Installation guides

-   [Requirements](https://www.mediawiki.org/wiki/Manual:Installation_requirements)
-   [Installing on\
    XAMPP](https://www.mediawiki.org/wiki/Manual:Installing_MediaWiki_on_XAMPP)

**Using XAMPP**

-   [Get mediaWiki](https://www.mediawiki.org/wiki/Download)

-   [Get XAMPP for\
    Windows/Linux](https://www.apachefriends.org/download.html)

-   Unzip into `/opt/lampp/htdocs`

-   Change folder access to group:RW others:R

        sudo /opt/lampp/lampp start
        sudo /opt/lampp/lampp stop

**Ownership of mediawiki folder**

The owner might be root or user but the group should be daemon so that\
apache can have write access

    sudo chown -R nick:daemon /opt/lampp/htdocs/mediawiki

**Export data into xml file**

For this to work you need packages \`php-mysql php-mbstring php-intl\`

    cd /opt/lampp/htdocs/wiki/maintenance
    php dumpBackup.php --full --quiet > ~/Documents/wm-dump.xml

**Import data**

    cd /opt/lampp/htdocs/wiki/maintenance
    php importDump.php < ~/Documents/wm-dump.xml

Resources

[River Writes - A MediaWiki Blog](https://river.me/)
