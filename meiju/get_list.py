#!/usr/bin/env python
# -*- coding: utf-8 -*-
# wwq @ 2013-09-26 22:30:40

import re
import sys
import optparse
import datetime
#from datetime import datetime
import requests

#reload(sys)
#sys.setdefaultenconding('utf-8')

URL = 'http://www.yyets.com/tv/schedule'

def month_end_day():
    '''
    获取本月最后一天的天数'''

    now = datetime.datetime.today()
    year = now.year
    month = now.month
    if month == 12:
        end = datetime.date(year+1, 1, 1) - datetime.timedelta(days=1)
        return end.day
    else:
        end = datetime.date(year, month+1, 1) - datetime.timedelta(days=1)
        #print type(end.day)
        return end.day

def get_day():
    today = datetime.datetime.today()
    return today.day

def set_day_str(day=False):
    if not day:
        return str(get_day()) + '号'
    else:
        return str(day) + '号'

def get_html(url):
    r = requests.get(url)
    print '正在读取的页面地址：', url
    if r.status_code == 200:
        return r.content
    else:
        return None

def get_day_html(html, day):
    regex = r'<td class="ihbg">.+?<dt>%s</dt>(.+?)</dl>' % day
    re_day = re.compile(regex, re.DOTALL)
    m = re.findall(re_day, html)
    return m[0] 

def get_jm_list(day_html):
    regex = r'<div class="floatSpan"><span>(.+?)<span></div>'
    re_jm = re.compile(regex, re.DOTALL)
    m = re.findall(re_jm, day_html)
    return m

def main():
    p = optparse.OptionParser(description=u"YYETS每日美剧更新列表",
            version="0.1",
            usage="%prog [day]")
    p.add_option('--day', '-d')
    options, arguments = p.parse_args()
    end = month_end_day()
    if options.day:
        if len(arguments) == 0:
            day_num = int(options.day)
            if isinstance(day_num, int) and 1<=day_num<=end:
                day = set_day_str(day_num)
            else:
                print '输入的天数无效'
                p.print_help()
                sys.exit(1)
        else:
            p.print_help()
            sys.exit()
    else:
        day = set_day_str() 

    html = get_html(URL)
    day_html = get_day_html(html, day)
    jm_list = get_jm_list(day_html)
    print '%s的美剧节目有：' % day
    print '=' * 64
    for i in jm_list:
        print i

if __name__ == '__main__':
    main()

