from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

# html = urlopen("http://www.pythonscraping.com/pages/page1.html")
try:
	html = urlopen("http://www.pythonscraping.com/pages/page1.html")	
except HTTPError as e:
	print(e)

else:
if html is None:
	print("URL is not found")

else:

bsObj = BeautifulSoup(html.read(), "html.parser")

print(bsObj.h1)

#print(bsObj.html.body.h1)
#print(bsObj.body.h1)
#print(bsObj.html.h1)
 