
from flask import Flask,jsonify
import requests
import simplejson 
import json
import constants

app = Flask(__name__)

@app.route("/")
def home():
    
    try:
        uResponse = requests.get(constants.uri_ordure_menage)
    except requests.ConnectionError:
       return "Connection Error"  
    Jresponse = uResponse.text
    data = json.loads(Jresponse)

    return Jresponse

if __name__ == "__main__":
    app.run(debug = True)