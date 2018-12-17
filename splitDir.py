# coding=utf-8
import os
import shutil

filesPath = u"D:\\WorkSpace\\1w\\"
def  getFiles(filesPath):
    '''获取5000文件'''
    fullPath = []
    for imagePath in os.listdir(filesPath):
        if imagePath.split(".")[1]=="jpg" or imagePath.split(".")[1]=="png":
            print(len(fullPath))
            if len(fullPath) < 10000:
                fullPath.append(filesPath + imagePath)
            else:
                return fullPath

files = getFiles(filesPath)

filecount =0
pathcount = 1

path = filesPath + "image" + str(pathcount)
os.mkdir(path)
for file in files:
    if filecount < 1000:
        shutil.copy(file,path)
        filecount += 1
    else:
        if pathcount >= 10:
            break
        else:
            pathcount += 1
            path = filesPath + "image" + str(pathcount)
            os.mkdir(path)
            filecount = 1



