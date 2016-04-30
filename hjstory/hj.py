import requests
import bs4
import re
# import grequests
import threading
import logging

# from urllib import urlretrieve
import urllib.request

baseURL = "http://www.hj-story.com/story-begins/"

def fileName(extract):
	extract = str(extract)
	asd = "D:/HJStory/" + extract + ".jpg"
	return asd

def imageSave(soup, counter):
	imageArea = soup.find("div", {"class" : "blog-content"})
	imageArea = imageArea.find("img")
	imageUrl = imageArea["src"]
	k = urllib.request.urlretrieve(imageUrl, fileName(counter))
	# print(imageArea)
	print(k)

def openPage(link, counter):
	r = requests.get(link)
	soup = bs4.BeautifulSoup(r.content, "lxml")

	nextLink = soup.find("h3", {"class" : "next-post-title"})	
	nextLink = nextLink.find("a")
	nextLink = nextLink['href']

	counter = counter + 1
	imageSave(soup, counter)

	openPage(nextLink, counter)

counter = 0
openPage(baseURL, counter)

# CSS selectors?