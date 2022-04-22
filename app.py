# -*- coding: utf8 -*-
import os
from flask import Flask, g, render_template, redirect, flash, request, jsonify, url_for, make_response, request,session, send_file, send_from_directory, Markup
from functools import wraps
from datetime import datetime, timedelta
from flask_wtf.csrf import CSRFProtect
import base64
import json
from config import PROJECT_ROOT, BASE_URL, PORT
from threading import Thread
import logging

from werkzeug.utils import secure_filename
from werkzeug.exceptions import BadRequest, InternalServerError, Forbidden, HTTPException, NotFound

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# logging.basicConfig(filename='cjapi.log', level=logging.DEBUG)

app.config['SECRET_KEY'] = 'shawasdlajnxiudhfhh3454qjijhgoaputki'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cjapi.db'

csrf = CSRFProtect(app)

@app.after_request
def after_request(response):
    response.headers['Cache-control']='no-store, no-cache, must-revalidate, post-check=0, pre-check=0'
    return response

@app.errorhandler(InternalServerError)
def e_500(e):
    app.logger.debug(e)
    return jsonify({'message':'Internal Server Error'}), 500

@app.errorhandler(HTTPException)
def e_http(e):
    app.logger.debug(e)
    return jsonify({'message':'HTTPException'}), 500


@app.errorhandler(Forbidden)
def e_forbidden(e):
    app.logger.critical(e)
    return jsonify({'message':'Forbidden'}), 401

@app.errorhandler(BadRequest)
def e_bad(e):
    app.logger.error(e)
    return jsonify({'message':'BadRequest'}), 400

@app.errorhandler(NotFound)
def e_404(e):
    app.logger.debug(e)
    return jsonify({'message':'KhujePaini'}), 404

@csrf.exempt
@app.route('/', methods=['POST'])
def vice_city():
    from get_country import country_lookup
    json_data = request.json
    remote_addr = request.remote_addr
    import pprint
    pp = pprint.PrettyPrinter(indent=2)
    pp.pprint(dir(request))
    pp.pprint(request.access_route[0])

    # process json_data
    country_name = country_lookup(remote_addr)
    # return jsonify(country_name)
    return jsonify({'ip':remote_addr, 'country':country_name})


if __name__ == '__main__':
    # print(PROJECT_ROOT)
    app.run(debug=True, port=PORT)