import logging
import threading
import requests
import bs4
import random
import json



logging.basicConfig(level = logging.ERROR)

rootURLS = [
'https://www.linkedin.com/in/fong-tuan-chen-66645836',
"https://www.linkedin.com/in/evonnechenmayyie", 
'https://www.linkedin.com/in/ericleongyittan', 
'https://www.linkedin.com/in/jef0194758292',
'https://www.linkedin.com/in/nicholas-tan-check-foong-460112b0'
]

# with open('useragents.txt') as f:
# 	ua = f.readlines()

ua = [line.rstrip('\n') for line in open('useragents.txt')]


def randomUA():
	x = random.randint(0,657)
	return x

def f7(seq):
    seen = set()
    seen_add = seen.add
    return [x for x in seq if not (x in seen or seen_add(x))]

def getLocality(source):
	s = source.find("span", {"class":"locality"})
	s = s.contents
	return s

# def getID(source):
# 	x = source.find("div", {"class":"masthead"})
# 	# x = x['id']
# 	return x

def getName(source):
	x = source.find("h1", {"class":"fn"})
	x = x.contents
	return x


master = {}
track = []
# def save(master):

def dropList(x):
	return ''.join(x)

def scrapStart(base):
	randUA = random.randint(0,657)
	headers = {
		'User-Agent' : ua[randUA]
	}
	try: 
		print(base)
		r = requests.get(base, headers=headers)
		source = bs4.BeautifulSoup(r.content, "lxml")
		k = source.find("div", {"class":"browse-map"})
		k = k.findAll('a')
		k = [x['href'] for x in k]
		k = f7(k)

		loc = getLocality(source)
		loc = dropList(loc)
		base = dropList(base)
		name = getName(source)
		name = dropList(name)

		try: 
			title = source.find("p", {"class":"headline title"})
			title = title.contents
			title = dropList(title)
		except:
			title = "N/A"

		track.append(base)
		d = {
			name: {
				"location": loc,
				"link": base, 
				"title": title
			}
		}

		master.update(d)
		print(len(master))

		if (len(master) % 10 == 0):
			with open('linkedinscrap_pia.json', 'w') as outfile:
				json.dump(master, outfile)

		for x in k:
			if x not in track:
				scrapStart(x)
			else: 
				pass
	except:
		print('##switch###')
		lol = random.randint(0,len(track) - 1)
		kk = track[lol]
		scrapStart(kk)


threads = []

for x in rootURLS:
	t = threading.Thread(target=scrapStart, args=(x,))
	threads.append(t)

for x in threads:
	x.start()


