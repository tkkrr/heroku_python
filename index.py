from flask import Flask, url_for, request, redirect
import os
app = Flask(__name__, static_folder='./frontend/dist', static_url_path="/")

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

if __name__ == '__main__':
    # app.debug = True
    # app.run()
    print(app.url_map)
    app.run(
        host=os.getenv("APP_ADDRESS", 'localhost'),
        port=os.getenv("APP_PORT", 3000)
    )