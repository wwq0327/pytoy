#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import sys
import urllib2

DICT_URL = 'http://3g.dict.cn/s.php?q=%s'

def get_http(url, word):
	sock = urllib2.urlopen(url%word)
	return sock.read()

def dict(html):
	regex = r'<div class="exp">(.+?)</div>'
	re_dt = re.compile(regex, re.DOTALL)
	m = re_dt.findall(html)
	## print len(m)
	return m

def html_format(s):
	s = s.replace("<span>", "").replace("</span>", "").replace("<br/>", "")
	s = " ".join(d.strip() for d in s.split("\n"))
	return s

def main():
	word = sys.argv[1]
	html = get_http(DICT_URL, word)
	m = dict(html)
	s = html_format(m[0])
	print s

if __name__ == '__main__':
	main()
