#
from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    names=['gauri']
    date=[]
    for i in names:
        url= "https://h6unpbwfnl.execute-api.us-east-1.amazonaws.com/santizerappdataretrive?Name=gauri&date=15-04-2002"
        resp = requests.get(url)
        data = resp.json()
        print(data)
        #[{'name': 'gauri', 'date':'15-04-2002'}]
        date.append(data['date'])
    return render_template('stats.html',p1=names[0],d1=date[0])


if __name__ == '__main__':
   app.run(host='0.0.0.0', port=5000, debug=True)        