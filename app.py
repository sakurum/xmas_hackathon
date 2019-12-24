# coding: utf-8
from flask import *
import queue
import sys, os
import re
import urllib.request
from bs4 import BeautifulSoup

app = Flask(__name__)
q_1000 = queue.Queue()
q_5000 = queue.Queue()
q_10000 = queue.Queue()

def title(url):
    d = urllib.request.urlopen(url).read().decode('UTF-8')
    # htmlをBeautifulSoupでパース
    soup = BeautifulSoup(d, "html.parser")

    # タイトル要素の取得
    print(soup.title) # <title>アルゴリズム雑記</title>

    # タイトル要素の文字列を取得
    print(soup.title.string) # アルゴリズム雑記
    return soup.title.string

@app.route('/', methods=["GET", "POST"])
def index():
    return render_template('index.html')

@app.route('/present', methods=["GET", "POST"])
def present():
    if request.method == "POST":
        price = int(request.form["present_price"])
        presenting_URL = request.form["present_URL"]
        presented_URL = ""
        if price <=1000:
            q_1000.put(presenting_URL)
            presented_URL = q_1000.get()
        elif price <=5000:
            q_5000.put(presenting_URL)
            presented_URL = q_5000.get()
        else:
            q_10000.put(presenting_URL)
            presented_URL = q_10000.get()
        present_title = title(presented_URL)
        print(present_title)
        return render_template('present.html',present_URL = presented_URL,present_title = present_title)
    else:
        return redirect('/')

if __name__ == "__main__":
    # webサーバー立ち上げ
    q_1000.put("https://www.amazon.co.jp/%E6%A0%97%E5%8E%9F%E5%9C%92-%E3%83%91%E3%82%A6%E3%83%B3%E3%83%89%E3%82%B1%E3%83%BC%E3%82%AD%E3%83%95%E3%83%AB%E3%83%BC%E3%83%84%E3%83%9F%E3%83%83%E3%82%AF%E3%82%B9-200g/dp/B07FMTV5GF/ref=sr_1_13?__mk_ja_JP=%E3%82%AB%E3%82%BF%E3%82%AB%E3%83%8A&keywords=%E3%82%B1%E3%83%BC%E3%82%AD&qid=1577206099&refinements=p_76%3A2227292051&rnid=2227291051&rps=1&sr=8-13")
    q_5000.put("https://www.amazon.co.jp/BANDAI-%E3%82%AD%E3%83%A3%E3%83%A9%E3%83%87%E3%82%B3%E3%82%AF%E3%83%AA%E3%82%B9%E3%83%9E%E3%82%B9-%E3%82%B9%E3%82%BF%E3%83%BC%E2%98%86%E3%83%88%E3%82%A5%E3%82%A4%E3%83%B3%E3%82%AF%E3%83%AB%E3%83%97%E3%83%AA%E3%82%AD%E3%83%A5%E3%82%A2/dp/B07ZCXYHRK/ref=sr_1_4?__mk_ja_JP=%E3%82%AB%E3%82%BF%E3%82%AB%E3%83%8A&keywords=%E3%82%B1%E3%83%BC%E3%82%AD&qid=1577206168&refinements=p_76%3A2227292051&rnid=2227291051&rps=1&sr=8-4")
    q_10000.put("https://www.amazon.co.jp/%E6%A3%AE%E6%B0%B8%E8%A3%BD%E8%8F%93-%E6%A3%AE%E6%B0%B8%E3%82%A8%E3%83%B3%E3%82%BC%E3%83%AB-%E3%82%B7%E3%83%BC%E3%83%88%E3%82%B1%E3%83%BC%E3%82%AD-%E3%83%86%E3%82%A3%E3%83%A9%E3%83%9F%E3%82%B9-365g%C3%9712%E7%AE%B1/dp/B01LYO5X95/ref=sr_1_4?__mk_ja_JP=%E3%82%AB%E3%82%BF%E3%82%AB%E3%83%8A&keywords=%E3%82%B1%E3%83%BC%E3%82%AD&qid=1577206219&refinements=p_76%3A2227292051&rnid=2227291051&rps=1&sr=8-4")

    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
