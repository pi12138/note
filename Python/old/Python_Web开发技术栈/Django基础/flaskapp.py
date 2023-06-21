from flask import Flask
from flask import Response

flask_app = Flask(__name__)

@flask_app.route('/hello')
def hello_world():
	return Response(
		'hello',
		mimetype='text/plain'
	)

app = flask_app.wsgi_app