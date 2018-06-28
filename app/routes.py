from app import app
from flask import jsonify
import requests
from bs4 import BeautifulSoup
import pprint
pp = pprint.PrettyPrinter(indent=4)


@app.route('/')
def index():
    return 'Homepage'


@app.route('/hackernews_title', methods=['GET', 'POST'])
def hackernews_title():
    r = requests.get("https://news.ycombinator.com/")
    if r.status_code is 200:
        cards = r.content
        soup = BeautifulSoup(cards, 'lxml')
        trs = soup.find_all('tr', class_='athing')
        title = soup.find_all('a', class_='storylink')
        source = soup.find_all('span', class_='sitestr')
        news = []
        for i, item in enumerate(trs):
            obj = {}
            try:
                obj['title'] = title[i].text.strip()
                obj['source'] = source[i].text.strip()
                news.append(obj)
            except IndexError:
                news.append(obj)
        result = news
        return jsonify({"Hackernews Titles": result})
    else:
        return "NOT ALLOWED"
