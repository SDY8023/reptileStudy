# coding=utf-8
# @Author:SDY
# @File:test3.py
# @Time:2022/7/6 21:44
# @Introduction: 爬取百度翻译
import requests
import json
if __name__ == '__main__':
    #1 指定url
    post_url = 'https://fanyi.baidu.com/sug'
    #2 进行UA伪装
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }
    # 数据获取
    data = {
        'kw':'dog'
    }
    #3 发送请求，并获取响应数据
    response = requests.post(url=post_url,data=data,headers=headers)
    #4 在确认响应数据是json后才可以转换为obj对象
    dic_obj = response.json()
    print(dic_obj)
    # 持久化存储
    fp = open('./dog.json','w',encoding='utf-8')
    json.dump(dic_obj,fp=fp,ensure_ascii=False)
    fp.close()
    print("over!!!")
