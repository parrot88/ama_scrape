# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
#from b4 import BeautifulSoup
import urllib2
#import os, re, urlparse

Site = 'http://oshiete.goo.ne.jp/qa/1425849.html'

soup = BeautifulSoup(urllib2.urlopen(Site), "lxml")

"""
res = soup.select('a[href^="http://"]')
for one in res:
    print one

"""

#from strip_html import MLStripper
from strip_html import strip_tags

# get question tittle
res = soup.find('div',class_="q_article_info clearfix")
#print str(res.h1)
print strip_tags( str(res.h1) )

#from pprint import pprint
#pprint ((res.h1).encode('utf-8'))

print ("- " * 50)

res = soup.find('p',class_="q_text")
print strip_tags( str(res) )
print ("- " * 50)

# get answers text
res = soup.findAll('div',class_="a_text")

for one in res:
    print strip_tags( str(one) )
    print ("- " * 50)

"""
from pprint import pprint
pprint(res)
"""

#print 'Finish'
