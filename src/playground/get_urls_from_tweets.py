
import re
import os
import sys


tweetURLdict = {}
for line in open("pmarca_rts_append.txt").readlines():
    results = re.search("(?P<url>https?://t.co/[A-Za-z]{10})", line.strip()) # some urls are malformed so I was only able to extract perfect ones, hence {10}
    if results:
        #print results.group("url")
        tweetURLdict[results.group("url")] = str(line).replace("\xe2\x80\x99","'").replace("\xe2\x80\x98","'").replace("\xe2\x80\x9c", '"').replace("\xe2\x80\x9d",'"').replace("\xe2\x80\x93",'-').replace("\xe2\x80\x94",'--').replace("\xe2\x80\xa6",'...').replace("\xc3\xb6","o").replace("\xf0\x9f\x98\x8a",":)")

target = open('tweetdict.txt','a')
target.write(str(tweetURLdict))
print len(tweetURLdict)

