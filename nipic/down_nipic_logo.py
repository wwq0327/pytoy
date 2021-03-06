#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import os
import urllib
import requests

BASE_URL = 'http://www.nipic.com'
LOGO_URL = 'http://www.nipic.com/design/7/'

def get_page_num():
    r_page = re.compile(r'<td height="25" class="tahoma" style="padding-left:9">第1页 共(.+?)页.+?</td>', re.DOTALL)
    page_url = get_page_url(1)

    html = get_html(page_url)

    s = re.findall(r_page, html.decode('gb2312').encode('utf-8'))
    return int(s[0])

def get_page_url(page_num):
    return LOGO_URL + str(page_num) + '.html'

def get_html(url):
    r = requests.get(url)
    print '正在读取的页面地址：', r.url
    if r.status_code == 200:
        return r.content
    else:
        return None

def get_signal_page(html):
    '''读取单页URL'''
    prog = re.compile(r'<td style="padding:4"><a href="(.+?)" title=.+? class="hui">.+?</a>')
    url_list = re.findall(prog, html)

    return url_list

def get_pic_url(pic_page_url):
    html = get_html(BASE_URL+pic_page_url)
    #print html
    re_pic = re.compile(r'<td align="center"><img src="(http://.+?\.jpg)".+?title="(.+?)".+?onload="DrawImage\(this\);".+?</td>', re.DOTALL)
    pic_url = re.findall(re_pic, html)

    return pic_url

def down_pic(pic_url):
    if pic_url:
        url = pic_url[0][0]
        pic_name = pic_url[0][1]
        pic_name = pic_name.decode('gb2312').encode('utf-8')
    pic_dir = 'pic/'
    urllib.urlretrieve(url, pic_dir+pic_name+'.jpg')

    print '保存了', pic_name

def main():
    all_num = get_page_num()
    print '共计 %s 页' % all_num
    print '*'*80
    count = 1
    while count <=all_num:
        page_url = get_page_url(count)
        count += 1
        html = get_html(page_url)
        s_page_url = get_signal_page(html)
        #print s_page_url
        for url in s_page_url:
            #print url
            pic_url = get_pic_url(url)
            #print pic_url
            down_pic(pic_url)

    #page_url = get_page_url(1)
    #html = get_html(page_url)
    #page_url = get_signal_page(html)
    #print page_url

    #pic_url = get_pic_url('/show/8595581.html')
    #print pic_url
    #down_pic(pic_url)

    #page_num = get_page_num()
    #print page_num, type(page_num)
if __name__ == '__main__':
    main()
