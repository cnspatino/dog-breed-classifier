# dog-breed-classifier
Web app for predicting dog breed from an image using a CNN

### Table of Contents

1. [Installation](#installation)
2. [Project Motivation](#motivation)
3. [File Descriptions](#files)
4. [Licensing, Authors, and Acknowledgements](#licensing)

## Installation <a name="installation"></a>
This code runs using Python versions 3.*. Additional python packages needed for this code are included in the requirements.txt file.

The packages can be installed by typing the following into your terminal (on a MacOS/Linux system):

`pip install -r requirements.txt`

To run the Flask app locally:

Type the following into your terminal (MacOS):

- export FLASK_APP=routes.py
- flask run

Copy the URL displayed in your terminal (should say Running on [the url]) and paste it into your browser. You can then use the web app to upload an image of a dog or human (click Choose File and select desired image) and predict the breed/resembling breed (click Predict).

## Project Motivation <a name="motivation"></a>
My motivation for this project was to develop an image classifier using convolutional neural networks that can:

1. Detect whether the subject of the image is a dog or a human
2. If a human is detected, return the dog breed that best resembles the human
3. If a dog is detected, return the predicted breed

I then implemented these scripts as a web app so that the user can easily run it locally in their browser and upload an image to get a prediction as opposed to having to run it from the command line. 
Through this project, I got a deeper knowledge of convolutional neural networks as well as more practice in web app development, getting to experiment with JavaScript, CSS and Flask.

## File Descriptions <a name="files"></a>
This repository includes all of the files that were necessary to code and deploy the web app.
The index.html file can be found in the templates folder. This file includes the HTML and Bootstrap code for designing the web page. The complimentary JavaScript and CSS code can be found in the static folder. The saved Keras model (resnet50_model.h5), the cascade file for the face detector (haarcascade_frontalface_alt.xml) and the pickle file with the list of dog breed names (dog_names.pkl) can also be found in the static folder. Lastly, a corresponding image of each dog breed can be found in the static/breeds folder.

The prediction_scripts folder contains all of the necessary scripts for getting the dog breed prediction from the uploaded file:

- Detector_functions.py contains the script for detecting whether the image is of a human or a dog
- Data_functions.py contains additional helper functions to run the main prediction script
- predict_dog_breed.py  is the main prediction script that utilizes the detector functions and helper functions

The requirements.txt file includes all of the necessary libraries for this project.

## Licensing, Authors, and Acknowledgements <a name="licensing"></a>
I'd like to thank the Udacity Data Science Nanodegree team for the inspiration for this project and for template code for the CNN image classifier. I’d also like to thank suketran for providing code on Bootsnipp for uploading an image and displaying a preview of the uploaded image on a webapp ([code found here](https://bootsnipp.com/snippets/eNbOa)).

