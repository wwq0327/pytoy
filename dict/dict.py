#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import urllib2
from BeautifulSoup import BeautifulSoup

DICT_URL = 'http://3g.dict.cn/s.php?q=%s'

def read_http(url, word):
    sock = urllib2.urlopen(url%word)
    return sock.read()

def dict(word):
    doc = read_http(DICT_URL, word)
    soup = BeautifulSoup(''.join(doc))
    return soup.findAll('div')[3]

def main():
    word = sys.argv[1]
    print dict(word)

if __name__ == '__main__':
    main()

