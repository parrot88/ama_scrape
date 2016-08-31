#from __future__ import unicode_literals
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import urllib2

Site = 'http://oshiete.goo.ne.jp/qa/2190657.html'
#Site = 'http://oshiete.goo.ne.jp/qa/1425849.html'
soup = BeautifulSoup(urllib2.urlopen(Site), "lxml")
from strip_html import strip_tags
ans = ''

# get question tittle
res = soup.find('div',class_="q_article_info clearfix")
ans += strip_tags( str(res.h1) )+"\n"
ans += ("- " * 50)+"\n"

res = soup.find('p',class_="q_text")
ans += strip_tags( str(res) )+"\n"
ans += ("- " * 50)+"\n"

# get answers text
res = soup.findAll('div',class_="a_text")

for one in res:
    ans += strip_tags( str(one) )+"\n"
    ans += ("- " * 50)+"\n"

from rw_file import rw_file
rw = rw_file()
rw.write("dat/result.txt",ans.decode('utf-8'))

print 'Finish'




