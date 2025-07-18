from flask import render_template, request, redirect,url_for,flash
from  Components import app, db

@app.route('/')
def index():
    return 'This is index page'