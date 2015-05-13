#!/usr/bin/env python
# -*- coding: utf-8 -*-
# wwq @ 2013-09-28 21:20:36

import os
import sys
import time
import subprocess

reload(sys)
sys.setdefaultencoding('utf-8')

USER = 'root'
PASSWD = '123'
HOST = 'localhost'
BACKUP = '/home/wyatt/backup'
DB_CHARSET = 'utf8'

filetamp = time.strftime('%Y-%m-%d_%Hh%Mm')

def db_name():
    p = subprocess.Popen("mysql -u%s -p%s -h%s --silent -N -e 'show databases'"\
            % (USER, PASSWD, HOST),
            shell=True,
            stdout=subprocess.PIPE)
    return p.stdout.readlines()

def backup(db_name_list):
    for db in db_name_list:
        db = db.strip()
        if db == 'information_schema':
            continue
        if not os.path.exists(os.path.join(BACKUP, db)):
            os.mkdir(os.path.join(BACKUP, db))
        filename = '%s/%s/%s-%s.sql' % (BACKUP, db, db, filetamp)
        cmd = 'mysqldump -u%s -p%s -h%s --default_character-set=%s -e --opt -c %s | gzip -c > %s.gz'\
                % (USER, PASSWD, HOST, DB_CHARSET, db, filename)
        print '开始备份数库: %s' % db
        subprocess.call(cmd, shell=True)
        print '%s 数据备份成功！' % db
        print '*' * 64

def main():
    db_name_list =  db_name()
    backup(db_name_list)

if __name__ == '__main__':
    main()

