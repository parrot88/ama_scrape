# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup

def fix_href(code):
    #href内のリンクをaタグ全てと置換
    soup = BeautifulSoup(code,"lxml")
    res = soup.select('a[href^="http"]')
    for one in res:
        key = one
        href = one.get('href')
        code = code.replace(str(key),str(href))
    return code

