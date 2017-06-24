# user/bin/env python3
# -*- coding:utf-8 -*-
from urllib import request
import re

def getNetResquest(url):
    with request.urlopen(url) as f:
        data = f.read()
        return data

class Spider:

    def __init__(self):
        self.siteURL = 'http://mm.taobao.com/json/request_top_list.htm'

    def getPage(self, pageIndex):
        url = self.siteURL + "?page=" + str(pageIndex)
        print(url)
        response = getNetResquest(url)
        return response.decode('gbk')

    def getContents(self, pageIndex):
        page = self.getPage(pageIndex)
        pattern = re.compile('<div class="list-item".*?pic-word.*?<a href="(.*?)".*?<img src="(.*?)".*?<a class="lady-name.*?>(.*?)</a>.*?<strong>(.*?)</strong>.*?<span>(.*?)</span>', re.S)
        items = re.findall(pattern, page)
        for item in items:
            print(item[0], item[1], item[2], item[3], item[4])

spider = Spider()
spider.getContents(1)
