#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by DAMNICOMNIPLUSVIC on 2017/8/12.
# * (c) 2017 DAMNICOMNIPLUSVIC Inc,All Rights Reserved.
import os

import sys
import traceback
from time import sleep

import requests
from selenium import webdriver

CURRENTPATH = os.path.split(os.path.realpath(sys.argv[0]))[0]  # 获取该文件的绝对路径


# 根据提供的网址下载文件
def downloadImageFile(imgUrl):
    local_filename = imgUrl.split('/')[-1]  # 读取文件的名字
    # local_filename = str(time()).replace('.', '') + '.jpg'
    print("Download Image File=", local_filename)
    r = requests.get(imgUrl, stream=True)  # here we need to set stream = True parameter
    os.makedirs(CURRENTPATH + '\\mzitu', exist_ok=True)  # 创建一个新的文件夹
    with open(CURRENTPATH + '\\mzitu\\' + local_filename, 'wb') as f:
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
        self.driver.get('http://www.mzitu.com')
        # for i in range(100):
        #     print('%sst scroll' % (i,))
        #     self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
        #     sleep(2)
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
