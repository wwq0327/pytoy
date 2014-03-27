#!/usr/bin/env python

def greeter():
    print 'Hello'

def repeat(fn, times):
    for i in range(times):
        fn()

def print_call(fn):
    def fn_wrap(*args, **kwargs):
        print "Calling %s" % fn.func_name
        fn_wrap.func_name = fn.func_name
        return fn(*args, **kwargs)
    return fn_wrap

greeter = print_call(greeter)
repeat(greeter, 3)

print 'func real name:', greeter.func_name
