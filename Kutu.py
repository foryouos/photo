import random
import requests
import time
import hashlib
#python的视频整理库movepy
from moviepy.editor import *
import os #引用文件操作库
import re
import json

def search_url():
    API_url="https://api.coolapk.com/v6/picture/list?"
    #url="https://api.coolapk.com/v6/picture/list?type=recommend&tag=%E9%A3%8E%E6%99%AF&page=1"
    #url类型recommend为推荐，hot为热门，newest为最新的
    type="newest"
    # 为内容页数,每一页在10-15个用户上传
    page=1
    # 为照片的标签
    """
    常见标签：
    小清新
    风景
    二次元
    壁纸
    """
    tag="小清新"
    picture_url=API_url+"&type="+type+"&page="+str(page)+"&tag="+tag
    print(picture_url)
    header = {
        "Accept": "*/*",
        "Accept-Encoding": "br;q=1.0, gzip;q=0.9, deflate;q=0.8",
        "Accept-Language": "zh-Hans-CN;q=1.0",
        "Connection": "keep-alive",
        "Cookie": "SESSID=577385abcaaa4d7e7006cfdc5c717e9615749fe4",
        "Host": "api.coolapk.com",
        "User-Agent": "Mozilla/5.0 (iPad Air (4th generation); CPU iPhone OS 15_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0 Mobile/15E148 Safari/604.1 (#Build; Apple; iPad Air (4th generation); iOS15.1; 15.1) +iCoolMarket/4.4.4",
        "X-Api-Version": "11",
        "X-App-Code": "2110201",
        "X-App-Device": "kibvlGdhJXZuV2ZggGd0gCIylWQgQWYQlGI7UGbwBXQgsTZsBHcBByOgsDI7AyOEVER0EEM0MTMFdTOtkDOwEUL4gjQ00iNzEzQtcDOBJURGNTR",
        "X-App-Id": "com.coolapk.app",
        "X-App-Token": "fd00ce75e748672442c1b1018663a423E3FEBA87-C136-4B88-A089-97E1340A4DED0x618f6b8a",
        "X-App-Version": "4.4.4",
        "X-Requested-With": "XMLHttpRequest",
        "X-Sdk-Int": "15.1",
        "X-Sdk-Locale": "zh-CN "
    }
    r=requests.get(url=picture_url,headers=header)
    content =r.json()
    #print(content)
    #json.dumps（）方法接受json对象，并返回JSON格式的字符串。 indent参数用于定义格式化字符串的缩进级别。
    #json.dump会自动转化为ascii编码，使用ensure_ascii=False
    json_content=json.dumps(content,indent=4,ensure_ascii=False)
    #print(json_content)
    """
    json的loads()函数将json数据转化为dict数据
    dumps()函数将dict数据转化为JSON数据
    """

    datas=json.loads(json_content)["data"]
    for data in datas:
        chinese=re.compile('[\u4e00-\u9fa5]+')  #使用汉字编码特征截取汉字部分
        messages=str(data["message"])
        message=chinese.findall(messages)
        print(message)
        print(data["picArr"])

if __name__=="__main__":
    content_url=search_url()