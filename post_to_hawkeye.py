#!/usr/bin/env python
#-*- coding:UTF-8 -*-

import requests
import base64
import json
import os

url='http://10.32.47.4:10020/face_camera'
headers = {'Accept':'application/json','Content-Type':'application/json'}

filesPath = "yj\\"
total_image = os.listdir(filesPath)
count = 0
scount = 0
print(len(total_image))

for imagefile in total_image:
	fullPath = os.path.join(filesPath, imagefile)
	f=open(fullPath, "rb")
	img=f.read()
	base64_data=base64.b64encode(img).decode('utf-8')
	f.close()
	test={"time":1515151515,'cid':'290200001474','image':base64_data,'faces':[base64_data]}
	r = requests.post(url, json=test,headers=headers)
	count += 1
	if r.status_code != 200:
		print(imagefile)
	else:
		scount += 1
print(count)
print("success:",scount)