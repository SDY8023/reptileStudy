# coding=utf-8
# @Author:SDY
# @File:test12.py
# @Time:2022/7/31 16:04
# @Introduction: 免费简历模板下载
import requests
from lxml import etree
import os
if __name__ == '__main__':
    # ua伪装
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }
    url = 'https://aspx.sc.chinaz.com/query.aspx?'
    params = {
        'keyword':'免费简历模板'
    }
    response = requests.get(url=url,params=params,headers=headers)
    response.encoding = response.apparent_encoding
    page_text = response.text
    etree_text = etree.HTML(page_text)

    # 解析最大页码数
    page_nums_a = etree_text.xpath('//div[@class="paging"]/a')
    # 定义最大页码数
    if not os.path.exists("./resumes"):
        os.mkdir("./resumes")
    max_page_nums = 1
    for page_nums in page_nums_a:
        page_num = page_nums.xpath('./@href')[0].split('=')[-1]
        # 因为前两个a标签中的属性值不是数字类型，所以做一次异常捕获
        try:
            if max_page_nums < int(page_num):
                max_page_nums = int(page_num)
        except ValueError as e:
            print(e)
    print(max_page_nums)
    for page_num in range(1,max_page_nums):
        page_url = "https://aspx.sc.chinaz.com/query.aspx?keyword=%E5%85%8D%E8%B4%B9%E7%AE%80%E5%8E%86%E6%A8%A1%E6%9D%BF&issale=&classID=0&navindex=0&page=" + str(page_num)
        page_response = requests.get(url=page_url,headers=headers)
        page_response.encoding = page_response.apparent_encoding
        page_etree_text = etree.HTML(page_response.text)
        new_blocks = page_etree_text.xpath('//div[@class="TPcontent_box"]//div[@class="imgload"]/div')
        print("开始下载第" + str(page_num) + "的数据！")
        for new_block in new_blocks:
            template_url = new_block.xpath('./div/a/@href')[0]
            # 发请求，获得免费简历下载页面数据
            try:
                resume_page_response = requests.get(url="https:" + template_url, headers=headers)
                resume_page_response.encoding = resume_page_response.apparent_encoding
                resume_page_text = resume_page_response.text
                resume_page_etree = etree.HTML(resume_page_text)
                # 由于页面简历中第一张简历的网页数据和其他的不一样，所以暂定这两种解析方式
                a_list = resume_page_etree.xpath(
                    '//div[@class="container"]//div[@class="c-div clearfix"]/a | //div[@class="bggray clearfix"]//div[@class="down_wrap"]//ul/li')
                dowLoad_url = a_list[0].xpath('./@href | ./a/@href')[0]
                file_name = str(page_num) + "-" + dowLoad_url.split("/")[-1]
                resume = requests.get(url=dowLoad_url, headers=headers).content
                with open("./resumes/" + file_name, "wb") as fp:
                    fp.write(resume)
            except Exception as e:
                print(e)







