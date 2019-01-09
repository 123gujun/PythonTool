#!/usr/bin/env python
#-*- coding:UTF-8 -*-

import grequests
import base64
import json
import datetime,os



def getFiles(filesPath):
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




def Parallel(url,filesPath,headers,filenames):
    tasks = []
    for file in filenames:
        filestr = GetFileStr(filesPath + file)
        test ={"time":1516002690,'cid':'290200001263', 'image':filestr, 'faces':[filestr]}
        res = grequests.post(url,json=test,headers=headers)
        #rs = grequests.map(res)
        tasks.append(res)
    grequests.map(tasks,size=300)



