#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Python格式输出

# 
print "hello, {}".format('wyatt')

# 自动编号，第一个参数为0，第二个参数为1，有点列表的意思
# s[0]=1, s[1]=2
print "{0} and {1} and {0}".format(1, 2)

print "三位划分来输出:{0:,}".format(1234567890)
print "三位划分来输出，带两位小数:{0:,.2f}".format(123456.7890)

import sys

print "{0.platform}".format(sys)

print "{0[name]}".format({"name":"wyatt"})
