#!/usr/bin/env python

import locale
import os
import pprint

print 'Environment settings:'
for env_name in ['LC_ALL', 'LC_CTYPE', 'LANG', 'LANGUAGE']:
    print "\t%s = %s" % (env_name, os.environ.get(env_name, ''))

print
print 'Default locale:', locale.getdefaultlocale()
locale.setlocale(locale.LC_ALL, '')
print 'Frome environment:', locale.getlocale()
pprint.pprint(locale.localeconv())
