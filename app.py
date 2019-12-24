from flask import *

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    return render_template('index.html')

if __name__ == "__main__":
    # webサーバー立ち上げ
app.run(port=8000,debug=True)
