from flask import render_template, request, redirect,url_for,flash
from  Components import app, db
from Components.models import Post
from slugify import slugify



@app.route('/')
def index():
    return 'This is index page'