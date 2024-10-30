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
i=os.path.join(assetFolder,"index.txt")
pages=[]
posts=[]
head=os.path.join(assetFolder,"header.html")
foot=os.path.join(assetFolder,"footer.html")
sitetitle="nyk0-nomikon"
forceUpdate=False


def getChildren(thisPage):
    # scan index for this page's children
    id=getPageID(thisPage)
    childLinks="<ul>"
    lineid=0;
    with open(i, "r") as myfile:
        for line in myfile:
            if str(id)+"\t" in line:
                lineid=line.split("\t")[0]
                if int(lineid)==id:
                    #print("FOUND "+str(id)+" in "+line)
                    line=line.replace("\n","")
                    pg=line.split("\t")
                    desc=getDescription(pg)
                    childLinks+="<li><a href=" + pg[1] + ".html>"+pg[1]+"</a>"
                    if pg[1]!="":
                        childLinks+="<p class='comment'>"+desc
                    
    childLinks+="</ul>"
    return childLinks
    
def getPageID(thisPage):
    # get id of page from index.txt
    curLine=0
    with open(i, "r") as myfile:
        for line in myfile:
            curLine+=1
            if thisPage.upper() in line.upper():
                return curLine
        myfile.close()
    print ("Not Found in index: "+thisPage)
    return 0

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
    shutil.copy(assetFolder+"style.css",destFolder)

def buildGallery():
    # art gallery
    global pages
    global pageindexCount
    aFolder=destFolder+"img/art/"
    d=os.path.join(destFolder,"artgallery.html")
    list_of_files = sorted( filter( lambda x: os.path.isfile(os.path.join(aFolder, x)), os.listdir(aFolder) ),reverse=False )
    gahtml="<style>body{max-width:98%;}</style><title>"+sitetitle+" - Artworks gallery</title><h1>Art gallery</h1><p>A selection of photos and drawings made over the years</p><div>"
    for filename in list_of_files:
        if filename[:5]=="thumb":
            fn=filename.split("-")
            gahtml+="<a href='img/art/art-"+fn[1]+".jpg'><figure style='float:left;width:250px;height:250px;'><img width='220' height='220' loading='lazy' src='img/art/"+filename+"' title='"+fn[2].split(".")[0]+"'><figcaption>"+fn[2].split(".")[0]+"</figcaption></figure></a>"
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

    d=os.path.join(destFolder,"blog.html")
    os.system("cat "+ head + " > " + d)
    os.system("cat "+ tmp + " >> " + d)
    os.system("echo '"+ setModiFooter(foot,d,datetime.datetime.now()) + "' >> " + d)
    pages.append(["blog.html","blog"])

def getDescription(tabs):
    if len(tabs)>2:
        desc=tabs[2]
    else:
        desc=""
    if tabs[1]=="recent":
        desc="Recently modified pages"
    if tabs[1]=="blog":
        desc="All blog entries"

    return desc

def buildPageIndex():
    global pages
    global posts
    tmp="/tmp/tmp.html"
    paghtml="<title>nyk0 - Index</title><h2>Index</h2><ul style='line-height:1.2em;list-style:none;'>"
    pages.sort()
    for page in pages:
        paghtml+="<li><a href="+page[0]+">"+page[1]+"</a></li>"
    paghtml+="</ul>"
    with open(tmp, "w") as myfile:
        myfile.write("<p>There are "+str(len(pages))+" indexed pages<p>&nbsp;<p>"+paghtml)
        myfile.close()

    d=os.path.join(destFolder,"pagelist.html")
    os.system("cat "+ head + " > " + d)
    os.system("cat "+ tmp + " >> " + d)
    os.system("echo '"+ setModiFooter(foot,d,datetime.datetime.now()) + "' >> " + d)

    # ===== Index on index.html ==========
    d=os.path.join(destFolder,"index.html")
    zeroindex="<h3>notes & pages</h3><idx><ul>"
    zlist=[]
    with open(i, "r") as myfile:
        lines = list(line for line in (l for l in myfile) if line)
        for line in lines:
            line=line.replace("\n","")
            tabs=line.split("\t")
            if tabs[0]=="0":
                fn=tabs[1]
                desc=getDescription(tabs)

                        #zeroindex+="<li><a href="+fn+".html>"+fn+"</a></li> "
                zlist.append([fn, desc])
    zlist.sort()
    for item in zlist:
        zeroindex+="<li><a href="+item[0]+".html>"+item[0]+"</a>"
        if item[1]!="":
            zeroindex+="<p class='comment'>"+item[1]
    zeroindex+="</ul></idx>"
    # latest posts
    maxposts=3
    postno=0
    latestindex="<h3>latest thoughts</h3><idx2><ul>"
    for item in posts:
        if postno<maxposts:
            ttl=item[1]
            ttl=ttl[:10]+": "+ttl[11:].replace("-"," ").capitalize()
            latestindex+="<li><a href="+item[0]+">"+ttl+"</a></li>"
            postno+=1
    latestindex+="<li><a href=blog.html>more...</a></ul></idx2>"

    # write index to the homepage
    with open(d, "r") as myfile:
        ind=myfile.read()
        ind=ind.replace("<nyk0index>",zeroindex+latestindex)
        myfile.close()
    with open(d, "w") as myfile:
        myfile.write(ind)
        myfile.close()


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

    d=os.path.join(destFolder,"recent.html")
    os.system("cat "+ head + " > " + d)
    os.system("cat "+ tmp + " >> " + d)
    os.system("echo '"+ setModiFooter(foot,d,datetime.datetime.now()) + "' >> " + d)
    pages.append(["recent.html","recent"])


    
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

            # child pages links
            if filename!="index.html" and not filename.startswith("201") and not filename.startswith("202"):
                childLinks=getChildren(filename.replace(".html",""))
                os.system("echo '"+childLinks+"' >> " + d)
            #print(setModiFooter(foot,d,srcfiletime))
            os.system("echo '"+ setModiFooter(foot,d,srcfiletime) + "' >> " + d)

    copySiteFiles()
    buildGallery()
    buildPostIndex()
    buildRecent()
    buildPageIndex()

    print("site updated!")
    if forceUpdate==True:
        print("forced full update")

if len(args)>1:
    if args[1]=="publish":
        publish()
    if args[1]=="full":
        forceUpdate=True
        publish()
