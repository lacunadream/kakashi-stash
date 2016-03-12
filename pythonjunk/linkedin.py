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
	
