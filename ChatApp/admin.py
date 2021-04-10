# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 14:13:20 2021

@author: bipin
"""

#import hashlib
import json
from flask import Flask, jsonify, request, render_template, redirect, url_for, flash
import requests
from flask_cors import CORS
import pickle


app = Flask(__name__)
cors = CORS(app)

port = 6080

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('report.html', error=None)

@app.route('/blockchain', methods=['GET'])
def blockchain():
    chain = []
    try:
        with open('database', 'rb') as db:
            chain = pickle.load(db)
    except:
        print("failed")
        pass
    response = {'chain': chain,
                'length': len(chain)
                }
    print(response)
    return jsonify(response), 200

@app.route('/add_to_sale', methods=['POST'])
def add_to_sale():
    json_req = request.get_json()
    receiver_id = json_req["receiver_id"]
    receiver_alias = json_req["receiver_alias"]
    type_of_asset = json_req["type"]
    amount = json_req["amount"]
    keys = {}
    with open('publickeys.json') as f:
        try:
            keys = json.load(f)  
        except:
            pass
    response = {}
    if receiver_alias in keys:
        if keys[receiver_alias]["public_address"] != receiver_id :
            response = "User and public address do not match"   
            return jsonify(response),200
    else :
        response = "User not in database"
        return jsonify(response),200
    with open('assets_for_sale.json') as f:
        try:
            keys = json.load(f)  
        except:
            pass
    print(keys)
    if receiver_alias in keys:
        keys[receiver_alias].append({"receiver_id": receiver_id, "receiver_alias" : receiver_alias, "type" : type_of_asset, "amount" : amount})
    else :
        keys[receiver_alias] = [{"receiver_id": receiver_id, "receiver_alias" : receiver_alias, "type" : type_of_asset, "amount" : amount}]
    with open('assets_for_sale.json','w') as f:
        json.dump(keys, f)
#    response = {}
    response["message"] = "asset added successfully"
    return jsonify(response), 200

@app.route('/all_sales', methods=['GET'])
def add_sales():
    keys = {}
    
    with open('assets_for_sale.json') as f:
        try:
            keys = json.load(f)  
        except:
            pass
    print(keys)
    resoonse = {}
    resoonse["keys"] = keys
    print(jsonify(resoonse))
    return jsonify(resoonse), 200

app.run(host = '0.0.0.0', port = port)