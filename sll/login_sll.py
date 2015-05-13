#!/usr/bin/env python
# -*- coding: utf-8 -*-
# wwq @ 2013-10-08 12:27:58

import subprocess
#import getpass 

USER = 'wyatt'
SSH_HOST = 'sociallearnlab.org'

def login_sll(host, user):
    cmd = 'ssh %s@%s' % (user, host)
    subprocess.call(cmd, shell=True)

def main():
    login_sll(SSH_HOST, USER)

if __name__ == '__main__':
    main()

