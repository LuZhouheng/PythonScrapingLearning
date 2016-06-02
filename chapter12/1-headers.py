import requests
from bs4 import BeautifulSoup

session = requests.Session()
headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebkit 537.36 (KHTML, like Gecko) Chrome", "Accepts":"text/html,application/xhtml+xml,application/xml; q=0.9,imagr/webp,*/*;q=0.8"}
url = "https://www.whatismybrowser.com/developers/what-http-headers-is-my-browser-sending"
req = session.get(url, headers=headers)

bsObj = BeautifulSoup(req.text, "lxml")
print(bsObj.find("table", {"class":"table-striped"}).get_text)
