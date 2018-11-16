# coding=utf-8
import os
import chardet

filesPath = u"D:\\WorkSpace\\dikuulsee\\dikuulsee\\"
#print(chardet.detect(filesPath))
for imagePath in os.listdir(filesPath):
    if imagePath.split(".")[1]=="jpg" or imagePath.split(".")[1]=="png":
        fullPath = filesPath + imagePath
        #print(chardet.detect(fullPath))
        #print(fullPath.decode('ISO-8859-9'))
        print(fullPath)