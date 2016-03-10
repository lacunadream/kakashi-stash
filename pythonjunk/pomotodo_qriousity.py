import requests
import bs4

url = "https://pomotodo.com/account#login"
data = {"username":"davidyong12@gmail.com","password":"","device":"web","offset":0,"timezone":"Europe/London"}

# r = requests.get(url)
# print(r.text)

# r = requests.post(url, params = data)
# print(r.text)

# r = requests.get(url, auth=('davidyong12@gmail.com', ''))
# print(r)

# appUrl = "https://pomotodo.com/app"
# r = requests.get(appUrl)
# print(r.content)

s = requests.Session()

data = {"email":"yourmom@gmail.com", "password":""}
data2 = "email=yourmom@gmail.com&password=&_csrf="



r = s.get("http://qriousity.com/login")
r = bs4.BeautifulSoup(r.content, "lxml")
k = r.find("input", {"name":"_csrf"})
k = k["value"]
data["_csrf"] = k
data2 = data2 + k
print(data)

r = s.post("http://qriousity.com/login", {"email":"yourmom@gmail.com", "password":"","_csrf":k})
print(r.text)




