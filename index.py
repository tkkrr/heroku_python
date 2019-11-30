from flask import Flask, url_for, request
app = Flask(__name__)


@app.route('/')
def hello_world():
    return '''
    <link rel="stylesheet" type="text/css" href="static/style.css">
    <h1>Hello World!!</h1>
    '''

@app.route('/hello')
def hello(methods = ["GET"]):
    name = request
    print(name)
    # name = request.args.get("name")
    return '''
    <p>Hello?</p>
    '''

@app.route('/hello/<int:username>')
def hello_name(username):
    return str(username)

if __name__ == '__main__':
    # app.debug = True
    app.run()