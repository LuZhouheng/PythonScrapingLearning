# -*- coding: utf-8 -*-
# @Author: LuZhouheng
# @Date:   2016-05-28 21:32:44

import bs4
from bs4 import BeautifulSoup
import re # 引入 BeautifulSoup 和 re (解析器与正则表达式)


html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
""" # 所用来解析的html例子

soup = BeautifulSoup(html_doc,'html.parser',from_encoding='utf-8') # 声明 BeautifulSoup

print "get all link" # 找到所有 <a> 标签并打印
links = soup.find_all('a')
for link in links:
    print link.name, link['href'], link.get_text()

print "get lacie link href" # 找到 <a> 标签里特定的网址并打印
link_node = soup.find('a', href='http://example.com/lacie')
print link_node.name, link_node['href'], link_node.get_text()

print 'find by re-compile' # 利用正则表达式找到 <a> 标签里的包含 "ill" 字符的地址并打印
link_node = soup.find('a',href=re.compile(r"ill"))
print link_node.name, link_node['href'], link_node.get_text()

print 'find <p>' # 找到class 为 "title" 的 <p> 标签并打印
p_node = soup.find('p', class_="title")
print p_node.name, p_node.get_text()
