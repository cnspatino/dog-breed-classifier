from flask import Flask
import logging

logging.warning('starting')

app = Flask(__name__)

logging.warning('started')

from dogclassifierapp import routes