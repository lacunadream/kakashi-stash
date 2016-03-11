import requests
import bs4
import logging
import threading

# GLOBALS
baseURL = 'https://udger.com'
logging.basicConfig(level =logging.DEBUG)
UALIST = []

# INTIAL URLs GRAB
r = requests.get("https://udger.com/resources/ua-list")
soup = bs4.BeautifulSoup(r.content, "lxml")

name = soup.findAll("td")
name = [x.find("a") for x in name]
# print(name)
out = []
for x in name: 
	try:
		if x.find('href') != -1:
			out.append(x)
	except: 
		pass

out = out[1:193]
urls = [x['href'] for x in out]
print(urls)
print(type(urls), type(out))

# individual page method
def indivPageScrap(link, UALIST):
	r = requests.get(baseURL + link)
	soup = bs4.BeautifulSoup(r.content, "lxml")

	data = soup.findAll("p")
	data = [x.find("a") for x in data]
	data = [x.contents for x in data]
	# buggy p tag
	data = data[:(len(data)-1)]
	final =[]
	for x in data: 
		x = ','.join(x)
		final.append(x)

	UALIST.extend(final)
	
# putting everything together (non threading)
# for x in urls: 
# 	k = indivPageScrap(x)
# 	UALIST.extend(k)

# threading method
threads = []

for x in urls: 
	t = threading.Thread(target=indivPageScrap, args=(x, UALIST))
	threads.append(t)

for x in threads:
	x.start()

for x in threads:
	x.join()


print('###########', UALIST)
print(len(UALIST))
f = open('useragents.txt', 'w')
for agent in UALIST:
	f.write("%s\n" % agent)
f.close()


## :) Done

