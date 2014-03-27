#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import Image

size = 128, 128

for infile in os.listdir('.'):
    outfile = os.path.splitext(infile)[0]+".thumbnail.jpg"
    if infile != outfile:
        try:
            im = Image.open(infile)
            im.thumbnail(size)
            im.save(os.path.join('/tmp/', outfile), "JPEG")
        except IOError:
            print "cannot create ghumbnail for ", infile



