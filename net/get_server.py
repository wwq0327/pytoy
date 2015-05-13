#!/usr/bin/env python
import urllib2
from threading import Thread

USER_AGENT = """Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36"""
URLS = [
        'http://www.baidu.com', 
        'http://www.weibo.com',
        'http://www.joinwee.com',
        'http://www.jianshu.com',
        'http://www.douban.com',
        'http://www.duokan.com'
        ]

def get_server_name(url):
    req = urllib2.Request(url)
    req.add_header('User-Agent', USER_AGENT)
    response = urllib2.urlopen(req)
    s = response.headers.get('server', None)
    return s


def test():
    for url in URLS:
        print get_server_name(url)

def main():
    threads = []
    for url in URLS:
        t = Thread(target=get_server_name, args=(url,))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

if __name__ == '__main__':
    main()
