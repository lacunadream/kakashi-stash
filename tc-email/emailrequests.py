import requests
import time
import re
import logging
import threading

EMAILNAME = "d.s.yong12+"
EMAILDOMAIN = "@gmail.com"

for i in range(1970, 5000):
	email_string = EMAILNAME + str(i) + EMAILDOMAIN

	res = requests.post('http://lifeatwork.my/lifeatwork-2016/submit/?c=14', data = {'email': email_string})

	print("Sending invite to " + email_string)
	# re.compile('table')
	# asd = re.search('table', res.text)
	# if asd is not None: 
	# 	print(asd.group(0))
	# 	print("gg")
	# 	break 

	time.sleep(1)

	if res.status_code != 200:
		print("request failed " + str(res.status_code))
	else: 
		print("success!")
		# time.sleep(1000)
		# res = requests.post('http://lifeatwork.my/lifeatwork-2016/submit/?c=14', data = {'email': email_string})

	# print("success!")


# def sendEmail(x):
# 	email_string = EMAILNAME + str(x) + EMAILDOMAIN 
# 	res = requests.post('http://lifeatwork.my/lifeatwork-2016/submit/?c=14', data = {'email': email_string})
# 	print("Sending invite to " + email_string)

# 	while res.status_code != 200: 
# 		print("request failed " + str(res.status_code))
# 		time.sleep(1000)
# 		res = requests.post('http://lifeatwork.my/lifeatwork-2016/submit/?c=14', data = {'email': email_string})


# for i in range(35, 5000):
# 	t = threading.Thread(target=sendEmail, args=(i,))
# 	t.start()
