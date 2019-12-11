from flask import Flask, url_for, request, redirect, render_template
from flask_pymongo import PyMongo
from dateutil.parser import parse
from datetime import datetime
import os

from create_pdf import _create_pdf

app = Flask(__name__, static_folder='./frontend/dist', static_url_path="/", template_folder="./frontend/dist")

app.config["MONGO_URI"] = os.getenv("MONGODB_URI", "mongodb://localhost:27017/testdb")
mongo = PyMongo(app)


@app.route("/")
def index():
    return render_template("index.html")

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
        entries.append({
            "name": row['name'],
            "start_date": row['start_date'].strftime("%Y/%m/%d"),
            "create_date": row['create_date'].strftime("%Y/%m/%d"),
            "week_journal": row['week_journal'],
            "journal": row['journal']
        })
    print(entries)
    return str(entries)


@app.route('/api/add', methods=['POST'])
def add_entry():
    mongo.db.user.insert({
        "name": request.form['name'],
        "start_date": parse(request.form['start_date']),
        "create_date": datetime.now(),
        "week_journal": [
            request.form['week1'],
            request.form['week2'],
            request.form['week3'],
            request.form['week4'],
            request.form['week5'],
            request.form['week6'],
            request.form['week7']
        ],
        "journal": request.form['journal']
    })
    return redirect(url_for('show_entry'))


@app.route('/create', methods=['GET'])
def create_pdf_from_db():
    user = mongo.db.user.find_one()
    content = {
        "name": user["name"],
        "start_date": user["start_date"],
        "create_date": user["create_date"],
        "week_journal": user["week_journal"],
        "journal": user["journal"]
    }
    return _create_pdf(content)

@app.route('/search', methods=['POST'])
def filter_entry():
    # start = parse(request.form['start'])
    # end = parse(request.form['end'])
    # cur = mongo.db.user.find({'birthday': {'$lt': end, '$gte': start}})
    # results = []
    # for row in cur:
    #     results.append({"name": row['name'], "birthday": row['birthday'].strftime("%Y/%m/%d")})
    # print(results)

    return "search!!"


@app.errorhandler(404)
def error_handler(error):
    return "Oops!! Something wrong..."

if __name__ == '__main__':
    # app.debug = True
    # app.run()
    print(app.url_map)
    app.run(
        host=os.getenv("APP_ADDRESS", 'localhost'),
        port=os.getenv("APP_PORT", 3000)
    )