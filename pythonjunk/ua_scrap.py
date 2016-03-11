import requests
import bs4
import logging

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
def indivPageScrap(link):
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

	return final

# putting everything together
for x in urls: 
	k = indivPageScrap(x)
	UALIST.extend(k)

print(UALIST)
f = open('useragents.txt', 'w')
f.write(UALIST)
f.close()




