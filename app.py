from flask import Flask
from flask import render_template, request, flash, session, url_for, redirect, make_response
app = Flask(__name__)
# from flask_sslify import SSLify
# sslify = SSLify(app)
app.config['DEBUG'] = True

@app.route('/')
def index():
    return render_template('site/index.html')

@app.route('/price-list')
def price_list():
    return render_template('site/price-list.html')

#@app.route('/paymants')
#def paymants():
    #return render_template('site/paymants.html')

@app.route('/cctv')
def cctv():
    return render_template('site/cctv.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('layouts/404.html'), 404

