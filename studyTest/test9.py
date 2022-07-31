# coding=utf-8
# @Author:SDY
# @File:test9.py
# @Time:2022/7/24 22:53
# @Introduction:xpath练习之58二手房爬取
import requests
from lxml import etree
if __name__ == '__main__':
    url = "https://nj.58.com/ershoufang/"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }
    # 爬取页面数据
    page_txt = requests.get(url=url,headers=headers).text

    #数据解析
    tree = etree.HTML(page_txt)
    section_list = tree.xpath('//section[@class="list"]/div')
    #print(section_list)
    fp = open('./58house.txt','w',encoding='utf-8')
    for div in section_list:
        # 这里的点表示局部定位到的标签
        title = div.xpath('./a/div[2]//div[@class="property-content-title"]/h3/text()')[0]
        address = div.xpath('./a/div[2]//section//p[@class="property-content-info-comm-address"]/span/text()')
        price = div.xpath('./a/div[2]//div[@class="property-price"]/p[1]/span[@class="property-price-total-num"]/text()')[0]
        unit = div.xpath('./a/div[2]//div[@class="property-price"]/p[1]/span[@class="property-price-total-text"]/text()')[0]
        unit_every = div.xpath('./a/div[2]//div[@class="property-price"]/p[2]/text()')[0]
        print(title+" 总价:"+price+unit+" 单价:"+unit_every+" 地址：" + "-".join(address))
        fp.write(title+" 总价:"+price+unit+" 单价:"+unit_every+" 地址：" + "-".join(address)+'\n')
    fp.close()




