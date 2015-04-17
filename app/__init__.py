from flask import Flask
import logging

app = Flask(__name__)

# Add config to app
app.config.from_object(__name__)

# Import our views
from app.views import *
