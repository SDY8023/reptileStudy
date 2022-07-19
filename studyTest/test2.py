# coding=utf-8
# @Author:SDY
# @File:test2.py
# @Time:2022/7/5 22:32
# @Introduction: 网页采集器

# UA检测：门户网站的服务器会检测对应请求的载体身份标识，若检测到请求载体身份标识为某一浏览器，说明该请求是正常请求，
# 否则就认为是爬虫
# UA: User-Agent (请求载体的身份标识)
# UA伪装：让爬虫对应的请求载体身份标识伪装成某一款浏览器
import requests
if __name__ == '__main__':
    # UA 伪装
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }
    # 这里的wd=后面跟的内容就是关键词，从网页上复制下来后就变乱码了，可以改为中文字符
    url = 'https://www.sogou.com/web?'
    # 处理url携带的参数：封装到字典中
    kw = input('enter a word:')
    param = {
        'wd':kw
    }
    # 对指定的url发起的请求对应的url是携带参数的，并且请求过程中处理了参数
    response = requests.get(url=url,params=param,headers=headers)

    page_text = response.text
    fileName = kw + '.html'
    with open(fileName,'w',encoding='utf-8') as fp:
        fp.write(page_text)
    print('保存成功!!')

