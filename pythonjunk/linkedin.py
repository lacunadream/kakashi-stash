import logging
import threading
import requests
import bs4
import random

logging.basicConfig(level = logging.ERROR)

rootURL = "https://www.linkedin.com/in/ashsingh"

with open('useragents.txt') as f:
	ua = f.readlines()

randUA = random.randint(0,657)

def randomUA():
	x = random.randint(0,657)
	return x
kk = ua[randUA]
print(ua[randUA])
headersX = {
	'User-Agent' : 'Mozilla/3.04 (compatible; NCBrowser/2.35; ANTFresco/2.17; RISC OS-NC 5.13 Laz1UK1309)'
}
	
r = requests.get(rootURL, headers=headersX)
source = bs4.BeautifulSoup(r.content, "lxml")
# print(r.text)
k = source.find("div", {"class":"browse-map"})
print(k)
