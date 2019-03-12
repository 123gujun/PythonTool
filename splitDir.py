# coding=utf-8
import os
import shutil

filesPath = u"D:\\WorkSpace\\1w\\"

def  getFiles(filesPath):
    '''获取2k文件'''
    fullPath = []
    for imagePath in os.listdir(filesPath):
        if imagePath.split(".")[1]=="jpg" or imagePath.split(".")[1]=="png":
            print(len(fullPath))
            if len(fullPath) < 1000:
                fullPath.append(imagePath)

    return fullPath

files = getFiles(filesPath)

print (len(files))
filecount =0
pathcount = 1


path = filesPath + "image" + str(pathcount)
os.mkdir(path)
for file in files:
    if filecount < 1000:
        shutil.copy(filesPath + file,path)
        filecount += 1
    else:
        if pathcount > 1:
            break
        else:
            pathcount += 1
            path = filesPath + "image" + str(pathcount)
            os.mkdir(path)
            filecount = 1



