#!/usr/bin/python3
# -*- coding:utf-8 -*-
import os
import requests
import sys
import time

CURRENTPATH = os.path.split(os.path.realpath(sys.argv[0]))[0]  # 获取该文件的绝对路径

# 向服务器发送Get请求
def getNetResquest(url):
    return requests.get(url).json()

# 向服务器发送Post请求
def postNetRequest(requrl, parms):
    response = requests.post(requrl, data=parms)
    res = response.text
    return res

# 根据提供的网址下载文件
def downloadImageFile(imgUrl):
    local_filename = imgUrl.split('/')[-1]
    local_filename = str(int(time.time()*1000000)) + '.jpg'
    print("Download Image File=", local_filename)
    r = requests.get(imgUrl, stream=True)  # here we need to set stream = True parameter
    os.makedirs(CURRENTPATH+'\\girls', exist_ok=True)
    with open(CURRENTPATH+'\\girls\\'+local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:  # filter out keep-alive new chunks
                f.write(chunk)
                f.flush()
        f.close()
    return local_filename

def main():
    page = 1
    url1 = 'http://gank.io/api/data/%E7%A6%8F%E5%88%A9/10/'
    url = 'http://gank.io/api/data/%E7%A6%8F%E5%88%A9/10/1'
    finish = False

    while not finish:
        response = getNetResquest(url)
        print(type(response), response)
        if response['error'] == True:
            break
        results = response['results']
        if len(results) == 0:
            break
        for result in results:
            downloadImageFile(result['url'])
        page = page+1
        url = url1+str(page)

if __name__ == '__main__':
    main()
