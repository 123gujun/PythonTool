#!/usr/bin/env python
#-*- coding:UTF-8 -*-

import requests
import base64
import json,time


    f=open("D:\\WorkSpace\\1w\\VT001_00000061.jpg",'rb')
img=f.read()
base64_data=base64.b64encode(img).decode('utf-8')
f.close()

with open("image.txt",'w') as file_object:
    file_object.write(base64_data)