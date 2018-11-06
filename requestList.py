# coding=utf-8

import requests
import json

# 金铭的接口列表
JingMingrequestList = [{"method":"get","path":"version","querystring":"","body": ""},  #系统信息
{"method":"get","path":"detail","querystring":"","body": ""},   #获取底库规格信息
{"method":"POST","path":"target/add","querystring":{"dbName": "test5555"},"body": ""},  # 创建底库
{"method": "POST", "path":"target/get", "querystring": "", "body": ""},  # 获取信息
{"method": "POST", "path":"target/clear", "querystring": {"dbName": "test5555"}, "body": ""}, #清空底库,未实现
{"method": "POST", "path":"target/delete", "querystring": {"dbName": "test5555"}, "body": ""},  # 删除底库
{"method": "POST", "path": "face/detectAndQuality", "querystring": "", "body":{"imageData":open("D:\\WorkSpace\\2k\\VT001_00000776.jpg","rb")}}, #人脸检测与质量评分
#{"method":"POST","path":"face/add","querystring":{"dbName":"test1234"},"body": {"imageData":open("D:\\WorkSpace\\2k\\VT001_00000776.jpg","rb")} },  #图片入库
#{"method": "GET", "path": "face/get", "querystring": {"dbName": "test1234","imageId": "E79717D44076D48A503ED4FA37767452"},"body": ""}, #获取图片
{"method": "POST", "path": "face/search", "querystring": {"dbName": "test1234","topNum":50,"score": 0.5},"body": {"imageData": open("D:\\WorkSpace\\2k\\VT001_00000776.jpg","rb")}}, #图片搜索
{"method": "POST", "path": "face/verification", "querystring":"","body": {"imageOne": open("D:\\WorkSpace\\2k\\VT001_00000776.jpg","rb"),"imageTwo":open("D:\\WorkSpace\\2k\\VT001_00000776.jpg","rb")}}, #人脸验证
{"method": "POST", "path": "face/deletePerson", "querystring": {"dbName": "test1234","personId":"2911888638490"},"body": ""}, # 删除人员
{"method": "POST", "path": "face/deleteImage", "querystring": {"dbName": "test1234","imageId":"B5E98DCAC8E54A289378FC16F4015C0E"},"body":""}, #删除图片
{"method": "POST", "path": "face/attribute", "querystring": "","body": {"imageData": open("D:\\WorkSpace\\2k\\VT001_00000776.jpg","rb")}}, # 人脸属性
{"method": "POST", "path": "face/liveRate", "querystring": "","body": {"imageData": open("D:\\WorkSpace\\2k\\VT001_00000776.jpg",'rb')}},  #活体验证
{"method": "POST", "path": "feature/add", "querystring": {"dbName": "test1234"},"body": {"feature": "p9LfQGgdZMB364LAmvshQO4Z4UBWs4PBkg6pQaYAxcGhDzHBwOdBwaul4z8txJs/c8mPQP16tL+pmcvAZhcPwYHlN8AhG5XB7M8awd2+70DtJl6+8LRWwOl0vEA6ZptAD0BGwCl+z8BBi0dAfkajwSodYMB737c/8AqxQa0FdEH8aLPAfSVrwQPvwsDNWtzA0G+jwB5eEEC3BvFAkW/9vwSvDsGGJBtAFT1nQDcXG0F/3EhAjtnOP+LX1EAXJWpAkEG3P6K0kz8alHDB5y7bwHQ0YcBMB1K/+p8YQKOsCsG2ecVBojBaQWnT4EDMJfLAk+PJQOmnC0CO7GtB+um7v6i47EC6Tq9Arp0TQY/jfr932mxBrxYEvxMTeUCmwurAYnGEQDh4S0HIfFDBptIiwbudlkEkM2zAdM0ZQS4cG8FrA/w/JjgswPlikcA9Bgc/RjINv4u7TEEETNHAtbNVwPzT2r9Ncca/2zwZwYJOYUBd3T5AcrGoQOpMTD81zd4/IJ0GwW7KSsBe9jlAWRYWv6n5L8GJSyNB5UOEwKDPfsEdji5AbNr9wMEfAcBaRCjBFNhFQRMZ+r8ryo7BiskiQHi5gEGBMztB63gNQRdDBkFL+DFBqAygPxfBxMA60oy+xbbzwOCLJ0FmiUtBfLBgwGFL/j++MVVBiZ1lwa7BQUEs1HdAcL+FwFK8u0CwEsbAJlPfQP1MTkHCN7E/X/WGv6uUjEDQO/DAhwYlQJDZi8DJzv7ArT0uv/KbF0Eiv1RAQKM0QeHxEsE+f8PADncDQc36YkFs7X7AqgvuwOH0kMCua+FAP7mawYqAsb/mMjHBJkeSQBwxtMBpEjtB0ymgwBQvRMHpqqLA0SaeP5JpKcD/Zqw/0uq7vzIfdsBcNhbBkcYUQKQQEcA4SQ4/GY8OQKd9uECe+mJAhEwoQbb9qkCV0DjAyAlgwWpz7T4n5hPBOjNqwS5euD8J9DFAPXFuwKyH3UHQuFZABobhQEzk9D+82Py9KrOswa51I8EeJfPAKtGjwR+VK8CUlMLA7DivwIiWi8FxBYNA/kh5PzgkI0AjpivBmCgvQQ3j30BdshdBnUA0Pw8cmEBuxFvBMT8twaeqLEFfnBPBDnSHQEZ3JcGJRo9BLfUkQRo4uMBwBmLBHbcKwcVMK8EqcHTB2yVLQHSAE0FVQIdBtDO6wADR4kDFgPRAIUPKP8CJycAnafTAneyiv+kt0r/GtL7Af4bZwLi3rkCctDRBnTTgQBWNtr/bdi+/4EqGP0nBp0B6iSVBAdkJQRZgakErAVY/r2GFv/DptcDm8z3BARURQcmyc0HN/Ty/zUmeQFTMGcH3fC3BGkSAQfAXakHDaNXAN5gNQQ=="}}, #特征入库   feature从哪里获取的
{"method": "POST", "path": "feature/search", "querystring": {"dbName": "test1234","topNum":50,"score":0.5},"body": {"feature": "p9LfQGgdZMB364LAmvshQO4Z4UBWs4PBkg6pQaYAxcGhDzHBwOdBwaul4z8txJs/c8mPQP16tL+pmcvAZhcPwYHlN8AhG5XB7M8awd2+70DtJl6+8LRWwOl0vEA6ZptAD0BGwCl+z8BBi0dAfkajwSodYMB737c/8AqxQa0FdEH8aLPAfSVrwQPvwsDNWtzA0G+jwB5eEEC3BvFAkW/9vwSvDsGGJBtAFT1nQDcXG0F/3EhAjtnOP+LX1EAXJWpAkEG3P6K0kz8alHDB5y7bwHQ0YcBMB1K/+p8YQKOsCsG2ecVBojBaQWnT4EDMJfLAk+PJQOmnC0CO7GtB+um7v6i47EC6Tq9Arp0TQY/jfr932mxBrxYEvxMTeUCmwurAYnGEQDh4S0HIfFDBptIiwbudlkEkM2zAdM0ZQS4cG8FrA/w/JjgswPlikcA9Bgc/RjINv4u7TEEETNHAtbNVwPzT2r9Ncca/2zwZwYJOYUBd3T5AcrGoQOpMTD81zd4/IJ0GwW7KSsBe9jlAWRYWv6n5L8GJSyNB5UOEwKDPfsEdji5AbNr9wMEfAcBaRCjBFNhFQRMZ+r8ryo7BiskiQHi5gEGBMztB63gNQRdDBkFL+DFBqAygPxfBxMA60oy+xbbzwOCLJ0FmiUtBfLBgwGFL/j++MVVBiZ1lwa7BQUEs1HdAcL+FwFK8u0CwEsbAJlPfQP1MTkHCN7E/X/WGv6uUjEDQO/DAhwYlQJDZi8DJzv7ArT0uv/KbF0Eiv1RAQKM0QeHxEsE+f8PADncDQc36YkFs7X7AqgvuwOH0kMCua+FAP7mawYqAsb/mMjHBJkeSQBwxtMBpEjtB0ymgwBQvRMHpqqLA0SaeP5JpKcD/Zqw/0uq7vzIfdsBcNhbBkcYUQKQQEcA4SQ4/GY8OQKd9uECe+mJAhEwoQbb9qkCV0DjAyAlgwWpz7T4n5hPBOjNqwS5euD8J9DFAPXFuwKyH3UHQuFZABobhQEzk9D+82Py9KrOswa51I8EeJfPAKtGjwR+VK8CUlMLA7DivwIiWi8FxBYNA/kh5PzgkI0AjpivBmCgvQQ3j30BdshdBnUA0Pw8cmEBuxFvBMT8twaeqLEFfnBPBDnSHQEZ3JcGJRo9BLfUkQRo4uMBwBmLBHbcKwcVMK8EqcHTB2yVLQHSAE0FVQIdBtDO6wADR4kDFgPRAIUPKP8CJycAnafTAneyiv+kt0r/GtL7Af4bZwLi3rkCctDRBnTTgQBWNtr/bdi+/4EqGP0nBp0B6iSVBAdkJQRZgakErAVY/r2GFv/DptcDm8z3BARURQcmyc0HN/Ty/zUmeQFTMGcH3fC3BGkSAQfAXakHDaNXAN5gNQQ=="}}, # 特征搜索  特征值
{"method": "POST", "path": "feature/verification", "querystring": "","body": {"featureOne": "p9LfQGgdZMB364LAmvshQO4Z4UBWs4PBkg6pQaYAxcGhDzHBwOdBwaul4z8txJs/c8mPQP16tL+pmcvAZhcPwYHlN8AhG5XB7M8awd2+70DtJl6+8LRWwOl0vEA6ZptAD0BGwCl+z8BBi0dAfkajwSodYMB737c/8AqxQa0FdEH8aLPAfSVrwQPvwsDNWtzA0G+jwB5eEEC3BvFAkW/9vwSvDsGGJBtAFT1nQDcXG0F/3EhAjtnOP+LX1EAXJWpAkEG3P6K0kz8alHDB5y7bwHQ0YcBMB1K/+p8YQKOsCsG2ecVBojBaQWnT4EDMJfLAk+PJQOmnC0CO7GtB+um7v6i47EC6Tq9Arp0TQY/jfr932mxBrxYEvxMTeUCmwurAYnGEQDh4S0HIfFDBptIiwbudlkEkM2zAdM0ZQS4cG8FrA/w/JjgswPlikcA9Bgc/RjINv4u7TEEETNHAtbNVwPzT2r9Ncca/2zwZwYJOYUBd3T5AcrGoQOpMTD81zd4/IJ0GwW7KSsBe9jlAWRYWv6n5L8GJSyNB5UOEwKDPfsEdji5AbNr9wMEfAcBaRCjBFNhFQRMZ+r8ryo7BiskiQHi5gEGBMztB63gNQRdDBkFL+DFBqAygPxfBxMA60oy+xbbzwOCLJ0FmiUtBfLBgwGFL/j++MVVBiZ1lwa7BQUEs1HdAcL+FwFK8u0CwEsbAJlPfQP1MTkHCN7E/X/WGv6uUjEDQO/DAhwYlQJDZi8DJzv7ArT0uv/KbF0Eiv1RAQKM0QeHxEsE+f8PADncDQc36YkFs7X7AqgvuwOH0kMCua+FAP7mawYqAsb/mMjHBJkeSQBwxtMBpEjtB0ymgwBQvRMHpqqLA0SaeP5JpKcD/Zqw/0uq7vzIfdsBcNhbBkcYUQKQQEcA4SQ4/GY8OQKd9uECe+mJAhEwoQbb9qkCV0DjAyAlgwWpz7T4n5hPBOjNqwS5euD8J9DFAPXFuwKyH3UHQuFZABobhQEzk9D+82Py9KrOswa51I8EeJfPAKtGjwR+VK8CUlMLA7DivwIiWi8FxBYNA/kh5PzgkI0AjpivBmCgvQQ3j30BdshdBnUA0Pw8cmEBuxFvBMT8twaeqLEFfnBPBDnSHQEZ3JcGJRo9BLfUkQRo4uMBwBmLBHbcKwcVMK8EqcHTB2yVLQHSAE0FVQIdBtDO6wADR4kDFgPRAIUPKP8CJycAnafTAneyiv+kt0r/GtL7Af4bZwLi3rkCctDRBnTTgQBWNtr/bdi+/4EqGP0nBp0B6iSVBAdkJQRZgakErAVY/r2GFv/DptcDm8z3BARURQcmyc0HN/Ty/zUmeQFTMGcH3fC3BGkSAQfAXakHDaNXAN5gNQQ== \
","featureTwo":"x8XSP1l0mECVlNK/QSoOwQCr1b/ncxlBlzg1QCWEs8BZPs5AQvGxwVwxtEEShQO/KfCZQFUBwEAebzfBIwEFQdYlmMFXvvvAOIQNQZVrJsHJ+8W/1LUowNocrr9Wx9M/F2InQdWwLL/cjli+8vZDwV0V1kACIiJB99YgwbYrK8GGtaTABTEpwNmPFcCPefVACUKnQJmtlT/LMhXAh7ThQJnwpUCAZRa/5U+eP+khoj9UYatAGvmpvkqAikA4EqXA5t0awTpYRMEF4JrB34t0QDP2oL5xwhQ+lREqvUuGN8Hx4f6/JriNwWd6ysCf+eO93QMzQdi4CEG/kgRAcqbPwIRXW8A0JiVAA2crQR7cTz5Twp3Am2pkQMYNLMDJ9STB7RtGQWlnJ8FsN+S/1OShQXHg8UBZP0tBVOXivh2wHMHvEw1ACosIQTswXEBne7xAsQAzQaO1CEGF2wZAlX4+P9c2KcDW5XxBqx5XQbbEyED5JTZAv5kewXVyOEFLcJk/f/c8wBqfg8HJqOa/abeAQft+iMETb5lA/k1twP5yYkHs9tXA3wKdQbVUFMBwjcnAVhhdQMhvocD2XhFBi1rlQJzGF0EyjaI/78ggwRP0d7/Hkl5BXurqwLDOA8EI28S+RwLBQPbFg0GBwS5BbTZ6QbuymEHwN8G+teBXwTseAkHNHrDBbD4NQYJWO0FviMFAnKsYv5uDTEEuaN7AcG4/QKjCT8C0CDlAs7m/wM43EUFT67TAiWNiQeWVjD1n3IY/w2EeQZJOfEFda5JBmpq9wA2tub7cuGZBnqutwJjjT8DwmE1BS1MYQRwllUDIz4vB542pwF/H98CgV/s/RAivwMnQM8E2DnDA90dDQClqBr+D+GhB5MSEQZG1FEDTjBrBewDDQHyUQUAHnYJAs8qAQaet2UCv4sBA48bev421JkCP4AvAX2DRQNzsPEF9AXNBqiUjQeb6wUFKpa4/l/47wVXSlUEmOAvAy887QQC1/kAnJoNBta25v/AyJMAMlYfAxchcwCrgOz+TfQ5Bx832QOkGGUHWNhhB5TTiQPCH/T9qTWJBRrAhwCPnSkHQbpJAukvJwNBwq8C2HQfBYO2uwK/ng8Ccpg/A+b5pwc3u6MBmAxFAbvYNwSWDUMHwjflAKVBjQLUlsL8Mm9xAuWAdv+B3W0C0gTJB2dEbv3hOoEA6fOTASQYGv8bMRkG8ZUw/TyojQRNpX0GhhYFAApOfQM20McH6Cd/AxL0wwP1WVEEIfmpBOn95QDvkBkCN251AXdxGwTB77EAPBx9Ahp46QBHf10ACad3AMRJ1wXt33cCqcD1AsRe0wEGSKcAsOaxBTlnfQGoP2EDDlxXB7WIPQQ=="}}, #特征验证
{"method": "POST", "path": "feature/compare", "querystring": {"dbName": "test1234","personId":"VT001_00000776"},"body": {"feature": "p9LfQGgdZMB364LAmvshQO4Z4UBWs4PBkg6pQaYAxcGhDzHBwOdBwaul4z8txJs/c8mPQP16tL+pmcvAZhcPwYHlN8AhG5XB7M8awd2+70DtJl6+8LRWwOl0vEA6ZptAD0BGwCl+z8BBi0dAfkajwSodYMB737c/8AqxQa0FdEH8aLPAfSVrwQPvwsDNWtzA0G+jwB5eEEC3BvFAkW/9vwSvDsGGJBtAFT1nQDcXG0F/3EhAjtnOP+LX1EAXJWpAkEG3P6K0kz8alHDB5y7bwHQ0YcBMB1K/+p8YQKOsCsG2ecVBojBaQWnT4EDMJfLAk+PJQOmnC0CO7GtB+um7v6i47EC6Tq9Arp0TQY/jfr932mxBrxYEvxMTeUCmwurAYnGEQDh4S0HIfFDBptIiwbudlkEkM2zAdM0ZQS4cG8FrA/w/JjgswPlikcA9Bgc/RjINv4u7TEEETNHAtbNVwPzT2r9Ncca/2zwZwYJOYUBd3T5AcrGoQOpMTD81zd4/IJ0GwW7KSsBe9jlAWRYWv6n5L8GJSyNB5UOEwKDPfsEdji5AbNr9wMEfAcBaRCjBFNhFQRMZ+r8ryo7BiskiQHi5gEGBMztB63gNQRdDBkFL+DFBqAygPxfBxMA60oy+xbbzwOCLJ0FmiUtBfLBgwGFL/j++MVVBiZ1lwa7BQUEs1HdAcL+FwFK8u0CwEsbAJlPfQP1MTkHCN7E/X/WGv6uUjEDQO/DAhwYlQJDZi8DJzv7ArT0uv/KbF0Eiv1RAQKM0QeHxEsE+f8PADncDQc36YkFs7X7AqgvuwOH0kMCua+FAP7mawYqAsb/mMjHBJkeSQBwxtMBpEjtB0ymgwBQvRMHpqqLA0SaeP5JpKcD/Zqw/0uq7vzIfdsBcNhbBkcYUQKQQEcA4SQ4/GY8OQKd9uECe+mJAhEwoQbb9qkCV0DjAyAlgwWpz7T4n5hPBOjNqwS5euD8J9DFAPXFuwKyH3UHQuFZABobhQEzk9D+82Py9KrOswa51I8EeJfPAKtGjwR+VK8CUlMLA7DivwIiWi8FxBYNA/kh5PzgkI0AjpivBmCgvQQ3j30BdshdBnUA0Pw8cmEBuxFvBMT8twaeqLEFfnBPBDnSHQEZ3JcGJRo9BLfUkQRo4uMBwBmLBHbcKwcVMK8EqcHTB2yVLQHSAE0FVQIdBtDO6wADR4kDFgPRAIUPKP8CJycAnafTAneyiv+kt0r/GtL7Af4bZwLi3rkCctDRBnTTgQBWNtr/bdi+/4EqGP0nBp0B6iSVBAdkJQRZgakErAVY/r2GFv/DptcDm8z3BARURQcmyc0HN/Ty/zUmeQFTMGcH3fC3BGkSAQfAXakHDaNXAN5gNQQ== \
"}}] #特征比对


