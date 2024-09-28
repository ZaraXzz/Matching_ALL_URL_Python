#-*- coding:utf-8 -*-
####################################################
#
#    Author: Chuwei Luo
#    Email: luochuwei@gmail.com
#    Date: 17/03/2016
#    Usage: Matching all urls
#
####################################################
import re
import requests

def find_all_url(sentence, show_urls = None, delete_urls = None):
    r = re.compile(r'(?i)\b((?:[a-z][\w-]+:(?:/{1,3}|[a-z0-9%])|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:\'".,<>?«»“”‘’]))')
    url_list = r.findall(sentence)
    if show_urls == 1:
        print("find," + str(len(url_list)))
        for i in url_list:
            print(i[0])

    if delete_urls == 1:
        for j in url_list:
            # sentence = sentence.replace(j[0], '<URL>')
            sentence = sentence.replace(j[0], '')
        return sentence
    return 1



def download_webpage(url):
    try:
        # 发送GET请求
        response = requests.get(url)
        # 确保请求成功
        response.raise_for_status()
        # 返回网页内容
        return response.text
    except requests.RequestException as e:
        # 打印错误信息
        print(f"Error downloading the webpage: {e}")
        return None




if __name__ == '__main__':
    # 使用函数
    url = 'https://www.bbc.com'  # 替换为你想要下载的网页的URL
    webpage_content = download_webpage(url)
    find_all_url(webpage_content, show_urls=1)




