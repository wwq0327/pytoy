#!/usr/bin/evn python
# -*- coding: utf-8 -*-

import pxssh
import getpass

try:
    s = pxssh.pxssh()
    passwd = getpass.getpass('password: ')
    s.login('joinwee.com', 'wyatt', passwd)
    s.sendline('uptime')
    s.prompt()
    print s.before

    s.sendline('df -h')
    s.prompt()
    print s.before

    s.logout()

except pxssh.ExceptionPxssh, e:
    print 'pxssh failed on login'
    print str(e)

