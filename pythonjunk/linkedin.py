import logging
import threading
import requests
import bs4
import random


logging.basicConfig(level = logging.ERROR)

rootURL = "https://www.linkedin.com/in/ashsingh"

# with open('useragents.txt') as f:
# 	ua = f.readlines()

ua = [line.rstrip('\n') for line in open('useragents.txt')]
randUA = random.randint(0,657)

def randomUA():
	x = random.randint(0,657)
	return x

def f7(seq):
    seen = set()
    seen_add = seen.add
    return [x for x in seq if not (x in seen or seen_add(x))]


kk = ua[randUA]
print(ua[randUA])
headersX = {
	'User-Agent' : ua[randUA]
}
	
r = requests.get(rootURL, headers=headersX)
source = bs4.BeautifulSoup(r.content, "lxml")

print(r.text)
def getLocality(source):
	s = source.find("span", {"class":"locality"})
	s = s.contents
	return s

def getID(source):
	x = source.find("div", {"class":"masthead"})
	# x = x['id']
	return x

k = source.find("div", {"class":"browse-map"})
k = k.findAll('a')
k = [x['href'] for x in k]
k = f7(k)
s = getLocality(source)
x = getID(source)
print(x)

