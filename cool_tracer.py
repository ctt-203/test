#!/usr/bin/env python
# coding: utf-8

from sys import monitoring

depth = 0
def on_start(code, offset):
    global depth
    depth += 1
    prefix = depth * ">"
    print(f"{prefix} entering {code.co_name}")

def on_return(code, offset, retval):
    global depth
    prefix = depth * "<"
    depth -= 1
    print(f"{prefix} leaving {code.co_name}, return value: {retval}")

ID = 0
monitoring.use_tool_id(ID, "cool")
monitoring.register_callback(ID, monitoring.events.PY_START, on_start)
monitoring.register_callback(ID, monitoring.events.PY_RETURN, on_return)

def trace(func):
    def inner(*args, **kwargs):
        monitoring.set_local_events(ID, func.__code__, monitoring.events.PY_START|
                                      monitoring.events.PY_RETURN)
        return func(*args, **kwargs)
    return inner

    
@trace
def fib(i):
    if i <= 2:
        return 1
    else:
        return fib(i-1) + fib(i-2)

fib(5)
monitoring.free_tool_id(ID)