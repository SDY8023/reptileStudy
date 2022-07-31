# coding=utf-8
# @Author:SDY
# @File:test7.py
# @Time:2022/7/24 17:32
# @Introduction:
import requests
import re
import os
from bs4 import BeautifulSoup
if __name__ == '__main__':
    os.environ['NO_PROXY'] = 'stackoverflow.com'
    url = "https://image.baidu.com/search/acjson?"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }
    pictureList = []
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
        , "pn": 0
        , "rn": 30
        , "gsm": "3c"
        , "1658068112810": ""
    }
    pageData = requests.get(url=url, params=paramData, headers=headers).content
    # print(pageData)
    soup = BeautifulSoup(pageData,'lxml')
    # print(soup.strong)
    print(soup.find("strong").text)


