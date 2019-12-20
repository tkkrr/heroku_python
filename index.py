from flask import Flask, url_for, request, redirect, render_template, jsonify
from flask_pymongo import PyMongo, ObjectId, DESCENDING
from dateutil.parser import parse
from datetime import datetime
import os

from create_pdf import _create_pdf

app = Flask(__name__, static_folder="./frontend/dist", static_url_path="", template_folder="./frontend/dist")

# mongoDBとのコネクションを作成．herokuの環境では環境変数を参考にする．
app.config["MONGO_URI"] = os.getenv("MONGODB_URI", "mongodb://localhost:27017/testdb")
mongo = PyMongo(app)


@app.route("/")
def index():
    '''
    vueにて作成したindex.htmlを表示する．
    '''
    return render_template("index.html")

@app.route('/api/')
def hello_world():
    return '''
    <h1>Hello World!!</h1>
    '''


@app.route('/api/all', methods=['GET'])
def show_entry():
    '''
    mongoDBに登録されているuser(PDFについての情報)の一覧を習得する．
    '''
    users = mongo.db.user.find()
    entries = []
    for row in users:
        entries.append({
            "_id": str(row['_id']),
            "name": row['name'],
            "start_date": row['start_date'].strftime("%Y/%m/%d"),
            "create_date": row['create_date'].strftime("%Y/%m/%d"),
            "week_journal": row['week_journal'],
            "journal": row['journal']
        })
    return jsonify( entlies=entries )


@app.route('/api/recent', methods=['GET'])
def show_entry_latest():
    '''
    mongoDBに登録されているuser(PDFについての情報)の最新10件を習得する．
    '''
    users = mongo.db.user.find(limit=10).sort('create_date', DESCENDING)
    entries = []
    for row in users:
        entries.append({
            "_id": str(row['_id']),
            "name": row['name'],
            "start_date": row['start_date'].strftime("%Y/%m/%d"),
            "create_date": row['create_date'].strftime("%Y/%m/%d"),
            "week_journal": row['week_journal'],
            "journal": row['journal']
        })
    return jsonify( entlies=entries )


@app.route('/api/add', methods=['POST'])
def add_entry():
    '''
    journalの情報をmongoDBに保存する．
    '''
    name = request.form['name'] if request.form['name'] != "" else "John Doe"
    start_date = parse( request.form['start_date'] ) if request.form['start_date'] != "" else datetime.now()
    journal = request.form['journal'] if request.form['journal'] != "" else "特になし"
    week_journal = []
    for i in range(1,8):
        tmp = request.form[f'week{i}'] if request.form[f'week{i}'] != "" else "特になし",
        week_journal += tmp

    mongo.db.user.insert({
        "name": name,
        "start_date": start_date,
        "create_date": datetime.now(),
        "week_journal": week_journal,
        "journal": journal
    })
    return redirect(url_for('index'))


@app.route('/api/delete/<string:id>', methods=['DELETE'])
def delete_user(id):
    '''
    指定したIDのjournalをテーブルから削除する．
    '''
    _id = ObjectId(id)
    user = mongo.db.user.delete_one( {"_id" : _id} )
    return jsonify({'message': 'delete success'}), 200


@app.route('/api/select/<string:id>', methods=["GET"])
def select_user(id):
    _id = ObjectId(id)
    user = mongo.db.user.find_one( {"_id" : _id} )
    return str(user)


@app.route('/api/create/<string:id>', methods=['GET'])
def create_pdf_from_db(id):
    _id = ObjectId(id)
    user = mongo.db.user.find_one({"_id" : _id})
    content = {
        "name": user["name"],
        "start_date": user["start_date"],
        "create_date": user["create_date"],
        "week_journal": user["week_journal"],
        "journal": user["journal"]
    }
    return _create_pdf(content)

@app.route('/journal')
def old_journal_path():
    return redirect(url_for("index"))

@app.route('/search', methods=['POST'])
def filter_entry():
    # start = parse(request.form['start'])
    # end = parse(request.form['end'])
    # cur = mongo.db.user.find({'create': {'$lt': end, '$gte': start}})
    # results = []
    # for row in cur:
    #     results.append({"name": row['name'], "birthday": row['birthday'].strftime("%Y/%m/%d")})

    return "success!!"


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