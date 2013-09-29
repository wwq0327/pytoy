#!/usr/bin/env python
# -*- coding: utf-8 -*-
# wwq @ 2013-09-29 21:26:23

import re
import sys
import optparse
import datetime
import requests

reload(sys)
sys.setdefaultencoding('utf-8')

URL = 'http://www.yyets.com/tv/schedule'


class MeiJuMi:
    def __init__(self, url):
        self.url = url

    def month_end_day(self):
        now = datetime.datetime.today()
        year = now.year
        month = now.month
        if month == 12:
            end = datetime.date(year+1, 1, 1) - datetime.timedelta(days=1)
            return end.day
        else:
            end = datetime.date(year, month+1, 1) - datetime.timedelta(days=1)
            return end.day

    def get_day(self):
        today = datetime.datetime.today()
        return today.day

    def set_day_str(self, day=None):
        if not day:
            return str(self.get_day()) + '号'
        else:
            return str(day) + '号'

    def get_html(self):
        r = requests.get(self.url)
        if r.status_code == 200:
            return r.content
        else:
            return None
    
    def get_day_html(self, html, day):
        regex = r'<td class="ihbg">.+?<dt>%s</dt>(.+?)</dl>' % day
        re_day = re.compile(regex, re.DOTALL)
        m = re.findall(re_day, html)
        return m[0] 

    def get_jm_list(self, day_html):
        regex = r'<div class="floatSpan"><span>(.+?)<span></div>'
        re_jm = re.compile(regex, re.DOTALL)
        m = re.findall(re_jm, day_html)
        return m

def main():
    m = MeiJuMi(url=URL)
    p = optparse.OptionParser(description=u"YYETS每日美剧更新列表",
            version="0.1",
            usage="%prog [day]")
    p.add_option('--day', '-d')
    options, arguments = p.parse_args()
    end = m.month_end_day()
    if options.day:
        if len(arguments) == 0:
            day_num = int(options.day)
            if isinstance(day_num, int) and 1<=day_num<=end:
                day = m.set_day_str(day_num)
            else:
                print '输入的天数无效'
                p.print_help()
                sys.exit(1)
        else:
            p.print_help()
            sys.exit()
    else:
        day = m.set_day_str() 

    html = m.get_html()
    day_html = m.get_day_html(html, day)
    jm_list = m.get_jm_list(day_html)
    print '=' * 72
    print '%s的美剧节目有：' % day
    print '-' * 72
    for i in jm_list:
        print i
    print '=' * 72

if __name__ == '__main__':
    main()


