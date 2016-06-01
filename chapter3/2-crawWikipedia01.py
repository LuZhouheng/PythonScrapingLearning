from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

pages = set()
def getLinks(pageUrl):
	global pages
	html = urlopen("http://en.wikipedia.org" + pageUrl)
	bsObj = BeautifulSoup(html, "html.parser")
	for link in bsObj.findAll("a", href=re.compile("^(/wiki/)")):
		if 'href' in link.attrs:
			if link.attrs['href'] not in pages:
				# 我们遇到了新画面
				newPage = link.attrs['href']
				print(newPage)
				pages.add(newPage)
				getLinks(newPage)

getLinks("")


#Python 默认的递归限制（程序递归地自我调用次数）是 1000 次。
#因为维基百科的网络链接浩如烟海，所以这个程序达到递归限制后就会停止，除非你设置一个较大的递归计数器，或用其他手段不让它停止。
