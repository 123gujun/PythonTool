# coding=utf8
import os
import base64,json

filepath ="C:\\WorkSpace\\2k\\"
filename="lua.json"


def read_file(filepath):
    # TODO  获取文件数据
    imageList = []
    for imagePath in os.listdir(filepath):
        if imagePath.split(".")[1] == "jpg" or imagePath.split(".")[1] == "png":
            fullPah = filepath + imagePath
            fp = open(fullPah, 'rb')
            image = fp.read()
            base64_data = base64.b64encode(image).decode('utf-8')
            fp.close()
            imageList.append(base64_data)

    return imageList


#必填项:dbName:test   imageData  method:"post"
def makeJson(imageList,file):

    # TODO  拼接一个json文件
    list=[]
    dict_out={}

    dict_in ={}

    #with open(file, "w") as fp:
    for image in imageList:
        dict_out["method"]= "post"
        dict_in["group_id"]= 44
        dict_in["photo"]= image
        dict_out["body"] = dict_in
        #dict_out["Content-Type"]="application/json"
        list.append(dict_out)
    with open(file,"w") as fp:
        json.dump(list,fp)

#测试一下看是否写成功了
def  main_function():
    imagelist = read_file(filepath)

    makeJson(imagelist,filename)


main_function()