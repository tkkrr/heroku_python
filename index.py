from flask import Flask, url_for, request, redirect, g
from flask_pymongo import PyMongo
from dateutil.parser import parse
import os

app = Flask(__name__, static_folder='./frontend/dist', static_url_path="/")

app.config["MONGO_URI"] = "mongodb://localhost:27017/testdb"
app.secret_key = 'secret'
mongo = PyMongo(app)


@app.route("/")
def index():
    return redirect("/index.html")

@app.route('/api/')
def hello_world():
    return '''
    <h1>Hello World!!</h1>
    '''

@app.route('/api/hello')
def hello(methods = ["GET"]):
    name = request
    print(name)
    # name = request.args.get("name")
    return '''
    <p>Hello?</p>
    '''

@app.route('/api/hello/<int:username>')
def hello_name(username):
    return str(username)


@app.route('/api/db', methods=['GET'])
def show_entry():
    users = mongo.db.user.find()
    entries = []
    for row in users:
        entries.append({"name": row['name'], "birthday": row['birthday'].strftime("%Y/%m/%d")})
    print(entries)
    return str(entries)


@app.route('/api/add', methods=['POST'])
def add_entry():
    mongo.db.user.insert({"name": request.form['name'], "birthday": parse(request.form['birthday'])})
    return redirect(url_for('show_entry'))


@app.route('/search', methods=['POST'])
def filter_entry():
    start = parse(request.form['start'])
    end = parse(request.form['end'])
    cur = mongo.db.user.find({'birthday': {'$lt': end, '$gte': start}})
    results = []
    for row in cur:
        results.append({"name": row['name'], "birthday": row['birthday'].strftime("%Y/%m/%d")})
    print(results)

    return "search!!"


if __name__ == '__main__':
    # app.debug = True
    # app.run()
    print(app.url_map)
    app.run(
        host=os.getenv("APP_ADDRESS", 'localhost'),
        port=os.getenv("APP_PORT", 3000)
    )