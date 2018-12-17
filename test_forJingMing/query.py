# coding=utf-8
import requests
import os
import datetime
import threading
import base64


url = "http://192.168.1.188:88/verify/face/search"
purl='http://192.168.10.240:10020/face_camera'

querystring = {"dbName":"test1234","topNum":10,"score":0.5}
filesPath20w = "C:\\WorkSpace\\20W\\"
filesPath1w  = "C:\\WorkSpace\\1w\\"
filesPath2k = "C:\\WorkSpace\\2k\\"

pathArray = [u"D:\\迅雷下载\\living_photo(1)\\",u"D:\\WorkSpace\\1w\\",u"C:\\WorkSpace\\20W\\"]

def query(filesPath):

    print("传递进来了%s\n" % filesPath)
    for imagePath in os.listdir(filesPath):
        if imagePath.split(".")[1]=="jpg" or imagePath.split(".")[1]=="png":
            fullPath = filesPath + imagePath
            files = {
                "imageData": open(fullPath,'rb')
            }
            headers = {
                "cache-control": "no-cache",
                "Postman-Token": "dd1495cf-cee1-4479-b930-85cba2bcba8b"
                }
            response = requests.request("POST", url, files=files, headers=headers, params=querystring)
            print(response.text)



#实际查询的模块
def mulitThread_Query(filespath,imagepath,threadIndex,gap,mode):

    start = threadIndex * gap
    end =  (threadIndex + 1) * gap

    successCount  = 0
    failCount = 0
    #filename = str(threadIndex) + "thread.txt"

    if threadIndex  == 200 - 1:
        end = end + mode

    filename = 'thread%d.txt' % threadIndex


    for  index  in range(start,end):
        fullpath = filespath + imagepath[index]
        #print(fullpath)
        '''
        files = {
            "imageData": open(fullpath, 'rb')
        }
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
        response = requests.request("POST", purl, files=files, headers=headers, params=querystring)
        '''
        f = open(fullpath, "rb")
        img = f.read()
        base64_data = base64.b64encode(img).decode('utf-8')
        f.close()
        test = {"time": 1516002690, 'cid': '290200001263', 'image': base64_data, 'faces': [base64_data]}
        response = requests.post(purl, json=test, headers=headers)
        # print(r.text)
        print(response.status_code)
        print(response.text)
        if response.status_code == requests.codes.ok:
            successCount = successCount + 1
        else:
            failCount = failCount + 1
#2k张

headers = {'Accept':'application/json','Content-Type':'application/json'}
purl='http://192.168.10.240:10020/face_camera'
def post_sailan(imagePaths):
    for imagefile in imagePaths:
        f = open(imagefile, "rb")
        img = f.read()
        base64_data = base64.b64encode(img).decode('utf-8')
        f.close()
        test = {"time": 1516002690, 'cid': '290200001263', 'image': base64_data, 'faces': [base64_data]}
        r = requests.post(purl, json=test, headers=headers)
        # print(r.text)
        print(r.status_code)

def main(index,pathArray,number):

    imageArray = []
    for  imagepath in os.listdir(pathArray[index]):
        if imagepath.split(".")[1] == "jpg" or imagepath.split(".")[1] == "png":
            imageArray.append(imagepath)
    gap = len(imageArray) / 200

    mode = len(imageArray) % 200
    threads = []
    start = datetime.datetime.now()
    #创建200个线程
    for  i in range(200):
        t = threading.Thread(target=mulitThread_Query,args=(pathArray[index],imageArray,i,gap,mode))
        threads.append(t)

    for j in range(200):
         threads[j].start()

    for k in range(200):
        threads[k].join()

    end = datetime.datetime.now()

    with open("res.txt", "a+") as fp:
        fp.write("*" * 50)
        fp.write("查询了%d张图片" % number)
        fp.write("时间=%ds" % (end - start).seconds)
        fp.write("*" * 50)
        fp.write("\n\n")

#1w张

if __name__ == '__main__':
    main(1,pathArray,10000)

#20w张


