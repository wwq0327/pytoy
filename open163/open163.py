#!/usr/bin/env python
# -*- coding: utf-8 -*-
# wwq @ 2013-10-02 09:58:10
# 获取http://open.163.com 网站上的TED所有视频链接，并生成下载文件，
# 通过Shell命令，结合wget，即可下载所有的ted视频到本地。

import sys
import os
import re
try:
    import requests
except:
    print >>sys.stderr, "本程序依赖requests, 请先安装requests库"
    sys.exit(1)

#try:
#    import gevent
#    from gevent import monkey;monkey.patch_all()
#except:
#    print >>sys.stderr, "本程序依赖gevent, 请先安装gevent库"
#    sys.exit(1)


reload(sys)
sys.setdefaultencoding('utf-8')

TED_URL = 'http://open.163.com/ted'

class OpenClass:
    def __init__(self, url):
        self.url = url
        self.headers = {
                'User-Agent': "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.76 Safari/537.36" 
                }

    def get_html(self,url):
        r = requests.get(url, headers=self.headers)
        if r.status_code == 200:
            return r.content
        else:
            return None

    def get_ted_page(self, html):
        '''获取当页所有TED视频的播放页面链接'''

        html = html.replace('\n', '').strip()
        regex = r'<li class="f-fl">\s+<a href="(http://v.163.com/movie/.+?)" class="listT">.+?<p>(.+?)<(/p|p)>.+?</a>\s+</li>'
        p_re = re.compile(regex, re.DOTALL)
        print '正在解析TED首页的视频链接...'
        pages_list = p_re.findall(html)
        return pages_list

    def get_video_url(self, url):
        '''在视频页面中获到.m3mu链，这个链接中会包含有相应视频的地址'''

        #r = requests.get(url, headers=self.headers)
        #if r.status_code == 200:
        #    html = r.content
        #else:
        #    html = None
        html = self.get_html(url)
        p = re.compile(r'appsrc: \'(http://mov\.bn\.netease\.com/.+?\.m3u8)\',', re.DOTALL)
        end = p.findall(html)
        print '找到视频链接信息: %s' % end[0]
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
            # 所得到的链接有两类，一类是.mp4文件，一类是.flv文件，
            # 可以根据链接中是否合有'open-movie' 和'movie'进行区分
            # 对于.flv文件，需在对链接作处理
            if 'open-movie' in l[0].strip('/'):
                vs.append((l[0].replace('m3u8', 'mp4'), l[1]))
            else:
                # 得到的链接中会多含一个-list，需要去除掉
                url = os.path.split(l[0])
                filename = url[1].split('-')
                real_url = os.path.join(url[0], filename[0]+'.flv') # 生成新的文件名，再与原路径结合起来
                #print "获取到视频: %s\t%s" % (l[1], real_url)
                vs.append((real_url, l[1]))

        return vs
    
    def play_page(self, page_list):
        '''单个视频页面链接列表'''
        video_list = []
        for page in page_list:
            p = self.get_video_url(page[0])
            video_list.append((p, page[1].decode('gb2312').encode('utf-8')))
        return video_list

    def down_file(self, vs):
        '''生成一个可执行的.sh文件'''

        f = open('video.sh', 'w')
        for v in vs:
            filename = "%s%s" % (v[1], os.path.splitext(v[0])[1])
            cmd = 'wget -c -O %s %s\n' % (filename, v[0])
            f.write(cmd)
        print '下载文件已生成，在Linux中，你可以执行 sh video.sh 开始下载!'
        f.close()

def main():
    oc = OpenClass(TED_URL)
    
    html = oc.get_html(oc.url)
    page_list = oc.get_ted_page(html)
    page = oc.play_page(page_list)
    vs = oc.filter_url(page)
    oc.down_file(oc.video(vs))

if __name__ == '__main__':
    main()

