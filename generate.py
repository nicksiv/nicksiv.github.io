# generate pages script
# Aug 2024

import os
os.system("")
import datetime,time
import sys
import subprocess
import webbrowser
import glob
import shutil
from random import random, randint 
from datetime import date
import re
username=os.getlogin()
srcFolder="/home/"+username+"/nicksiv.github.io/src/"
destFolder="/home/"+username+"/nicksiv.github.io/"

list_of_files = sorted( filter( lambda x: os.path.isfile(os.path.join(srcFolder, x)), os.listdir(srcFolder) ),reverse=False )
head=os.path.join(srcFolder,"header.html")
foot=os.path.join(srcFolder,"footer.html")
pages="<h2>Page List (site index)</h2><ul>"

for filename in list_of_files:
    if filename!="header.html" and filename!="footer.html":
        f=os.path.join(srcFolder,filename)
        d=os.path.join(destFolder,filename)
        pages+="<li><a href="+filename+">"+filename+"</a></li>"
        os.system("cat "+ head + " > " + d)
        os.system("cat "+ f + " >> " + d)
        os.system("cat "+ foot + " >> " + d)

# Build index
pages+="</ul>"

tmp="/tmp/tmp.html"
with open(tmp, "w") as myfile:
    myfile.write(pages.replace("<^G>",""))
    myfile.close()

d=os.path.join(destFolder,"pagelist.html")
os.system("cat "+ head + " > " + d)
os.system("cat "+ tmp + " >> " + d)
os.system("cat "+ foot + " >> " + d)

print("site updated!")
