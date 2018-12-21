#!/usr/bin/env python
#-*- coding:UTF-8 -*-

import requests
import base64
import json

url='http://192.168.1.151:5656/face_camera'
headers = {'Accept':'application/json','Content-Type':'application/json'}

facePath='face.jpg'
imagePath = 'bg.jpg'


f=open(facePath, "rb")
img=f.read()
faceBase64 = base64.b64encode(img).decode('utf-8')
f.close()

f=open(imagePath, "rb")
img=f.read()
bgBase64 = base64.b64encode(img).decode('utf-8')
f.close()

body={
		"function" : "FR",
		"data" : {
			"alertType" : "target",
			"dateTime" : "2018-12-19 16:53:21",
			"camera" : {
				"id" : "10086",
				"name" : "CAM01"
			},
			"person" : {
				"id" : "365054f5ba7e26931516",
				"name" : "Andrew",
				"face" : faceBase64,
				"image" : bgBase64
			}
		}
	}
	
r = requests.post(url, json=body, headers=headers)
print(r.text)
print(r.status_code)
