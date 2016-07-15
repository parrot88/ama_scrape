# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import urllib2
#import os, re, urlparse

//test
Site = 'https://www.amazon.de/Sieben-Brad-Pitt/dp/B000FTCEAA/'

soup = BeautifulSoup(urllib2.urlopen(Site), "lxml")
#res = soup.find_all("a")
#res = soup.a.get("href")
res = soup.select('a[href^="http://"]')

for one in res:
    print one

#from pprint import pprint
#pprint(txt)
print 'Finish'
