#!/usr/bin/python
# Copyright (c) 2009 Denis Bilenko. See LICENSE for details.
# gevent-test-requires-resource: network
"""Spawn multiple workers and wait for them to complete"""
from __future__ import print_function
import gevent
from gevent import monkey

# patches stdlib (including socket and ssl modules) to cooperate with other greenlets
monkey.patch_all()

import requests

# Note that we're using HTTPS, so
# this demonstrates that SSL works.
urls = [
    'https://www.google.com/',
    'https://www.apple.com/',
    'https://www.python.org/'
]


import time
def print_head(url):
    start_s=time.time()
    print('Starting %s' % url)
    data = requests.get(url).text
    print(f'{url}: {len(data)} {time.time()-start_s }')
    return 1

jobs = [gevent.spawn(print_head, _url) for _url in urls]

gevent.joinall(jobs)
for j in jobs:
    print(j.value)