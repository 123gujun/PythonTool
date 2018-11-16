
# coding=utf-8
import requests
import os



# 基类对象

class Base():
    """基类"""
    def __init__(self,filepath,addr,group_id):
        self.filepath  = filepath
        self.addr = addr
        self.group_id = group_id

    def  GetFile(self):
        fileName = []
        for image in os.listdir(self.filepath):
            if image.split(".")[1] == "jpg" or image.split(".")[1] == "png":
                fileName.append(image)
        return  fileName

#上传


class Upload(Base):
    """上传类"""
    def __init__(self,filepah,addr,group_id):
        super.__init__(filepah,addr,group_id)

    def upload(self):
        fileName = self.GetFile()
        for image in fileName:
            fullpath = self.filepath + image
            files = {"photo": open(fullpath,'rb'),"name": (None,image),"group_id": (None,self.group_id) }
            response = requests.request("POST", self.addr, files=files)


#查询

class Query(Base):

    def __init__(self,filepath,addr,group_id,querystring):
        super.__init__(filepath,addr,group_id)
        self.querystring =  querystring
    def query(self):
        pass


