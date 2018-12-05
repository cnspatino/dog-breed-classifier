from flask import Flask, render_template, flash, request, redirect, url_for, send_from_directory, jsonify
from werkzeug.utils import secure_filename
import os
from dogclassifierapp.prediction_scripts.predict_dog_breed import predict_breed


UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = set(['pdf', 'png', 'jpg', 'jpeg'])


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER



@app.route('/', methods=['GET'])
def index():
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
    file = request.files['file']
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        pred_message = predict_breed(image_path)

        prediction_results = Prediction(pred_message, 'dummy')
        # TO DO: erase image
        return jsonify(prediction_results.__dict__)


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)