import time
from multiprocessing import  Pool
from pebble import ProcessPool
from concurrent.futures import TimeoutError

def foo(num ):
    time.sleep(10)
    return num+1

#
# p=Pool(20)
# res= p.map(foo, [i for i in range(40)])
#
# print(res)
# res= p.map(foo, [i for i in range(100)])
#
# print(res)

def mp_test():
    p=Pool(10)
    start=time.time()
    jobs=p.map_async(foo, range(10))
    p.close()
    # jobs.wait(timeout=1.0)
    try:
        res=jobs.get(timeout=2)
        end=time.time()
        print(end-start)
        print(res)
    except Exception as e:
        print('timeout')
        p.terminate()
    p.join()
    time.sleep(100)

def pebble_test():
    start=time.time()
    with ProcessPool(10) as p:
        jobs=p.map(foo,args=range(10),timeout=1)
    try:
        res=jobs.result()
        print(res)
        print(time.time()-start)
    except Exception as e:
        print(e)

# mp_test()
# pebble_test()


import functools
import signal


def timeout(sec):
    """
    timeout decorator
    :param sec: function raise TimeoutError after ? seconds
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapped_func(*args, **kwargs):

            def _handle_timeout(signum, frame):
                err_msg = f'Function {func.__name__} timed out after {sec} seconds'
                raise TimeoutError(err_msg)

            signal.signal(signal.SIGALRM, _handle_timeout)
            signal.alarm(sec)
            try:
                result = func(*args, **kwargs)
            finally:
                signal.alarm(0)
            return result

        return wrapped_func
    return decorator


@timeout(3)
def slow_func(i):
    time.sleep(10)
    return i+1

# p=Pool(10)
# res= p.map(slow_func, range(10))
# print(res)

with Pool(10) as p:
    try:
        res=p.map(slow_func, range(10))
        print(res)
    except TimeoutError:
        print('timeout')

time.sleep(100)