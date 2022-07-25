# coding=utf-8
# @Author:SDY
# @File:test10.py
# @Time:2022/7/25 22:21
# @Introduction: 4k图片下载
import os

import requests
from lxml import etree
if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }
    url = "http://pic.netbian.com/4kmeinv/"
    response = requests.get(url=url,headers=headers)
    response.encoding = response.apparent_encoding
    page_text = response.text

    # 数据解析
    tree = etree.HTML(page_text)
    picture_list = tree.xpath('//div[@class="wrap clearfix"]/div[1]/div[3]/ul[@class="clearfix"]/li')
    picture_url_title = "http://pic.netbian.com"
    if not os.path.exists("./picture"):
        os.mkdir("./picture")
    for picture in picture_list:
        picture_url = picture_url_title+picture.xpath('./a/img/@src')[0]
        file_name = picture.xpath('./a/img/@alt')[0] + '.jpg'
        picture = requests.get(url=picture_url,headers=headers).content

        with open("./picture/"+file_name,'wb') as fp:
            fp.write(picture)
        print(file_name+"下载成功！！")
    # print(picture_list)
