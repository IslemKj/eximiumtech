from flask import Flask, render_template, request, session, redirect, url_for, flash, jsonify
from passlib.hash import sha256_crypt
import mysql.connector
import os
import time
from passlib.hash import sha256_crypt  # Make sure this import is present
from datetime import datetime
import hashlib


app = Flask(__name__)
app.secret_key = 'abla bla key bbdd'


@app.route('/') # Main page 
def index():
    return render_template(
        'index.html'
    )
    
@app.route('/contact') # Contact page
def contact():
    return render_template(
        'contact.html'
    )
    
@app.route('/about') # about page
def about():
    return render_template(
        'about.html'
    )
    
@app.route('/projects') # projects page
def projects():
    return render_template(
        'projects.html'
    )
    
@app.route('/services') # services page
def services():
    return render_template(
        'services.html'
    )
    
if __name__ == '__main__':
    app.run(debug=True)
