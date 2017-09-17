#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib2
import httplib
import os
import io
import time
import ssl
ssl.match_hostname = lambda cert, hostname: True

def request(url):
    try:
        request = urllib2.Request(url)
        response = urllib2.urlopen(request)
        print "Status response " + str(response.info())
        page = response.read()
    except httplib.IncompleteRead, e:
        page = e.partial

    return page

def write_to_file(json):
    file_nm = "scheme" + str(int(time.time())) + ".json"
    with open(file_nm, "w") as text_file:
        text_file.write(json)

if __name__ == '__main__':
    import sys
    if len(sys.argv) != 2:
        print("[*] rose_get.py <url>")
    else:
        print('[*] Buscar scheme mockaroo')
        url = sys.argv[1]
        print("Consultar [*]: %s\n" % url)
        for i in range(1000):
            json = request(url)
            write_to_file(json)
