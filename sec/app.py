from flask import Flask
import bs4
import requests

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'
# https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001288776&type=10-K&dateb=&owner=exclude&count=40
@app.route('/search/<company_code>')
def get_sec(company_code):
	r = requests.get("https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001288776&type=10-K&dateb=&owner=exclude&count=40")
	print(r.text)
	return r.text


if __name__ == '__main__':
    app.run()