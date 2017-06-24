# user/bin/env python3
# -*- coding:utf-8 -*-
from urllib import request
import re
import os

def getNetResquest(url):
    with request.urlopen(url) as f:
        data = f.read()
        return data

class Spider:
    #页面初始化
    def __init__(self):
        self.siteURL = 'https://tuchong.com/1019261/'
    def getUrl(self, num):
        url = 'https://tuchong.com/%s/albums' % (num,)
        return url
    def test(self):
        num = 3
        result = getNetResquest(self.getUrl(num)).decode('utf-8')
        pattern = re.compile('<a class="albums " href="(.*?)">', re.S)
        items = re.findall(pattern, result)
        for item in items:
            result = getNetResquest(item)
            pattern = re.compile('')


#传入起止页码即可，在此传入了2,10,表示抓取第2到10页的MM
spider = Spider()
spider.test()
