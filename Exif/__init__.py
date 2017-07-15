# user/bin/env python3
# -*- coding:utf-8 -*-
import threading
from time import sleep

import exifread

def getExif(filename):
    fd = open(filename, 'rb')
    tags = exifread.process_file(fd, strict=True)
    fd.close()
    print(filename)
    print(tags)
    for key in tags.keys():
        print(key, ':', tags.get(key))

def sleepprint(num):
    sleep(num)
    print(num)

numbers = [5, 2, 3, 4, 5, 6, 2, 7, 2, 9, 2]
for number in numbers:
    threading.Thread(target=sleepprint, args=(number,)).start()

if __name__ == '__main__':
    filename = 'F:\KwDownload\\12.jpg'
    getExif(filename)
