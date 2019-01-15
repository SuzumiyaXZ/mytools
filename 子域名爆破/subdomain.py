#!/usr/bin/python env
# -*- coding: UTF-8 -*-
##导入模块
import requests
import socket
import sys
def domain(): ##创建一个domain的函数
    try:
        url = sys.argv[1]  ##url赋值第一个命令行值

        ll = sys.argv[2]  ##ll复制第二个命令行值
        aa = open(ll)  ## aa变量等于打开 ll赋值的文件
        for i in aa.readlines(): ## 变量i遍历 aa文件
            a = i.strip('\n') ## a赋值i换行一行一个
            p = 'http://'+a+'.'+url ##变量p拼接字符串与变量a+用户输入的url
            o = a+'.'+url ##o与p一样
            try:
               r = requests.get(p, allow_redirects=False,timeout=0.1) ##r等于请求p
               s = socket.gethostbyname(o) ##s 获取o里的url（不加二级域名）
               httpcode = r.status_code ##httpcode变量获取状态码
               if httpcode == 200: ##判断 如果状态码为200
                   print "[+]ok "+a+'.'+url,httpcode,"IP:"+str(s)
            except requests.exceptions.RequestException:
                None
    except IndexError:
        print "Use: python subdomain.py xxx.com dic.txt"

if __name__=='__main__':
    domain()


