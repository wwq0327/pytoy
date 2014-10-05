#!/usr/bin/env python

def gen(fun):
	def _():
		print "111"
		fun()
		print "111"
	return _

@gen
def hello():
	print "hello"

if __name__ == '__main__':
	hello()