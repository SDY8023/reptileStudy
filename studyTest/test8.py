# coding=utf-8
# @Author:SDY
# @File:test8.py
# @Time:2022/7/24 21:55
# @Introduction: 爬取三国演义小说
import requests
from bs4 import BeautifulSoup
if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }
    # 获取总页面数据
    url = "https://sanguo.5000yan.com/"
    total_page_txt = requests.get(url=url,headers=headers)
    # print(total_page_txt.apparent_encoding)
    # print(total_page_txt.encoding)
    total_page_txt.encoding = total_page_txt.apparent_encoding
    # 封装bs4
    soup = BeautifulSoup(total_page_txt.text,'lxml')
    # print(soup)
    # 解析出所有的章节页面的url
    li_list = soup.select(".sidamingzhu-list-mulu > ul > li")
    fp = open("./sanguo.text","w",encoding="utf-8")
    # 遍历每一个章节url
    for li in li_list:
        # 获取每个章节的标题
        title = li.a.string
        page_url = li.a['href']
        page_txt = requests.get(url=page_url,headers=headers)
        page_txt.encoding = page_txt.apparent_encoding
        page_soup = BeautifulSoup(page_txt.text,'lxml')
        detail_page_txt = page_soup.find('div',class_="grap")
        fp.write(title + ":\n" + detail_page_txt.text + "\n")
        print(title + ": 下载完成!")
    fp.close()
