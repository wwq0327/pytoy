#!/usr/bin/env python
# -*- coding: utf-8 -*-
# wwq @ 2013-10-09 20:44:58

# 批量下载百度mp3 Top500 歌曲

import re
import sys
import os
import urllib
import time

try:
    import requests
except:
    print 'Please install requests lib'
    sys.exit(1)

MP3_BASE_URL = 'http://music.baidu.com/song'
TOP_URL = 'http://music.baidu.com/top/dayhot'

class DownloadBaiduMp3:
    def __init__(self, path):
        self.path = path

    def get_html(self, url):
        headers = {
                'User-Agent': "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.76 Safari/537.36" 
                }

        r = requests.get(url, headers=headers)
        if r.status_code == 200:
            return r.content
        else:
            return None

    def get_mp3_num(self, html):
        #mp3_num_list = []
        #regex = r'{"sid":"(.+?)","author":"(.+?)","sname":"(.+?)"}'
        regex = r'<a href="/song/(\d+)" title=".+?">(.+?)</a>'
        p = re.compile(regex, re.DOTALL)
        mp3_num_list = p.findall(html)
        return mp3_num_list
    
    def get_mp3_url(self, mp3_list):
        '''得到MP3的下载链接
        mp3_list格式为('num', 'name')
        '''
        url = '%s/%s/download' % (MP3_BASE_URL, mp3_list[0])
        html = self.get_html(url)
        print html
        #regex = r'<a data-btndata="{"ids":".+?",type="song"}" href="(.+?)" id="128".+?'
        regex = r'.+?id="96".+?<a data-btndata=\'{"ids":"\d+","type":"song"}\'  href="/data/music/file\?link=(.+?)"  id="128".+?'
        p = re.compile(regex, re.DOTALL)
        down_url = p.findall(html)
        print down_url
        return (down_url[0], mp3_list[1])

    def down_call(self, count, size, total_filesize):
        '''下载进程显示'''
        per = 100.0 * count * size / total_filesize
        if per > 100:
            per = 100
        process = '已下载 %d KB(%.2f' % (count*size/1024, per)+"%)\n"
        sys.stdout.write(process)
        sys.stdout.flush()
        time.sleep(0.2)

    def down_mp3(self, down_list):
        '''下载mp3'''
        url, sname = down_list
        filename = sname+".mp3"
        urllib.urlretrieve(url, filename, self.down_call)


def main():
    top = DownloadBaiduMp3(".")
    html = top.get_html(TOP_URL)
    mp3_nums = top.get_mp3_num(html)
    print mp3_nums
    for num in mp3_nums:
        down = top.get_mp3_url(num)
        #top.down_mp3(down)

if __name__ == '__main__':
    main()
