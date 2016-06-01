# -*- coding: utf-8 -*-
# @Author: LuZhouheng
# @Date:   2016-05-28 21:32:44
# @Last modified by:   ChowHungLou
# @Last Modified time: 2016-05-28 21:43:03

import urllib.request
import http.cookiejar
import urllib.response

print('*'*80,'第一种方法')
url = "http://www.baidu.com"
response1 = urllib.request.urlopen(url)
print (response1.getcode());
print (len(response1.read())) #打印网页内容的长度


print('*'*80,'第二种方法')
request = urllib.request.Request(url)
request.add_header("user-agent", "Mozilla/5.0")
response2 = urllib.request.urlopen(request)
print(response2.getcode())
print(len(response2.read()))


print('*'*80,'第三种方法')
cj = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
urllib.request.install_opener(opener)
response3 = urllib.request.urlopen(url)
print(cj)
print(opener)
print(response3.getcode())
print(len(response3.read()))
