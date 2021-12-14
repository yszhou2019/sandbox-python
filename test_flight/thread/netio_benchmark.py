import gevent
from gevent import monkey
monkey.patch_all()
import requests
import time
from threading import Thread
from multiprocessing import Process
import numpy as np

_head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36'}
url = "http://www.tieba.com"
def http_request():
    try:
        webPage = requests.get(url, headers=_head)
        html = webPage.text
        return {"context": html}
    except Exception as e:
        return {"error": e}

def test_single_process():
    # 网络请求密集型操作，重复10次，单次io平均耗时
    t = time.time()
    for x in range(10):
        http_request()
    print("Line Http Request", (time.time() - t) / 10)

def test_multithread_netio():
    # 10线程并行 loop 100 times
    cost = []
    for i in range(100):
        threads = []
        t = time.time()
        for x in range(10):
            thread = Thread(target=http_request)
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()
        cost.append(time.time() - t)
    print("Multithread Http Request", np.mean(cost))

def test_mp_netio():
    # 10进程并行 loop 100 times
    cost = []
    for i in range(100):
        processes = []
        t = time.time()
        for x in range(10):
            process = Process(target=http_request)
            processes.append(process)
            process.start()

        for process in processes:
            process.join()
        cost.append(time.time() - t)
    print("Multiprocess Http Request", np.mean(cost))

def test_let_netio():
    # 10协程并行 loop 100 times
    cost = []
    for i in range(100):
        httprs = []
        t = time.time()
        httprs=[gevent.spawn(http_request) for i in range(10)]
        gevent.joinall(httprs)
        cost.append(time.time() - t)
    print("Gevent Http Request", np.mean(cost))

if __name__ == '__main__':
    test_single_process()
    test_multithread_netio()
    test_mp_netio()
    test_let_netio()