# coding=utf-8
# @Author:SDY
# @File:test11.py
# @Time:2022/7/31 15:10
# @Introduction: 爬取所有城市名称https://www.aqistudy.cn/historydata/
import requests
from lxml import etree
if __name__ == '__main__':
    url = 'https://www.aqistudy.cn/historydata/'
    # ua伪装
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }
    response = requests.get(url=url,headers=headers)
    # 处理页面字符集不统一的问题
    response.encoding = response.apparent_encoding
    response_text = response.text
    etree_text = etree.HTML(response_text)
    # 拿到热门城市
    # hot_lis = etree_text.xpath('//div[@class="hot"]//ul/li')
    # all_lis = etree_text.xpath('//div[@class="all"]//ul//li')
    # city_names = []
    # # 遍历热门城市
    # for li in hot_lis:
    #     hot_city_name = li.xpath("./a/text()")[0]
    #     city_names.append(hot_city_name)
    # for li in all_lis:
    #     city_name = li.xpath("./a/text()")[0]
    #     city_names.append(city_name)
    # print(city_names)

    # 上边爬取热门城市名称和所有城市名称解析了两次页面数据，可以解析一次就够了的
    a_lis = etree_text.xpath('//div[@class="hot"]//ul/li | //div[@class="all"]//ul//li')

    city_names = []
    for li in a_lis:
        city_name = li.xpath("./a/text()")[0]
        city_names.append(city_name)
    print(city_names)


