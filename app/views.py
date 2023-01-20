from app import app
from flask import render_template

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return '<h1 style="color:blue">Samarth</h1>'

@app.errorhandler(404)
def not_found(e):
    return render_template("404.html")

