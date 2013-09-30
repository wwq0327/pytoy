#!/usr/bin/env python
# -*- coding: utf-8 -*-
# wwq @ 2013-09-30 23:20:43

import paramiko

hostname = 'sociallearnlab.org'
port = 22
username = 'aaa'
password = 'aaa'

if __name__ == '__main__':
    paramiko.util.log_to_file('p.log')
    s = paramiko.SSHClient()
    s.load_system_host_keys()
    s.connect(hostname, port, username, password)
    stdin, stdout, stderr = s.exec_command('tail -f  /data/wwwlogs/access.log')
    print stdout.read()
    s.close()
