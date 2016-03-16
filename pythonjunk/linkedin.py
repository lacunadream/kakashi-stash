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
	s = dropList(s)
	return s

# def getID(source):
# 	x = source.find("div", {"class":"masthead"})
# 	# x = x['id']
# 	return x

def getName(source):
	x = source.find("h1", {"class":"fn"})
	x = x.contents
	x = dropList(x)
	return x

def getTitle(source):
	title = source.find("p", {"class":"headline title"})
	title = title.contents
	title = dropList(title)
	return title


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

		base = dropList(base)
		name = getName(source)


		try: 
			title = getTitle(source)
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

		if (len(master) % 10):
			with open('linkedinscrap_pia.json', 'w') as outfile:
				json.dump(master, outfile)

		def nextRandom():
			x = random.randint(0,len(k) -1)
			return x

		def nextLevel():
			r = nextRandom()
			print(k[r])
			if k[r] not in track:
				scrapStart(k[r])
			else:
				nextLevel()

		nextLevel()

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

