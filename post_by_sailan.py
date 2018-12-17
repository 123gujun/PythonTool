#!/usr/bin/env python
#-*- coding:UTF-8 -*-

import requests
import base64
import json
import datetime

import threading

import os

url='http://192.168.10.240:10020/face_camera'
#url='http://192.168.1.173:10020/face_camera'
headers = {'Accept':'application/json','Content-Type':'application/json'}

'''
imagePaths=[
"/home/oldog/program-devel/ULSee_system/tools/jinming.jpg",
"/home/oldog/program-devel/ULSee_system/tools/algchenbo.jpg",
"/home/oldog/program-devel/ULSee_system/tools/algchenbo438.jpg"
#"/home/oldog/program-devel/ULSee_system/tools/jj.jpg"
]
'''
filesPath = u"D:\\WorkSpace\\1w\\"
def getFiles():
	fullpath=[]
	for imagePath in os.listdir(filesPath):
		if imagePath.split(".")[1] == "jpg" or imagePath.split(".")[1] == "png":
			fullpath.append(filesPath + imagePath)
	return fullpath

imagePaths = getFiles()

start = datetime.datetime.now()

def MutiThread(imagePaths):
	for imagefile in imagePaths:
		f=open(imagefile, "rb")
		img=f.read()
		base64_data=base64.b64encode(img).decode('utf-8')
		f.close()
		test={"time":1516002690,'cid':'290200001263','image':base64_data,'faces':[base64_data]}
		r = requests.post(url, json=test,headers=headers)
		#print(r.text)
		print(r.status_code)

end = datetime.datetime.now()

print ((end - start).seconds)