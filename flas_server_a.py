#https://flask.palletsprojects.com/en/2.0.x/quickstart/
import flask
from flask_cors import CORS
from flask import Flask, request, jsonify, session
from datetime import date
import requests

app = Flask(__name__)
CORS(app)

@app.route("/",  methods=['POST'])
def hello_world():
    data=request.get_json(force=True)
    return " blah"

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return "you are logged in man"
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''


@app.route("/mike", methods=['GET', 'POST'])
def mike():
    b=request.form
    c=request.json
    r=flask.Response()
    r.status=200

    return jsonify("{name:mike}")


app.run(host='0.0.0.0',port=5001)