#鹰眼的接口列表

'''
HawkEyeList = [{"method":"get","path":"groups","querystring":"","body": ""},  #获取底库列表
               {"method": "get", "path": "cameras", "querystring": "", "body": ""},    #获取视频源列表
               {"method": "get", "path": "summary", "querystring": "", "body": ""},    #系统概览
               {"method": "get", "path": "pass_records", "querystring": {"begin_time":"2018-09-01 18:00:00","end_time":"2018-09-01 19:00:00","start_page":1,"page_count":100}, "body": {"camera_id":1}},     #获取通行记录
               {"method": "get", "path": "alarm_records", "querystring": {"begin_time":"2018-09-01 18:00:00","end_time":"2018-09-01 19:00:00","start_page":1,"page_count":100}, "body": {"group_id":1,"keyword":"allen or 330320xxxxx","camera_location":"地铁口A"}},  # 报警记录
               {"method": "PUT", "path": "tasks", "querystring": {"begin_time":"2018-09-01 18:00:00","end_time":"2018-09-01 19:00:00","alarm_type":0,"alarm_threshold":0.7,"status":1,"mark":"xxx"}, "body": {"name":"xxx","camera_id":2,"group_ids":[1,2,3]}},  #任务管理
               {"method": "DELETE", "path": "tasks/:id", "querystring": {"id":1}, "body": ""}, #删除任务
               {"method": "get", "path": "tasks", "querystring": "", "body": ""},    #获取任务列表
               {"method": "get", "path": "version", "querystring": "", "body": ""},
               {"method": "get", "path": "version", "querystring": "", "body": ""},
               {"method": "get", "path": "version", "querystring": "", "body": ""},
               {"method": "get", "path": "version", "querystring": "", "body": ""},
               {"method": "get", "path": "version", "querystring": "", "body": ""},
               {"method": "get", "path": "version", "querystring": "", "body": ""},
               {"method": "get", "path": "version", "querystring": "", "body": ""},
               {"method": "get", "path": "version", "querystring": "", "body": ""},
               {"method": "get", "path": "version", "querystring": "", "body": ""},
               {"method": "get", "path": "version", "querystring": "", "body": ""},
               {"method": "get", "path": "version", "querystring": "", "body": ""},
               {"method": "get", "path": "version", "querystring": "", "body": ""},
               {"method": "get", "path": "version", "querystring": "", "body": ""},
               {"method": "get", "path": "version", "querystring": "", "body": ""},]
'''
#  http://192.168.1.188:88/verify/

def MakeRequests(requestList, url):
    for request in requestList:
        stringtest = url + request["path"]
        res = requests.request(request["method"], url + request["path"], files=request["body"],
                               params=request["querystring"])
        # print (res.text)
        print ("*" * 150)
        # 补充鹰眼的返回结果判断

        if request["path"] == "version":
            if res.status_code != requests.codes.ok or res.json()["result"]["result"] != "success":
                with open("JinMing.txt", "a+") as fp:
                    fp.write("error txt = %s resquest = %s" % (res.text, url + request["path"]))
                    fp.write("\n" + "*" * 200 + "\n\n")

        if res.status_code != requests.codes.ok or res.json()["result"] != "success":
            with open("JinMing.txt", "a+") as fp:
                fp.write("error txt = %s resquest = %s" % (res.text, url + request["path"]))
                fp.write("\n" + "*" * 200 + "\n\n")

#处理金铭的接口
JingMingUrl = "http://192.168.1.188:88/verify/"
MakeRequests(JingMingrequestList,JingMingUrl)

#处理鹰眼的接口
HawkEyeUrl = "http://192.168.1.173/api/"