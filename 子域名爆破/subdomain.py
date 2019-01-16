#!/usr/bin/python env
# -*- coding: UTF-8 -*-
##导入模块
import requests
import socket
import sys
import threading


def connect(hh,o):
    try:
        r = requests.get(hh, allow_redirects=False, timeout=0.1)
        httpcode = r.status_code
        s = socket.gethostbyname(o)
        if s: print "[+]ok " + hh, httpcode,s
    except requests.exceptions.RequestException:
        pass
def main():
    try:
        url = sys.argv[1]
        ll = sys.argv[2]
        aa = open(ll)
        for i in aa:
            a = i.strip('\n')
            p = "http://"+a + '.' + url
            oo = a + '.' + url
            connect(p,oo)
    except IndexError:
        print "use python subdomain.py xxx.com dic.txt"


if __name__=='__main__':
    main()
