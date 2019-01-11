#-*- coding:UTF-8 -*-
import GeneralUse as gu
import json
import grequests
import datetime
import requests

url = "http://10.24.1.188:8888/people/api/add_peoples"
filedir = u"D:\\WorkSpace\\dikuulsee\\dikuulsee\\"



#添加人员api ,测算出添加速度
def  BatchAdd(filedir,url):
    filenames = gu.getFiles(filedir)
    arry = []
    task = []
    for value in filenames:
        with open(filedir + value,"rb") as fileobject:
            arry.append(("[]image",(value,fileobject)))
    headers = {'Cookie':'Token="bearer 9de08f26-0637-44e7-9895-0203b7906725"'}
    body = {'flag':(None,'staff')}
   # file = [("[]image",("chenbo.png",open(filedir + "chenbo.png",'rb'))),("[]image",("yuf.jpg",open(filedir + "yuf.jpg",'rb')))]
    print (arry)
    res=requests.request("POST",url,data=body,files=arry,headers=headers)
    print (res.text)

'''
start = datetime.datetime.now()
BatchAdd(filedir,url)
end = datetime.datetime.now()
print ((end - start).seconds)
'''


#设备识别记录同步至平台
def sendRecognition():
    '''发送识别记录'''
    url = "http://10.24.1.188:8888/recognition/api/syncrecord"
    headers = {'Cookie': 'Token="bearer 9de08f26-0637-44e7-9895-0203b7906725"'}
    body = {
        'people_id':684,
        'create_at':1547102978000,
        'score':85,
        'sn':'JQ5RQNUUKE',
       # 'image':("zjj.png",open(u"D:\\WorkSpace\\dikuulsee\\dikuulsee\\zjj.png",'rb'))
    }
    files = [("image",("chenbo.png",open(filedir +  "chenbo.png","rb")))]
    for i in range(100):
        res = requests.request("POST",url,data=body,files=files,headers=headers)

'''
    task =[]
    for i in range(1,100):
        res = grequests.post(url,data=body,files=files,headers=headers)
        task.append(res)
    grequests.map(task,size=2)

start = datetime.datetime.now()
sendRecognition()
end = datetime.datetime.now()
print ("*******************************************************")
print ((end - start).seconds)
'''

def  compare():
    '''人脸比对  1：N'''
    url = "http://10.24.1.188:8888/recognition/api/seachface"
    headers = {'Cookie': 'Token="bearer 9de08f26-0637-44e7-9895-0203b7906725"'}
    comparepath = u"D:\\WorkSpace\\2k\\image2\\"
    filearray = gu.getFiles(comparepath)
    task =[]
    for file in filearray:
        res = grequests.post(url,headers=headers,files = [("image",(file,open(comparepath + file,'rb')))])
        task.append(res)
    grequests.map(task,size=2)




start = datetime.datetime.now()
compare()
end = datetime.datetime.now()
print ("*******************************************************")
print ((end - start).seconds)