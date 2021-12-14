import gevent
import sys
import urllib
import subprocess
import re

import urllib.request


def download(url):
    try:
        url_opener = urllib.request.urlopen(url)
    except Exception as e:
        print(f'open url{url} error, {e}')
        return

    if url_opener.code != 200:
        print(f'return code is:{url_opener.code}')
        return

    file_name = url[url.rfind('/') + 1 :]

    status_subprocess = subprocess.call(f'wget -c {url}', shell=True)

    if status_subprocess == 0:
        print(f'[{file_name}]:download complete!')
    else:
        print(f'[{file_name}]:download failed !')


'''
1 打开schedule.html
2 解析所有xxx.pdf文件名，生成对应的文件名的url -> 去重
3 多线程各自下载对应的文件名
'''


def parse(url):
    # type from bytes to string
    contents = urllib.request.urlopen(url).read().decode()
    key_pattern = re.compile(r'[a-z0-9_\-]*.pdf')
    vals = re.findall(key_pattern, contents)
    # dedup
    urls = list(set(vals))
    # concat
    # urls=[url+u for u in urls]
    urls = [
        'http://www.cs.cmu.edu/afs/cs/academic/class/15418-f18/www/lectures/' + u
        for u in urls
    ]
    return urls


if __name__ == '__main__':
    argc = len(sys.argv)
    if argc < 2:
        print('usage:%s <url> [url...]' % (sys.argv[0]))
        sys.exit(-1)

    urls = parse(sys.argv[1])
    jobs = [gevent.spawn(download, url) for url in urls]

    gevent.joinall(jobs)
