from flask import Flask

app = Flask(__name__)

from dogclassifierapp import routes

