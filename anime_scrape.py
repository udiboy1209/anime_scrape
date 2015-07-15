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
totbytes=0
speed=0

def escapeall(url):
    return re.sub("[A-Z\~\!\@\#\$\*\{\}\[\]\-\+\.]",'',url)

def dwbar(a,b,c):
    global updtime, totbytes, speed

    totbytes+=b

    if time.time()-updtime > 0.5:
        speed = (totbytes)/((time.time()-updtime)*1000.0)
        updtime = time.time()
        totbytes=0;

    esttime = ((c-a*b)/1000.0)/speed if speed!=0 else 0
    sys.stdout.write("\rDownload progress: %.2fM of %.2fM - %.2f kB/s - %dm %ds left      " %
                    ((a*b)/1000000.0,c/1000000.0, speed,
                    int(esttime)/60, int(esttime)%60))
    sys.stdout.flush()

def fetch(pageurl):
    global updtime, failed_links

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
        updtime=currtime
        urllib.urlretrieve(vidlink,ani_name+"-episode-%d.mp4" % i, dwbar)
        currtime = time.time()-currtime

        print
        print "Download finished in %dm %ds\n" % (int(currtime)/60, int(currtime)%60)
    except Exception as e:
        print e
        print "Failed : ", pageurl, "\n"
        failed_links+=pageurl+"\n"


args = len(sys.argv)

if args < 2:
    print "Enter Anime Name : ",
    ani_name=raw_input()
else :
    ani_name=sys.argv[1]

if ani_name[:4] == "http":
    fetch(ani_name)
else:
    ani_name=ani_name.title()
    if args < 3:
        print "Enter staring Episode:",
        s=int(raw_input())
    else :
        s=int(sys.argv[2])

    if args < 4:
        print "Enter ending episode:",
        e=int(raw_input())
        print
    else :
        e=int(sys.argv[3])

    print "Dowloading ", ani_name, " from episode ", s, " to ", e
    print

    for i in range(int(s),int(e)+1):
        pageurl="http://anilinkz.tv/"+ani_name.lower().replace(" ","-")+"-episode-%d" % i;
        fetch(pageurl)

print "Failed links :"
print "".join(failed_links)
