# -*- coding: utf-8 -*-
from HTMLParser import HTMLParser

class MLStripper(HTMLParser):

    def __init__(self):
        self.reset()
        # stripしたテキストを保存するバッファー
        self.fed = []

    def handle_data(self, d):
        # 任意のタグの中身のみを追加していく
        self.fed.append(d)

    def get_data(self):
        # バッファーを連結して返す
        return ''.join(self.fed)

    def check_href(self,d):
        #a hrefタグがあるか調査、urlのみに変換する

        return d

def strip_tags(html):
    s = MLStripper()
    html = s.check_href(html)
    s.feed(html)
    return s.get_data()

