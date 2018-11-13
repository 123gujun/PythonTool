# coding=utf-8
import requests
import os
url = u"http://192.168.10.240/api/personnels"

querystring = {"group_id": 1}

# 乱码的问题
filesPath = u"D:\\WorkSpace\\dikuulsee\\dikuulsee\\"
for imagePath in os.listdir(filesPath):
    if imagePath.split(".")[1]=="jpg" or imagePath.split(".")[1]=="png":
        fullPath = filesPath + imagePath
        print(fullPath)


        files = {
            'photo': open(fullPath,'rb'),
            'name':(None,imagePath),
            'group_id':(None,1)
        }
        headers = {
            'Cache-Control': "no-cache",
            'Postman-Token': "75b7c49d-6c6d-43ba-ad19-70f1b84043b2"
            }

        response = requests.request("POST", url, files=files, headers=headers)

        print(response.text)