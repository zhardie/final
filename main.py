#!/usr/bin/env python

import flask
import os
import cgi
import requests
import json
import time
import hashlib
from flask import request
APP = flask.Flask(__name__)

@APP.route('/')
def index():
    
    return flask.render_template('index.html')

@APP.route('/pwn', methods=['POST'])
def pwn():
    i = 0
    while i < 5:
        refer = request.form['refer']
        millis = int(round(time.time() * 1000))
        hashstring = str(millis) + refer
        email = (hashlib.md5(hashstring.encode('utf-8')).hexdigest()) + '%40pwn.com'
    
        headers = {
            'Origin': 'https://www.getfinal.com',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'en-US,en;q=0.8',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (X11; CrOS x86_64 7077.134.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.156 Safari/537.36',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Cache-Control': 'max-age=0',
            'Referer': 'https://www.getfinal.com/?ref=' + refer,
            'Connection': 'keep-alive',
        }
        data = 'signup%5Bemail%5D=' + email + '&signup%5Bshare_hash%5D=' + refer + '&subscribe='
        
        r = requests.post('https://apply.getfinal.com/signups', headers=headers, data=data)
        i += 1
    return flask.render_template('pwned.html')
    
if __name__ == '__main__':
    APP.debug=True
    APP.run(host=os.environ['IP'],port=int(os.environ['PORT']))