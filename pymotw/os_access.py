#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

print 'Testing:', __file__  #当前文件
print 'Exists:', os.access(__file__, os.F_OK)  # 文件是否存在
print 'Readable:', os.access(__file__, os.R_OK)  # 文件是否可读
print 'Writable:', os.access(__file__, os.W_OK)  # 文件是否可写
print 'Executable:', os.access(__file__, os.X_OK)  # 是否可执行
