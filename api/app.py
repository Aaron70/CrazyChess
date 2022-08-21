from flask import Flask, request, Response as response
from flask_cors import CORS
import json as JSON

app = Flask(__name__)
CORS(app)

def makeResponseJSON(status,obj):
    obj = JSON.dumps()
    return response(obj, status=status, mimetype="application/json")

@app.route("/")
def hello_world():
    return "Hello world, with cross-origin."

@app.route("/user/create", methods = ['POST'])
def create_user():
    user_name = request.form.get('username')
    if ( user_name == None ):
        json = {
                # TODO: add the rest of the structure 
                }
        return makeResponseJSON(500,json)
