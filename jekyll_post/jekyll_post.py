import os, sys
from datetime import datetime

OUTPUT  = "./_posts"
CONTENT = '''---
layout: post
title:
description:
keywords:
---
'''

def post_name(title):
	_day = datetime.today()
	day = _day.strftime("%Y-%m-%d")
	filename = day + "-" + title + ".markdown"
	return filename

def write_to_file(filename):
	_f = os.path.join(OUTPUT, filename)
	f = open(_f, "w")
	try:
		f.write(CONTENT)
	except IOError, e:
		print e
		sys.exit(0)
	finally:
		f.close()

def main():
	if len(sys.argv) != 2:
		print "Usage: %s <post tilte>\n" % sys.argv[0]
		sys.exit(1)

	title = sys.argv[1]
	filename = post_name(title)
	write_to_file(filename)

if __name__ == '__main__':
	main()
