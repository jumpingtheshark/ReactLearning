#https://flask.palletsprojects.com/en/2.0.x/quickstart/
import flask
from flask_cors import CORS
from flask import Flask, request, jsonify, session
from datetime import date
import requests
import logging


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


@app.route ('/mike_get', methods=['GET', 'POST'] )
def mike_get():
    rval = "{"
    queryStringDict = request.args
    for i, j in queryStringDict.items():
        print(i, j)
        rval=rval+i+':'+j+';'

    rval=rval+ "}"
    print (jsonify(rval))
    return jsonify(rval)





@app.route("/mike", methods=['GET', 'POST'])
def mike():
    c=request.json
    logging.info(c)
    b=request.form
    c=request.json
    r=flask.Response()
    r.status=200
   # r.headers.add_header("Access-Control-Allow-Origin", "http://localhost:8080")
   # return r
    #return jsonify("{name:mike}")
    return jsonify(c)
    #return jsonify(c)


app.run(host='0.0.0.0',port=5001)


