#!/usr/bin/env python
# -*- coding: utf-8 -*-
# wwq @ 2013-10-02 09:58:10

import sys
import re
import requests

reload(sys)
sys.setdefaultencoding('utf-8')

TED_URL = 'http://open.163.com/ted'

class OpenClass:
    def __init__(self, url):
        self.url = url

    def get_html(self):
        r = requests.get(self.url)
        if r.status_code == 200:
            return r.content
        else:
            return None

    def get_ted_page(self, html):
        '''获取当页所有TED视频的播放页面链接'''

        html = html.replace('\n', '').strip()
        regex = r'<li class="f-fl">\s+<a href="(http://v.163.com/movie/.+?)" class="listT">.+?<p>(.+?)<(/p|p)>.+?</a>\s+</li>'
        p_re = re.compile(regex, re.DOTALL)
        pages_list = p_re.findall(html)
        #print len(pages_list)
        return pages_list

    def get_video_url(self, url):
        r = requests.get(url)
        if r.status_code == 200:
            html = r.content
        else:
            html = None
        p = re.compile(r'appsrc: \'http://mov\.bn\.netease\.com/.+?\.m3u8\',', re.DOTALL)
        end = p.findall(html)

        return end[0]

    def play_page(self, page_list):
        for page in page_list:
            p = self.get_video_url(page[0])
            print p
            #print "%s ==> %s" % (page[0], page[1].decode('gb2312').encode('utf-8'))


def main():
    oc = OpenClass(TED_URL)
    
    html = oc.get_html()
    #print html
    page_list = oc.get_ted_page(html)
    print oc.play_page(page_list)

if __name__ == '__main__':
    main()
