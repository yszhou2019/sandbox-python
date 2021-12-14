import gevent

def foo():
    return 0/1

def bar():
    return 1/0

a=gevent.spawn(foo)
b=gevent.spawn(bar)
try:
    gevent.joinall([a,b])
except Exception as e:
    print('hello')