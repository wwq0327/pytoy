#!/usr/bin/env python

import re
from subprocess import Popen, PIPE

class DiskMonitor():
    def __init__(self,
            pattern="2[0-9]%",
            message="CAPACITY WARNING",
            cmd="df -h"):
        self.pattern = pattern
        self.message = message
        self.cmd = cmd

    def disk_space(self):
        ps = Popen(self.cmd, shell=True, stdout=PIPE, stderr=PIPE)
        output_lines = ps.stdout.readlines()
        for line in output_lines:
            line = line.strip()
            if re.search(self.pattern, line):
                print "%s %s" % (self.message, line)

if __name__ == '__main__':
    d = DiskMonitor()
    d.disk_space()

