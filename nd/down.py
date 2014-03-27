#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#By Lerry http://lerry.org
#

import os
import urllib

base_dir = os.path.join(os.getcwd(), 'imgs/')
url = 'http://nd.oeeee.com/images/ztpics/yixiangsu/list/20120306lhhc/zhx.tiles/l7/'

def get_range(n):
    temp = range(1, n+1)
    result = []
    for i in temp:
        i = str(i)
        if len(i) == 1:
            result.append('0' + i)
        else:
            result.append(i)

    return result

def down_one(url, name):
    if not os.path.exists(name):
        pic = urllib.urlopen(url).read()
        print 'Downloaded: ', name
        f = open(name, 'wb')
        f.write(pic)
        f.close()

if __name__ == '__main__':
    for m in get_range(55):
        for n in get_range(85):
            fname = '%s_%s.jpg' % (m, n)
            print url+fname
            down_one(url+fname, base_dir+fname)

