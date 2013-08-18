#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import os
import requests

LOGO_URL = 'http://www.nipic.com/design/7/'

def get_page_url(page_num):
    return LOGO_URL + str(page_num) + '.html'

def get_html(url):
    r = requests.get(url)
    print '正在读取的页面地址：', r.url
    if r.status_code == 200:
        return r.content
    else:
        return None

def main():
    page_url = get_page_url(1)
    print get_html(page_url)

if __name__ == '__main__':
    main()
