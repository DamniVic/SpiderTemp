#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from aip import AipFace
Ak = 'TBPtvVXmPoAnSX4ljiTkrpji'
Sk = '2wRiOMvA1yEvY09GRm4v6fSvW9H0Kzcj'
Ai = '9647392'
aipFace = AipFace(Ai, Ak, Sk)
aipFace.setConnectionTimeoutInMillis(2000)
aipFace.setSocketTimeoutInMillis(60000)
options = {
    'max_face_num': 5,
    'face_fields': "age,beauty,expression,faceshape,gender,glasses,landmark,race,qualities"
}
# 读取图片
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()
path = 'F:\\KwDownload\\3.jpg'
response = aipFace.detect(get_file_content(path), options)
print(response)
