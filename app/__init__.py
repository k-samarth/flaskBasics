from flask import Flask,render_template

app = Flask(__name__)

from app import views
from app import admin_views
