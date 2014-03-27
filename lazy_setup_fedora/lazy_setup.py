#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import urllib
import sys
import shutil
import subprocess

REPOS_URL = 'http://mirrors.163.com/.help/'
REPOS_FILES = ['fedora-163.repo', 'fedora-updates-163.repo']

def reporthook(*a): print a

def repos_exist():
    '''判断repo是否已存在'''

    #repos_files = ['fedora-163.repo', 'fedora-updates-163.repo']
    for repos in REPOS_FILES:
        return os.path.exists(repos)

def downrepos(url, repos_file):
    '''下载repo文件'''

    print url, '->', repos_file
    urllib.urlretrieve(url, repos_file, reporthook)

def copy_repos():
    if repos_exist():
        shutil.copy('fedora-163.repo', '/tmp/')
        shutil.copy('fedora-updates-163.repo', '/tmp/')
    else:
        sys.exit(1)

def yum_cache_and_update():
    subprocess.call('yum', 'makecache', shell=True)
    #subprocess.call('yum', 'check-update', shell=True)
    #subprocess.call('yum', '-y update', shell=True)

def main():
    if repos_exist():
        print 'repos 已存在'
    else:
        for repos in REPOS_FILES:
            downrepos(REPOS_URL, repos)
    copy_repos()

    print '更新系统'
    yum_cache_and_update()


if __name__ == '__main__':
    main()
