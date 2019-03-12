#!/usr/bin/env python
#-*- coding:UTF-8 -*-

# import requests
import base64
import json,time
# import asyncio
# from grequests import async
import grequests
# import wrk

url='http://192.168.1.173:10020/face_camera'
headers = {'Accept':'application/json','Content-Type':'application/json'}
f=open(u"D:\\迅雷下载\\底库-ulsee\\7-杜鹏-男.jpg",'rb')
img=f.read()
base64_data=base64.b64encode(img).decode('utf-8')
f.close()
print(type(base64_data))
test={u"time":1516002690,u"cid":"290300000897",'image':base64_data,'faces':[base64_data]}

filename = "image.txt"
with open(filename,'w') as file_object:
    file_object.write(base64_data)

