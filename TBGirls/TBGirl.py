# user/bin/env python3
# -*- coding:utf-8 -*-
from urllib import request
import re

# get网络请求
def getNetResquest(url):
    with request.urlopen(url) as f:
        data = f.read()
        return data

class Spider:

    def __init__(self):
        self.siteURL = 'http://mm.taobao.com/json/request_top_list.htm'  # 淘宝MM网页的URL
    # 获取该页的网页数据
    def getPage(self, pageIndex):
        url = self.siteURL + "?page=" + str(pageIndex)
        print(url)
        response = getNetResquest(url)
        return response.decode('gbk')
    # 获取第几页的网页MM
    def getContents(self, pageIndex):
        page = self.getPage(pageIndex)  # 获取到网页源码数据
        pattern = re.compile('<div class="list-item".*?pic-word.*?<a href="(.*?)".*?<img src="(.*?)".*?<a class="lady-name.*?>(.*?)</a>.*?<strong>(.*?)</strong>.*?<span>(.*?)</span>', re.S)  # 正则表达式，匹配我们想要的信息这里分别获取到MM的个人主页，头像的链接，姓名，年龄，城市
        items = re.findall(pattern, page)  # 用正则表达式，去匹配网页源码
        for item in items:  # 遍历匹配的结果，并打印出来
            print(item[0], item[1], item[2], item[3], item[4])  # 分别对应MM的个人主页，头像的链接，姓名，年龄，城市

spider = Spider()
spider.getContents(1)
