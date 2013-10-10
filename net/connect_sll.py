#!/usr/bin/env python
# -*- coding: utf-8 -*-
# wwq @ 2013-10-10 22:12:04

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('sociallearnlab.org', 80))
print s.getsockname()
print s.getpeername()
