# coding=utf-8
# @Author:SDY
# @File:test4.py
# @Time:2022/7/6 22:29
# @Introduction: 爬取豆瓣电影
import requests
import json
if __name__ == '__main__':
    url = 'https://movie.douban.com/j/chart/top_list?'

    params={
        'type': '24',
        'interval_id': '100:90',
        'action':'',
        'start': '1',#从库中的第几部电影取数据
        'limit': '20' # 一次取出的个数
    }

    #2 进行UA伪装
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }

    response = requests.get(url=url,params=params,headers=headers)

    list_data = response.json()

    print(list_data)

