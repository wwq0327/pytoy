#!/usr/bin/env python
# -*- coding: utf-8 -*-
# wwq @ 2013-10-04 17:09:41

# 自动备份nginx产生的log文件

import os
import shutil
import time
import subprocess
import tarfile

LOG_DIR = '/data/wwwlogs'
LOG_BACKUP_DIR = '/data/wwwlogs/logs'
LOGS = ['access.log', 'wiki_access.log']

def mv_file(filename):
    this_time = time.strftime('%Y-%m-%d_%Hh%Mm')
    if not os.path.exists(LOG_BACKUP_DIR):
        os.mkdir(LOG_BACKUP_DIR)
    log_file = os.path.join(LOG_DIR, filename)
    tar_filename = os.path.splitext(filename)[0]+'-'+this_time+'.tar.gz'
    new_log_file = os.path.join(LOG_BACKUP_DIR, tar_filename) 
    print '开始压缩备份文件...%s...' % new_log_file
    tar = tarfile.open(new_log_file, 'w:gz')
    print '备份文件压缩完成!'
    tar.add(log_file)
    tar.close()
    print '正在删除原日志文件: %s ...' % log_file
    os.remove(log_file)
    print '原日志文件已删除!'

def restart_nginx():
    print '开始重启nginx服务器...'
    subprocess.call('kill -HUP `cat /data/wwwlogs/nginx.pid`', shell=True)

    p = subprocess.Popen('ps -ef | grep nginx', 
            shell=True,
            stdout=subprocess.PIPE)
    print p.stdout.read()


def main():
    for filename in LOGS:
        mv_file(filename)

    restart_nginx()

if __name__ == '__main__':
    main()



