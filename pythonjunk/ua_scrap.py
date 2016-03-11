import requests
import bs4
import logging

# GLOBALS
baseURL = 'https://udger.com'
logging.basicConfig(level =logging.DEBUG)

# r = requests.get("https://udger.com/resources/ua-list")
# soup = bs4.BeautifulSoup(r.content, "lxml")

# name = soup.findAll("td")
# name = [x.find("a") for x in name]
# # print(name)
# out = []
# for x in name: 
# 	try:
# 		if x.find('href') != -1:
# 			out.append(x)
# 	except: 
# 		pass


# out = out[1:193]
# urls = [x['href'] for x in out]
# print(urls)
# print(type(urls), type(out))


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




# r = requests.get(baseURL + '/resources/ua-list/browser-detail?browser=360 browser')
# soup = bs4.BeautifulSoup(r.content, "lxml")



# data = soup.findAll("p")
# logging.debug(data)
# data = [x.find("a") for x in data]
# logging.debug(data)
# data = [x.contents for x in data]
# logging.debug(data)
# data = data[:(len(data)-1)]
# logging.debug(data)
# final =[]
# for x in data: 
# 	x = ','.join(x)
# 	final.append(x)
# logging.debug(final)





