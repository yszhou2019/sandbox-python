import gevent
from gevent import monkey
monkey.patch_all()
import requests
import time

_head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36'}
url = "http://www.tieba.com"
def http_request():
    try:
        webPage = requests.get(url, headers=_head)
        html = webPage.text
        return {"context": html}
    except Exception as e:
        return {"error": e}

def test_let_netio():
    # 10协程并行
    httprs = []
    t = time.time()
    httprs=[gevent.spawn(http_request) for i in range(10)]
    gevent.joinall(httprs)
    print("Gevent Http Request", time.time() - t)

if __name__ == '__main__':
    test_let_netio()