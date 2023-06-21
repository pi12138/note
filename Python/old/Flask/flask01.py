from flask import Flask
from flask import request
from flask import make_response


app = Flask(__name__)


@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')

    # return """<h1>Hello World!</h1><br><p>Your browser is {}</p>""".format(user_agent)
    return '<h1>Bad request</h1>', 400

@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, {}!</h1>'.format(name)


@app.route('/response/')
def res():
    response = make_response('<h1>This is document carries a cookie!</h1>')
    response.set_cookie('answer', '42')
    return response


if __name__ == "__main__":
    app.run(debug=True)


