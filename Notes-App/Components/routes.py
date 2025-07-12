from flask import render_template,request,redirect,url_for,flash
from Components import app

@app.route('/')
def index():
    return 'This is Index page of notes app'