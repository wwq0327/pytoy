#!/usr/bin/env python
# -*- coding: utf-8 -*-
#20个排序好的数组，每个数组500个数，按照降序排序好的，让找出500个最大的数。

import random

N = 500
M = 20

num_list = [[random.randint(0, 100000) for i in xrange(M)] for j in xrange(N)]

big_list = []
for i in num_list:
    big_list.extend(i)

big_list.sort()
a = big_list[-500:]
print a
