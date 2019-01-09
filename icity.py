#-*- coding:UTF-8 -*-
import GeneralUse as gu
import json
import requests
import datetime

url = "http://10.24.1.188:8888/people/api/add_peoples"
filedir = u"D:\\WorkSpace\\dikuulsee\\dikuulsee\\"

# 主循环

#获取文件，构造发送json结构体，发送


#添加人员api ,测算出添加速度
def  BatchAdd(filedir,url):
    filenames = gu.getFiles(filedir)
    arry = []
    filearray =[]
    for value in filenames:
        fileobject = open(filedir + value, "rb")
        filearray.append(fileobject)
        arry.append(("[]image", (value, fileobject)))
        #arry.append(("[]image",(value,open(filedir + value,"rb"))))
    headers = {'Cookie':'Token="bearer 9de08f26-0637-44e7-9895-0203b7906725"'}
    body = {'flag':(None,'staff')}
   # file = [("[]image",("chenbo.png",open(filedir + "chenbo.png",'rb'))),("[]image",("yuf.jpg",open(filedir + "yuf.jpg",'rb')))]

    print (arry)

    #发送
    res  = requests.request("POST",url,data=body,files=arry,headers=headers)
    print (res.text)

start = datetime.datetime.now()
BatchAdd(filedir,url)
end = datetime.datetime.now()

print ((end - start).seconds)