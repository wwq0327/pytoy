#!/usr/bin/env python
# -*- coding: utf-8 -*-
# wwq @ 2013-10-04 09:56:01

import gevent
from gevent import monkey
monkey.patch_all()

urls = ['http://www.google.com', 'http://www.yahoo.com', 'http://www.baidu.com']

import urllib2

def print_head(url):
    print 'starting %s' % url
    data = urllib2.urlopen(url).read()
    print '%s: %s bytes: %r' % (url, len(data), data[:50])

jobs = [gevent.spawn(print_head, url) for url in urls]
gevent.joinall(jobs)


