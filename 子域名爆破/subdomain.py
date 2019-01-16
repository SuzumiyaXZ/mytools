#!/usr/bin/python env
# -*- coding: UTF-8 -*-
##导入模块
import requests
import socket
import sys
import threading


def connect(hh,o):
    try:
        r = requests.get(hh, allow_redirects=False, timeout=0.1)  ##r等于请求p
        httpcode = r.status_code  ##httpcode变量获取状态码
        s = socket.gethostbyname(o)
        if s: print "[+]ok " + hh, httpcode,s
    except requests.exceptions.RequestException:
        pass
def main():
    try:
        url = sys.argv[1]  ##url赋值第一个命令行值
        ll = sys.argv[2]  ##ll复制第二个命令行值
        aa = open(ll)  ## aa变量等于打开 ll赋值的文件
        for i in aa:  ## 变量i遍历 aa文件
            a = i.strip('\n')  ## a赋值i换行一行一个
            p = "http://"+a + '.' + url  ##变量p拼接字符串与变量a+用户输入的url
            oo = a + '.' + url
            connect(p,oo)
    except IndexError:
        print "use python subdomain.py xxx.com dic.txt"


if __name__=='__main__':
    main()
