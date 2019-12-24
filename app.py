# coding: utf-8
from flask import *

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    return render_template('index.html')

@app.route('/present', methods=["GET", "POST"])
def present():
    if request.method == "POST":
        return render_template('present.html')
if __name__ == "__main__":
    # webサーバー立ち上げ
    app.run(port=8000,debug=True)
