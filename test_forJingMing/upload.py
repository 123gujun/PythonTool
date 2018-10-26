# coding=utf-8
import requests
import os
import datetime
import query


url_insert = "http://192.168.1.188:88/verify/face/add"

insertstring = {"dbName": "test1234"}
filesPath2k = "C:\\WorkSpace\\2k\\"
filesPath1w = "C:\\WorkSpace\\1w\\"
filesPath20w = "C:\\WorkSpace\\20W\\"

def insert(filesPath):
    count = 0
    start = datetime.datetime.now()
    for imagePath in os.listdir(filesPath):
        if imagePath.split(".")[1]=="jpg" or imagePath.split(".")[1]=="png":
            fullPath = filesPath + imagePath
            #print(fullPath)
            files = {
                "imageData": open(fullPath,'rb')
            }
            headers = {
                'Cache-Control': "no-cache",
                'Postman-Token': "75b7c49d-6c6d-43ba-ad19-70f1b84043b2"
                }
            response = requests.request("POST", url_insert, files=files, headers=headers, params=insertstring)
            count = count + 1
            print(response.text)
    end = datetime.datetime.now()
    with open("res.txt","a+") as fp:
        fp.write("*"*50)
        fp.write("插入了%d张图片" % count)
        fp.write("时间=%ds" % (end - start).seconds)
        fp.write("*" * 50)
        fp.write("\n\n")

# 插入底库

# insert(filesPath1w)
# insert(filesPath20w)

# 查询底库
query.query(filesPath1w)
#query.query(filesPath20w)
