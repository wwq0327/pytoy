#!/usr/bin/env python

import requests

URL = "http://httpbin.org/%s"

__all__ = [
	# 'hello',
	'r_post',
]

# def hello():
# 	print 'hello'

def r_post():
	url = URL % 'post'
	print url
	payload = {'key1': 'value1', 'key2' : 'value2', 'key3': 'value3'}
	r = requests.post(url, data = payload)
	# print r.url
	print r.text

def main():
	for func in __all__:
		eval(func+'()')

if __name__ == '__main__':
	main()
