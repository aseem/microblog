from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# This import must come after app is created
from app import routes
