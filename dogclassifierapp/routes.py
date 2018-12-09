from flask import Flask, render_template, flash, request, redirect, url_for, send_from_directory, Response
from werkzeug.utils import secure_filename
import os
from dogclassifierapp.prediction_scripts.predict_dog_breed import predict_breed
from dogclassifierapp import app
import logging
import json

logging.warning('in routes.py')

UPLOAD_FOLDER = os.path.join(app.root_path, 'tmp')
logging.warning('root folder: ' + UPLOAD_FOLDER)
ALLOWED_EXTENSIONS = set(['pdf', 'png', 'jpg', 'jpeg'])


app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER



@app.route('/', methods=['GET'])
def index():
    logging.warning('in index route get')
    return render_template('index.html')


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


class Prediction:
    def __init__(self, predictionText, predictionImage):
        self.predictionText = predictionText
        self.predictionImage = predictionImage


@app.route('/prediction', methods=['POST'])
def predict():
    def generate(image_path):
        logging.warning('in generator')
        # return immediate response to get another 55s window
        yield " "
        logging.warning('yielded 1 byte')

        pred_message, pred_img = predict_breed(image_path)
        logging.warning('predicted')

        prediction_results = Prediction(pred_message, pred_img)
        logging.warning('built result')
        
        logging.warning('removed')
        yield json.dumps(prediction_results.__dict__)

    logging.warning('in predict')
    file = request.files['file']
    logging.warning('got file')
    if file and allowed_file(file.filename):
        logging.warning('file allowed')
        filename = secure_filename(file.filename)
        logging.warning('secure filename')
        image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        logging.warning('path joined')
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        logging.warning('image saved')
    
    return Response(generate(image_path), mimetype='application/json')


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)