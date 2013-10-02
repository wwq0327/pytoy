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
        return pages_list

    def get_video_url(self, url):
        r = requests.get(url)
        if r.status_code == 200:
            html = r.content
        else:
            html = None
        p = re.compile(r'appsrc: \'(http://mov\.bn\.netease\.com/.+?\.m3u8)\',', re.DOTALL)
        end = p.findall(html)

        return end[0]
    
    def filter_url(self, video_list):
        '''过滤无用的列表'''

        nofile = 'http://mov.bn.netease.com/movie/nofile/list.m3u8'
        vl = []
        for i in xrange(len(video_list)):
            if not video_list[i][0] == nofile:
                vl.append(video_list[i])

        return vl
    def video(self, vl):
        vs = []
        for l in vl:
            if l[0].find('open-movie'):
                vs.append((l[0].replace('m3u8', 'mp4'), l[1]))
            else:
                vs.append((l[0].replace('m3u8', 'flv'), l[1]))

        return vs
    
    def play_page(self, page_list):
        '''单个视频页面链接列表'''
        video_list = []
        for page in page_list[:50]:
            p = self.get_video_url(page[0])
            video_list.append((p, page[1].decode('gb2312').encode('utf-8')))
        return video_list

    def down_file(self, vs):
        f = open('video.sh', 'w')
        for v in vs:
            filename = "%s.%s" % (v[1], os.path.split(v[0])[1])
            cmd = 'wget -o %s %s' % (filename, v[0])
            f.write(cmd)

        f.close()

def main():
    oc = OpenClass(TED_URL)
    
    html = oc.get_html()
    #print html
    page_list = oc.get_ted_page(html)
    page = oc.play_page(page_list)
    vs = oc.filter_url(page)
    oc.down_file(oc.video(vs))

if __name__ == '__main__':
    main()

