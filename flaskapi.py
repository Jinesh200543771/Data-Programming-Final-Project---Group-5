from flask import Flask, render_template, jsonify
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('mongodb://jinesh:Jinesh5715@ac-vj7b4r1-shard-00-00.evkgv3q.mongodb.net:27017,ac-vj7b4r1-shard-00-01.evkgv3q.mongodb.net:27017,ac-vj7b4r1-shard-00-02.evkgv3q.mongodb.net:27017/?ssl=true&replicaSet=atlas-3odq0a-shard-0&authSource=admin&retryWrites=true&w=majority')
db = client.test
collection = db["weatherdata"]


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/data')
def data():
    return render_template('data.html')

@app.route('/charts')
def charts():
    return render_template('charts.html')

@app.route('/team')
def team():
    return render_template('team.html')

if __name__=='__main__':
    app.run()