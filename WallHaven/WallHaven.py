#!/usr/bin/python3
# -*- coding:utf-8 -*-
import os
import traceback

import requests
import sys
CURRENTPATH = os.path.split(os.path.realpath(sys.argv[0]))[0]  # 获取该文件的绝对路径
# 根据提供的网址下载文件
def downloadImageFile(imgUrl):
    local_filename = imgUrl.split('/')[-1]
    print("Download Image File=", local_filename)
    r = requests.get(imgUrl, stream=True)  # here we need to set stream = True parameter
    os.makedirs(CURRENTPATH+'\\wallpapers', exist_ok=True)
    with open(CURRENTPATH+'\\wallpapers\\'+local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:  # filter out keep-alive new chunks
                f.write(chunk)
                f.flush()
        f.close()
    return local_filename

def main():
    num = 1
    while True:
        try:
            url = geturl(num)
            downloadImageFile(url)
            num = num+1
        except:
            traceback.print_exc()


def geturl(num):
    url = 'https://wallpapers.wallhaven.cc/wallpapers/full/wallhaven-%s.jpg' % (str(num),)
    return url

if __name__ == '__main__':
    main()
