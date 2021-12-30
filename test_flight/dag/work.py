from dag import Workflow
import gevent
import time

w = Workflow(name="demo")
start_t = time.time()


def sleep_print(msg):
    def func(*_):
        gevent.sleep(1)
        print(f"{msg} DONE in {time.time()-start_t}")

    return func


w.add_task(id="1", deps=[], func=sleep_print("1"))
w.add_task(id="2", deps=["1"], func=sleep_print("2"))
w.add_task(id="3", deps=["1"], func=sleep_print("3"))
w.add_task(id="4", deps=["2", "3"], func=sleep_print("4"))
w.execute(check=False)