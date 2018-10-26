import requests
import os
url = "http://192.168.1.124:8088/verify/face/add"

querystring = {"dbName":"djm3"}
filesPath = "D:\\memo\\media\\ulsee\\"
for imagePath in os.listdir(filesPath):
    if imagePath.split(".")[1]=="jpg" or imagePath.split(".")[1]=="png":
        fullPath = filesPath + imagePath
        print(fullPath)
        files = {
            'imageData': open(fullPath, 'rb')
        }
        headers = {
            'Cache-Control': "no-cache",
            'Postman-Token': "75b7c49d-6c6d-43ba-ad19-70f1b84043b2"
            }

        response = requests.request("POST", url, files=files, headers=headers, params=querystring)

        print(response.text)