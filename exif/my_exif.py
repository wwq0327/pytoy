#!/usr/bin/env python
# -*- coding: utf-8 -*-
# wwq @ 2013-09-11 09:13:01

from PIL import Image
from PIL.ExifTags import TAGS

def get_exif(fn):
    ret = {}
    i = Image.open(fn)
    info = i._getexif()
    for tag, value in info.items():
        decoded = TAGS.get(tag, tag)
        ret[decoded] = value
    return ret

if __name__ == '__main__':
    fn = '/home/wyatt/ddd.jpg'
    d = get_exif(fn)
    print type(d)
    for k, v in  d.items():
        print '%s\t%s' % (k, v)


