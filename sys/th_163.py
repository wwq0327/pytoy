#!/usr/bin/env python
# -*- coding: utf-8 -*-
# wwq @ 2013-10-08 17:03:53

import os
import re
import requests
from threading import Thread
from Queue import Queue

queue = Queue()

URL = 'http://open.163.com/ted'
headers = {
        'User-Agent': "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.76 Safari/537.36" 
        }

def get_html(url):
    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        return r.content
    else:
        return None

def get_ted_url(html):
    '''获取当页所有TED视频的播放页面链接'''

    html = html.replace('\n', '').strip()
    regex = r'<li class="f-fl">\s+<a href="(http://v.163.com/movie/.+?)" class="listT">.+?<p>(.+?)<(/p|p)>.+?</a>\s+</li>'
    p_re = re.compile(regex, re.DOTALL)
    print '正在解析TED首页的视频链接...'
    pages_list = p_re.findall(html)
    return pages_list

def get_ted_page(i, q):
    while True:
        url = q.get()
        filename = os.path.join('/home/wyatt/backup/', url[1].decode('gb2312').encode('utf-8')+'.html')
        f = open(filename, 'w')
        print '开始读取内容: %s' % url[0]
        html = get_html(url[0])
        f.write(html)
        print "成功保存文件: %s" % filename
        q.task_done()

def run():
    for i in range(3):
        worker = Thread(target=get_ted_page, args=(i, queue))
        worker.setDaemon(True)
        worker.start()
    html = get_html(URL)
    page_list = get_ted_url(html)
    for url in page_list[:50]:
        queue.put(url)
    queue.join()
    print "Done"

if __name__ == '__main__':
    run()
