When I first started testing Tiddlywiki in summer, I found out a lot about the new version which I could use to have a better experience.

This document may serve as a starting point for anyone who wants to easily setup a low maintenance wiki. I tried to experiment with other wiki systems available under Linux, but setting up a whole LAMP server for using a wiki locally seemed like an overkill (and it is as I'm so lazy to do such things).

Now Tiddlywiki as a javascript powered application has some downsides and I admit that I was a bit sceptical at first: Your browser will not save data in it easily and your data will be bundled inside an HTML file which is cool but creates a bit of insecurity. You know, there's a chance that things will go south and the file gets corrupted. Needless to say you need to backup the whole wiki frequently.

### Nodejs to the rescue
After researching a bit, I found out that there is a tiddlywiki version for nodejs. Nodejs acts like a server building your wiki from text files. It's like a static blog engine. You run it in the background and visit a localhost page in your browser. New you can save easily and even work directly with your text files from a normal text editor. Even if corruption hits your wiki, your files are seperated from it.

[Here are the instructions I've used to set this up into my Linux system](https://tiddlywiki.com/#Installing%20TiddlyWiki%20on%20Node.js)

After setting it up, I created a new wiki 
```
tiddlywiki ~/Documents/mynewwiki --init server
``` 
and run the command to start the server 
```
tiddlywiki ~/Documents/mynewwiki --listen
```
That's all! Visiting http://127.0.0.1:8080/ in my browser loads my wiki ready to be edited.

I Backup the whole wiki to a single html file using this
```
tiddlywiki ~/Documents/mynewwiki --build index
```
I use this command to keep daily backups of my wiki and sync one of the into my phone. Of course I use a non editable copy to have my information into my mobile. To edit on the mobile phone, termux for android supports the whole nodejs setup. I have tried it and reporting that it works just fine. So it is another nice option.


### Plugins
Tiddlywiki is great as it is, but there are so many quality plugins available to customize the whole thing to your needs. It's just good to know what you need and don't get drown in a sea of possibilities like this [full catalog of plugins and solutions](https://dynalist.io/d/zUP-nIWu2FFoXH-oM7L7d9DM).

I use the following:
* [Stroll](https://giffmex.org/stroll/stroll.html)

  Contains a pack of great plugins to make your wiki o lot like roam. Backlinks, extra buttons, double column view and easy links addition are some of its features. Just visit the site and drop the plugins into your wiki.

* [Autolist](https://saqimtiaz.github.io/sq-tw/editor-autolists.html)

  Editing lists in wikitext can be a pain, so I use this to auto create bullet lists

* [Favorites](https://kookma.github.io/TW-Favorites/)

  Gives you the ability to mark tiddlers as favorites. It is quite useful when you have many tiddlers.

* [Commander](https://kookma.github.io/TW-Commander/)

  A really basic plugin if you are serious about your wiki. It gives you the power to do nearly anything you want to multiple tiddlers at once.


### Some video resources I enjoyed
* [Talks with Jeremy Ruston, the creator](https://www.youtube.com/c/JeremyRuston/videos)
* [Anne Laure (Ness Labs) tips](https://www.youtube.com/watch?v=vuU3MrxdKcU)
* [An opinionated approach to Vault:TiddlyWiki](https://lesser.occult.institute/an-opinionated-approach-to-tiddlywiki)
