# user/bin/env python3
# -*- coding:utf-8 -*-
import requests
import re
import os

def getNetResquest(url):
    headers = {
        'Host': 'wx.qq.com',
        'Origin': 'https://wx.qq.com',
        'Referer': 'https://wx.qq.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, sdch, br',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive'
    }
    f = requests.get(url, headers=headers)
    data = f.content
    return data

class Spider:
    #页面初始化
    def __init__(self):
        self.siteURL = 'https://wx.qq.com/'
    def getUrl(self, num):
        url = 'https://tuchong.com/%s/albums' % (num,)
        return url
    def test(self):
        result = getNetResquest(self.siteURL).decode('utf-8')
        pattern = re.compile('<div class="qrcode".*?src="(.*?)"', re.S)
        item = re.findall(pattern, result)
        print(item)
        print(result)

spider = Spider()
spider.test()
