#!/usr/bin/env python

import urllib
import urllib2
import re
import time
import sys
from bs4 import BeautifulSoup

opener = urllib2.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11')]
failed_links=[]

def escapeall(url):
    return re.sub("[A-Z\~\!\@\#\$\*\{\}\[\]\-\+\.]",'',url)

def dwbar(a,b,c):
    global currtime

    speed = (a*b)/((time.time()-currtime)*1000.0)
    esttime = ((c-a*b)/1000.0)/speed if speed!=0 else 0
    sys.stdout.write("\rDownload progress: %.2fM of %.2fM - %.2f kB/s - %dm %ds left      " %
                    ((a*b)/1000000.0,c/1000000.0, speed,
                    int(esttime)/60, int(esttime)%60))
    sys.stdout.flush()

print "Enter Anime Name : ",
ani_name=raw_input();

print "Staring Episode:",
s=int(raw_input())
print "Ending Episode:",
e=int(raw_input())

for i in range(s,e+1):
    global currtime
    pageurl="http://anilinkz.tv/"+ani_name.lower().replace(" ","-")+"-episode-%d" % i;

    try:
        print "Loading page:",pageurl

        handle = opener.open(pageurl)
        html = handle.read()

        player = BeautifulSoup(html).find("div", {"id":"player"});

        encoded = player.find_all('script')[1].text[35:-5].encode('ascii')
        decoded = urllib2.unquote(escapeall(encoded)).encode('ascii')
        playlink = BeautifulSoup(decoded).find('iframe')['src']

        print "Loading player:", playlink

        handle = opener.open(playlink)
        html = handle.read()

        vidlink = BeautifulSoup(html).find('video').find('source')['src']
        print "Downloading: ", vidlink
        print

        currtime = time.time()
        urllib.urlretrieve(vidlink,ani_name+"-episode-%d.mp4" % i, dwbar)
        currtime = time.time()-currtime

        print
        print "Download finished in %dm %ds" % (int(currtime)/60, int(currtime)%60)
    except Exception:
        print "\n\nFailed : ", pageurl
        failed_links+=pageurl

print "Failed links :"
print "\n".join(failed_links)
