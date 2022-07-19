# coding=utf-8
# @Author:SDY
# @File:test5.py
# @Time:2022/7/6 22:38
# @Introduction: 肯德基位置获取
import requests
import json
if __name__ == '__main__':
    # 1 指定url
    url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?'
    # 2 指定参数
    data = {
        'op':'keyword',
        'cname':'',
            'pid':'',
    'keyword': '南京',
    'pageIndex': '2',
    'pageSize': '10'
    }
    # 3 进行UA伪装
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }
    # 4 发送请求
    dict_json = requests.post(url=url,data=data,headers=headers)
    # 5 持久化存储
    result = dict_json.json()
    print(result)

