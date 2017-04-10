# -*- coding: utf-8 -*-

import urllib2
import random
import lxml.html
import telnetlib
import requests

url = "http://www.ip181.com/"
ips = ['121.40.108.76']
ip_list = []
# ip = random.choice(ips)#'5.2.69.103:1080'
# proxy_support = urllib2.ProxyHandler({'http':ip})
#参数是一个字典{'类型':'代理ip:端口号'}
# opener = urllib2.build_opener(proxy_support)
#定制opener
# opener.add_handler=[('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36')]
#add_handler给加上伪装
# urllib2.install_opener(opener)
try:
    response = urllib2.urlopen(url,timeout=8)
except:
    print '抓ip出错'
else:
    html = response.read().decode('gbk')
    tree = lxml.html.fromstring(html)
    # fixed_html = lxml.html.tostring(tree, pretty_print=True)
    # print fixed_html
    trs = tree.cssselect('table.table tr')
    for index,tr in enumerate(trs):
        if index == 0:
            continue
        ip_spare = tr.cssselect('td')[0].text_content()
        port_spare = tr.cssselect('td')[1].text_content()
        ips.append(ip_spare+':'+port_spare)
    for ip in ips:
        try:
            requests.get('https://baidu.com/', proxies={"http":ip})
        except:
            print 'ip不可用'
            continue
        print 'ip可用'
        ip_list.append(ip)
        print ip_list
    ip = random.choice(ip_list)
    print ip
    proxy_support = urllib2.ProxyHandler({'http': ip})
    opener = urllib2.build_opener(proxy_support)
    opener.add_handler = [('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36')]
    urllib2.install_opener(opener)
    try:
        response = urllib2.urlopen('http://bj.lianjia.com/chengjiao/dongcheng/', timeout=20)
    except:
        print '链接出错'
    html = response.read().decode('utf-8')
    print html
    tree = lxml.html.fromstring(html)
    lis = tree.cssselect('ul.listContent li')
    for li in lis:
        print li.cssselect('div.info div.title a')[0].text_content()