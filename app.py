from flask import Flask, jsonify, request, Response
import json
import requests


app = Flask(__name__)

@app.route("/")
def home():
  return jsonify({"home": "ok"})

@app.route("/api/notif", methods = ['POST'])
def notif():
    print(json.dumps(request.get_json(), indent=2))

    return ('', 204)

@app.route("/api/clients")
def customers():
    print("PYTHON-CLIENTS-API: Get Client List")

    return jsonify([{
        "nom": "Martin Ouimet",
        "email": "mouimet@redhat.com"
    },
    {
        "name": "Michael Lessard",
        "email": "mlessard@redhat.com"
    },
    {
        "name": "Martin Sauve",
        "email": "msauve@redhat.com"
    }
    ])

app.run(host="0.0.0.0", port=8080)