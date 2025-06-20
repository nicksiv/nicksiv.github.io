# generate pages script
# Aug 2024

import os
import shutil
import datetime,time
import sys
import glob
args=sys.argv

username=os.getlogin()
rootFolder="/home/"+username+"/nicksiv.github.io/"
srcFolder=rootFolder+"src/"
assetFolder=rootFolder+"assets/"
destFolder=rootFolder+"site/"
pages=[]
posts=[]
head=os.path.join(assetFolder,"header.html")
foot=os.path.join(assetFolder,"footer.html")
sitetitle="nyk0-nomikon"
forceUpdate=False



def setModiFooter(footer,dfile,dfiletime):
    # update footer with modified date

    # edit link for github
    # os.system("echo '<p>&nbsp;<p><em><a href=https://github.com/nicksiv/nicksiv.github.io/edit/main/site/"+filename+">Edit</a></em>' >> " + d)
    with open(footer, "r") as myfile:
        ind = myfile.read()
        ind = ind.replace("$nyk0modi", "last update: "+dfiletime.strftime("%Y-%m-%d %H:%M"))
        myfile.close()
    return ind;

def copySiteFiles():
    # Copy files for public
    print("css")
    shutil.copy(assetFolder+"style.css",destFolder)

def buildGallery():
    # art gallery
    global pages
    global pageindexCount
    aFolder=rootFolder+"img/art/"
    d=os.path.join(destFolder,"artgallery.html")
    list_of_files = sorted( filter( lambda x: os.path.isfile(os.path.join(aFolder, x)), os.listdir(aFolder) ),reverse=False )
    gahtml="<style>body{max-width:98%;}</style><title>"+sitetitle+" - Artworks gallery</title><h1>Art gallery</h1><p>A selection of photos and drawings made over the years</p><div>"
    for filename in list_of_files:
        if filename[:5]=="thumb":
            fn=filename.split("-")
            gahtml+="<a href='../img/art/art-"+fn[1]+".jpg'><figure style='float:left;width:250px;height:250px;'><img width='220' height='220' loading='lazy' src='../img/art/"+filename+"' title='"+fn[2].split(".")[0]+"'><figcaption>"+fn[2].split(".")[0]+"</figcaption></figure></a>"
    gahtml+="</div>"
    tmp="/tmp/tmp.html"
    with open(tmp, "w") as myfile:
        myfile.write(gahtml)
        myfile.close()

    os.system("cat "+ head + " > " + d)
    os.system("cat "+ tmp + " >> " + d)
    # os.system("cat "+ foot + " >> " + d)
    #os.system("echo '"+ setModiFooter(foot,d,datetime.datetime.now()) + "' >> " + d)

    pages.append(["artgallery.html","artgallery"])

def buildPostIndex():
    global posts
    tmp="/tmp/tmp.html"
    paghtml="<title>"+sitetitle+" - Blog</title><h2>Blog</h2><ul style='line-height:1.2em;list-style:none;'>"
    posts.sort(reverse=True)
    for page in posts:
        ttl=page[1]
        ttl=ttl[:10]+": "+ttl[11:].replace("-"," ").capitalize()
        paghtml+="<li><a href="+page[0]+">"+ttl+"</a></li>"
    paghtml+="</ul>"
    with open(tmp, "w") as myfile:
        myfile.write("<p>There are "+str(len(posts))+" indexed posts<p>&nbsp;<p>"+paghtml)
        myfile.close()

    d=os.path.join(destFolder,"index-blog.html")
    os.system("cat "+ head + " > " + d)
    os.system("cat "+ tmp + " >> " + d)
    os.system("echo '"+ setModiFooter(foot,d,datetime.datetime.now()) + "' >> " + d)
    pages.append(["index-blog.html","blog"])

def buildPageIndex():
    global pages
    global posts
    tmp="/tmp/tmp.html"
    paghtml="<title>"+sitetitle+" - Index</title><h2>Index</h2><ul style='line-height:1.2em;list-style:none;'>"
    pages.sort()
    for page in pages:
        paghtml+="<li><a href="+page[0]+">"+page[1]+"</a></li>"
    paghtml+="</ul>"
    with open(tmp, "w") as myfile:
        myfile.write("<p>There are "+str(len(pages))+" indexed pages<p>&nbsp;<p>"+paghtml)
        myfile.close()

    d=os.path.join(destFolder,"index-pages.html")
    os.system("cat "+ head + " > " + d)
    os.system("cat "+ tmp + " >> " + d)
    os.system("echo '"+ setModiFooter(foot,d,datetime.datetime.now()) + "' >> " + d)

    d=os.path.join(destFolder,"index.html")

def buildRecent():
    #recent pages
    tmp="/tmp/tmp.html"
    maxpages=30
    thispage=0
    recentList="<title>"+sitetitle+" - Recent changes</title><h2>Recent changes</h2><ul style='line-height:1.2em;list-style:none;'>"

    list_of_files = filter( os.path.isfile, glob.glob(srcFolder + '*') )
    # Sort list of files based on last modification time in ascending order
    list_of_files = sorted( list_of_files, key = os.path.getmtime, reverse=True)
    for file_path in list_of_files:
        timestamp_str = time.strftime(  '%Y-%m-%d', time.localtime(os.path.getmtime(file_path)))
        fnn=os.path.basename(file_path)
        recentList+="<li>"+timestamp_str+"&nbsp;-&nbsp;<a href='"+fnn+"'>"+fnn.split(".")[0]+"</a>"
        thispage+=1
        if thispage>maxpages:
            break;
    recentList+="</ul>"

    with open(tmp, "w") as myfile:
        myfile.write(recentList)
        myfile.close()

    d=os.path.join(destFolder,"index-recent.html")
    os.system("cat "+ head + " > " + d)
    os.system("cat "+ tmp + " >> " + d)
    os.system("echo '"+ setModiFooter(foot,d,datetime.datetime.now()) + "' >> " + d)
    pages.append(["index-recent.html","recent"])

def publish():
    # ============== Main routine start ==================================
    list_of_files = sorted( filter( lambda x: os.path.isfile(os.path.join(srcFolder, x)), os.listdir(srcFolder) ),reverse=False )

    global pages
    global posts
    global pageindexCount
    global forceUpdate
    global head
    global foot

    for filename in list_of_files:
        f=os.path.join(srcFolder,filename)
        d=os.path.join(destFolder,filename)
        if filename!="index.html":
            if filename.startswith("201") or filename.startswith("202"):
                posts.append([filename,filename.replace(".html","")])
            else:
                pages.append([filename,filename.replace(".html","")])

        srcfiletime = datetime.datetime.fromtimestamp(os.stat(f).st_mtime)
        if os.path.isfile(d):
            dstfiletime = datetime.datetime.fromtimestamp(os.stat(d).st_mtime)
        else:
            dstfiletime = datetime.datetime.now()

        if srcfiletime>dstfiletime or forceUpdate==True:
            #create page only if it has been changed after previous export
            os.system("cat "+ head + " > " + d)
            os.system("cat "+ f + " >> " + d)
            os.system("echo '"+ setModiFooter(foot,d,srcfiletime) + "' >> " + d)

    copySiteFiles()

    buildGallery()
#    buildVault()
    buildPostIndex()
    buildRecent()
    buildPageIndex()
#    buildRSS()
    
    print("site updated!")
    if forceUpdate==True:
        print("forced full update")

if len(args)>1:
    if args[1]=="publish":
        publish()
    if args[1]=="full":
        forceUpdate=True
        publish()
