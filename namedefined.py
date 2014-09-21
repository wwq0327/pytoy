#!/usr/bin/env python

def is_name(name):
    try:
        name
    except NameError:
        return False
    else:
        return True

if __name__ == '__main__':
    a = 1
    if is_name(a):
        print "haha"
    else: 
        print "heihei"
    
