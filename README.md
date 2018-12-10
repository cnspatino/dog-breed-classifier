# dog-breed-classifier
Web app for predicting dog breed from an image using a CNN

### Table of Contents

1. [Installation](#installation)
2. [Project Motivation](#motivation)
3. [File Descriptions](#files)
4. [Summary of Model and Results](#results)
5. [Licensing, Authors, and Acknowledgements](#licensing)

## Installation <a name="installation"></a>
This code runs using Python versions 3.*. Additional python packages needed for this code are included in the requirements.txt file.

The packages can be installed by typing the following into your terminal (on a MacOS/Linux system) once you're in the directory of the repo:

`pip install -r requirements.txt`

To run the Flask app locally:

Change the directory to dogclassifierapp/ (within the repo) and then type the following into your terminal (MacOS):

- export FLASK_APP=routes.py
- flask run

Copy the URL displayed in your terminal (should say Running on [the url]) and paste it into your browser. You can then use the web app to upload an image of a dog or human (click Choose File and select desired image) and predict the breed/resembling breed (click Predict).

## Project Motivation <a name="motivation"></a>
My motivation for this project was to develop an image classifier using convolutional neural networks that can:

1. Detect whether the subject of the image is a dog or a human
2. If a human is detected, return the dog breed that best resembles the human
3. If a dog is detected, return the predicted breed

I then implemented these scripts as a web app so that the user can easily run it locally in their browser and upload an image to get a prediction as opposed to having to run it from the command line. 

For this project, I was also motivated to get a deeper knowledge of convolutional neural networks as well as more practice in web app development, getting to experiment with JavaScript, CSS and Flask.

Note, the RunOnHeroku branch includes the modified code for deploying this app to Heroku. Unfortunately, I could not get around Heroku's timeout limit, but still left this as a branch to show the process for deploying it.

## File Descriptions <a name="files"></a>
This repository includes all of the files that were necessary to code and deploy the web app.
The index.html file can be found in the templates folder. This file includes the HTML and Bootstrap code for designing the web page. The complimentary JavaScript and CSS code can be found in the static folder. The saved Keras model (resnet50_model.h5), pre-trained face detector file (haarcascade_frontalface_alt.xml) and a pickle file with the list of dog breed names (dog_names.pkl) can also be found in the static folder. Lastly, a corresponding image of each dog breed can be found in the static/breeds folder.

The prediction_scripts folder contains all of the necessary scripts for getting the dog breed prediction from the uploaded file:

- Detector_functions.py contains the script for detecting whether the image is of a human or a dog
- Data_functions.py contains additional helper functions to run the main prediction script
- predict_dog_breed.py  is the main prediction script that utilizes the detector functions and helper functions

The requirements.txt file includes all of the necessary libraries for this project.

## Summary of Model and Results <a name="results"></a>
For this project, I used transfer learning to create a convolutional neural network using bottleneck features from a Resnet50 model pre-trained on the ImageNet dataset. Bottleneck features are the last activation maps before the fully-connected layers, and using them allows us to make use of the knowledge already gained by the pre-trained model. Transfer learning allows us to reduce training time without sacrificing accuracy by only having to train on the newly added layers.

The model architecture was designed as follows:

-	Input layer: The output of the ResNet50 model (aka the bottleneck features)
-	Global Average Pooling layer
-	Fully connected layer with a softmax activation function

The model was trained on 6680 dog images using 20 epochs to find the best weights. I then used the trained model to predict the results of 836 test dog images. The result was a test accuracy of 81%.

**Detector Results**:

With a test set of 100 human face images and 100 dog images, the following results were determined:

- Human face detector: A human face was detected in 100% of the human images and 11% of the dog images.
- Dog detector: A dog was detected in 0% of the human images and 100% of the dog images.

**Potential points of improvement**:

1. An ensemble approach could be employed in order to further improve prediction accuracy.
2. Other animal detector algorithms could be applied in order to detect and reject images of other animals.
3. Training the model on human and dog images in which the subject is not looking straight at the camera could help with the accuracy of the model and detector functions.


## Licensing, Authors, and Acknowledgements <a name="licensing"></a>
I'd like to thank the Udacity Data Science Nanodegree team for the inspiration for this project and for template code for the CNN image classifier. I’d also like to thank suketran for providing code on Bootsnipp for uploading an image and displaying a preview of the uploaded image on a webapp ([code found here](https://bootsnipp.com/snippets/eNbOa)).

