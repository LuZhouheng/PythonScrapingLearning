from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://en.wikipedia.com/wiki/Kevin_Bacon")
# html = urlopen("http://baike.baidu.com/view/5711166.htm")
bsObj = BeautifulSoup(html,"html.parser")
for link in bsObj.findAll("a"):
	if 'href' in link.attrs:
		print(link.attrs['href'])
