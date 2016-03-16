import requests
import bs4

root = "http://www.cs.cmu.edu/~ninamf/courses/601sp15/"
r= requests.get('http://www.cs.cmu.edu/~ninamf/courses/601sp15/lectures.shtml')
# print(r.text)
source = bs4.BeautifulSoup(r.content, "lxml")



k = source.findAll("td", {"style":"text-align: center;"})
k = [x.find('a') for x in k]
out = []
for x in k: 
	try:
		if x.find('href') != -1:
			out.append(x)
	except: 
		pass
# print(out)

urls = [x['href'] for x in out]
print(urls)

def filename(url):
	k = url.split('/')
	return k

# for x in urls:
# 	if x.find('http') != -1:
# 		r = requests.get(root + x)
# 		zzz = filename(x)
# 		f = open(zzz[1], 'wb')
# 		f.write(r.content)
# 		f.close
# 		print('done', zzz)
# 	else:
# 		print('gg')

final = []
for x in urls:
	x = root + x
	final.append(x)

print(final)

f = open('ml_download.txt', 'w')
for x in final:
	f.write(x + ",")
f.close()

