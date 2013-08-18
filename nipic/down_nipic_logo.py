#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import os
import requests

LOGO_URL = 'http://www.nipic.com/design/7/'

def get_page_url(page_num):
    return LOGO_URL + str(page_num) + '.html'

def get_html(url):
    return requests.get(url)

def main():
    page_url = get_page_url(1)
    print get_html(page_url)

if __name__ == '__main__':
    main()
