from flask import Flask
import logging

app = Flask(__name__)

# Add config to app
app.config.from_object('config')
app.secret_key = 'imsosecretyeah1'

# Import our views
from app.views import index
