#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by DAMNICOMNIPLUSVIC on 2017/7/15.
# * (c) 2017 DAMNICOMNIPLUSVIC Inc,All Rights Reserved.
import os
import re
import traceback
from time import sleep, time

import requests
import sys
from selenium import webdriver

CURRENTPATH = os.path.split(os.path.realpath(sys.argv[0]))[0]  # 获取该文件的绝对路径


# 根据提供的网址下载文件
def downloadImageFile(imgUrl):
    local_filename = imgUrl.split('/')[-1]  # 读取文件的名字
    # local_filename = str(time()).replace('.', '') + '.jpg'
    print("Download Image File=", local_filename)
    r = requests.get(imgUrl, stream=True)  # here we need to set stream = True parameter
    os.makedirs(CURRENTPATH + '\\zhuangbi', exist_ok=True)  # 创建一个新的文件夹
    with open(CURRENTPATH + '\\zhuangbi\\' + local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:  # filter out keep-alive new chunks
                f.write(chunk)
                f.flush()
        f.close()
    return local_filename


class Spider:
    def __init__(self):
        self.driver = webdriver.Chrome()  # 初始化这个类，这里仅仅指明了用哪个浏览器

    def load(self):
        self.driver.get(
            'http://image.baidu.com/search/detail?ct=503316480&z=0&ipn=d&word=%E8%A3%85%E9%80%BC%E8%A1%A8%E6%83%85&step_word=&hs=2&pn=721&spn=0&di=112490514071&pi=0&rn=1&tn=baiduimagedetail&is=0%2C0&istype=0&ie=utf-8&oe=utf-8&in=&cl=2&lm=-1&st=undefined&cs=700045939%2C462386463&os=2137295864%2C298513828&simid=82758647%2C1042444962&adpicid=0&lpn=0&ln=1974&fr=&fmq=1500101529811_R&fm=&ic=undefined&s=undefined&se=&sme=&tab=0&width=undefined&height=undefined&face=undefined&ist=&jit=&cg=&bdtype=0&oriquery=&objurl=http%3A%2F%2Fimg.lenovomm.com%2Fs3%2Fimg%2Fapp%2Fapp-img-lestore%2F6002-2015-10-16103521-1445034921755.jpeg%3FisCompress%3Dtrue%26width%3D342%26height%3D513%26quantity%3D0.8%26rotate%3Dtrue%26dk%3D2&fromurl=ippr_z2C%24qAzdH3FAzdH3Fooo_z%26e3Bsjg5e544_z%26e3Bv54AzdH3Frw1AzdH3Fwrr1jpwtsAzdH3F2w5_z%26e3Bxtw5_z%26e3BzkkqAzdH3Fa&gsm=2d0&rpstart=0&rpnum=0')
        # for i in range(100):
        #     print('%sst scroll' % (i,))
        #     self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
        #     sleep(2)
        while True:
            try:
                image = self.driver.find_element_by_xpath('//*[@id="currentImg"]')
                imageurl = image.get_attribute('src')
                if not str(imageurl).__contains__('bdimg'):
                    print(imageurl)
                    downloadImageFile(imageurl)
                sleep(0.5)
                next = self.driver.find_element_by_class_name('img-next')
                if next is not None:
                    next.click()
            except:
                traceback.print_exc()
                next = self.driver.find_element_by_class_name('img-next')
                if next is not None:
                    next.click()
        self.driver.quit()


if __name__ == '__main__':
    spider = Spider()
    spider.load()
    # downloadImageFile('http://img1.imgtn.bdimg.com/it/u=1327995708,648537931&fm=26&gp=0.jpg')
