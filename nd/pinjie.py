#!/usr/bin/env python

import PIL.Image as Image
import os, sys
from down import get_range, base_dir

w = 85 * 512
h = 55 * 512

a = 512

toImage = Image.new('RGBA', (w, h))

for m in get_range(85):
    for n in get_range(55):
        fname = '%s_%s.jpg' % (n, m)
        fromImage = Image.open(base_dir+fname)
        i, j = int(m), int(n)
        toImage.paste(fromImage,((i-1)*a, (j-1)*a))

toImage.save('result.jpg')
