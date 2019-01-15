#!/usr/bin/python env
# -*- coding: UTF-8 -*-
import requests
import socket
import sys
def domain():
    try:
        url = sys.argv[1]

        ll = sys.argv[2]
        aa = open(ll)
        for i in aa.readlines():
            a = i.strip('\n')
            p = 'http://'+a+'.'+url 
            o = a+'.'+url
            try:
               r = requests.get(p, allow_redirects=False,timeout=0.1)
               s = socket.gethostbyname(o)
               httpcode = r.status_code 
               if httpcode == 200:
                   print "[+]ok "+a+'.'+url,httpcode,"IP:"+str(s)
            except requests.exceptions.RequestException:
                None
    except IndexError:
        print "Use: python subdomain.py xxx.com dic.txt"

if __name__=='__main__':
    domain()


