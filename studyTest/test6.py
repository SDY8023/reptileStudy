# coding=utf-8
# @Author:SDY
# @File:test6.py
# @Time:2022/7/17 20:50
# @Introduction: 爬取糗事百科图片
import requests
import re
import os
if __name__ == '__main__':
    url = "https://image.baidu.com/search/acjson?"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }
    pictureList = []
    for pn in range(0,300,30):
        paramData = {
            "tn": "resultjson_com"
            , "logid": 11452365279271225749
            , "ipn": "rj"
            , "ct": 201326592
            , "is": ""
            , "fp": "result"
            , "fr": "ala"
            , "word": "美女图片库"
            , "queryWord": "美女图片库"
            , "cl": 2
            , "lm": -1
            , "ie": "utf-8"
            , "oe": "utf-8"
            , "adpicid": ""
            , "st": ""
            , "z": ""
            , "ic": ""
            , "hd": ""
            , "latest": ""
            , "copyright": ""
            , "s": ""
            , "se": ""
            , "tab": ""
            , "width": ""
            , "height": ""
            , "face": 0
            , "istype": 2
            , "qc": ""
            , "nc": "1"
            , "expermode": ""
            , "nojc": ""
            , "isAsync": ""
            , "pn": pn
            , "rn": 30
            , "gsm": "3c"
            , "1658068112810": ""
        }
        pageData = requests.get(url=url, params=paramData, headers=headers).text
        ex = '"thumbURL":"(.*?)","commodityInfo"'
        pictureList += re.findall(ex,pageData,re.S)
    # print(pictureList)
    if not os.path.exists("./meinv"):
        os.mkdir("./meinv")
    for pictUrl in pictureList:
        fileName = str(pictUrl).split("=")[-1]
        pictureData = requests.get(url=pictUrl,headers=headers).content
        with open("./meinv/"+fileName+".jpg",'wb') as fp:
            fp.write(pictureData)
        print(pictUrl,"下载成功！！！")



