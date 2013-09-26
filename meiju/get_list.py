#!/usr/bin/env python
# -*- coding: utf-8 -*-
# wwq @ 2013-09-26 22:30:40

import re
from datetime import datetime
import requests

URL = 'http://www.yyets.com/tv/schedule'

def get_day():
    today = datetime.today()
    return today.day

def set_day_str():
    return str(get_day()) + '号'

def get_html(url):
    r = requests.get(url)
    print '正在读取的页面地址：', url
    if r.status_code == 200:
        return r.content
    else:
        return None

def get_day_html(html):
    day = set_day_str()
    regex = r'<td class="ihbg">.+?<dt>%s</dt>(.+?)</dl>' % day
    re_day = re.compile(regex, re.DOTALL)
    m = re.findall(re_day, html)
    return m[0] 

def get_jm_list(day_html):
    regex = r'<div class="floatSpan"><span>(.+?)<span></div>'
    re_jm = re.compile(regex, re.DOTALL)
    m = re.findall(re_jm, day_html)
    return m

def main():
    html = get_html(URL)
    #print html
    #print '今天是: ', set_day_str()
    day_html = get_day_html(html)
    #print day_html
    jm_list = get_jm_list(day_html)
    #print jm_list
    print '今天的美剧节目有：'
    print '=' * 64
    for i in jm_list:
        print i

if __name__ == '__main__':
    main()

