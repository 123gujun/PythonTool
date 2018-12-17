#!/usr/bin/env python
#-*- coding:UTF-8 -*-

import grequests
import base64
import json
import datetime,os


filesPath = u"D:\\WorkSpace\\1w\\"
url = "http://192.168.10.240:10020/face_camera"
headers = {'Accept':'application/json','Content-Type':'application/json'}

def getFiles():
    '''获取文件名集合'''
    fullpath=[]
    for imagePath in os.listdir(filesPath):
        if imagePath.split(".")[1] == "jpg" or imagePath.split(".")[1] == "png":
            fullpath.append(imagePath)
    return fullpath

def GetFileStr(fileName):
    '''获取文件字符串'''
    f = open(fileName, "rb")
    img = f.read()
    base64_data = base64.b64encode(img).decode('utf-8')
    f.close()
    return base64_data

filenames = getFiles()


def Parallel():
    tasks = []
    for file in filenames:
        filestr = GetFileStr(filesPath + file)
        test ={"time":1516002690,'cid':'290200001263', 'image':filestr, 'faces':[filestr]}
        res = grequests.post(url,json=test,headers=headers)
        #rs = grequests.map(res)
        tasks.append(res)
    grequests.map(tasks,size=300)



start = datetime.datetime.now()
Parallel()
end = datetime.datetime.now()


print ((end - start).seconds)