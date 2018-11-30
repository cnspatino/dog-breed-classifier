"""
This script loads a trained network from a checkpoint file and uses the model to 
predict the dog breed for an input image. When the input image is of a dog, it 
returns the predicted breed. When the input image is of a human, it returns the 
most resembling breed along with an image of a dog of that breed.

Required inputs:    - image_path: type str, filepath to single image
                    - checkpoint: type str, checkpoint filepath for trained network

Optional inputs:    - topk: type int, returns the top K most likely dog breeds (default is 1)
                    - gpu: whether to train on gpu (default is cpu)

"""

# import packages
import argparse
from detector_functions import face_detector, dog_detector
from data_functions import path_to_tensor
from keras.models import load_model
from keras.applications.resnet50 import ResNet50, preprocess_input
import pickle
import numpy as np

# set up command line inputs
parser = argparse.ArgumentParser(description='Predicts dog breed for an input image')
parser.add_argument('image_path', type=str)
parser.add_argument('checkpoint', type=str)
args = vars(parser.parse_args())

# set input args to variables
img_path = args['image_path']
checkpoint = args['checkpoint']

# load model
model = load_model(checkpoint)

# convert image into tensor
img_tensor = path_to_tensor(img_path)

def Resnet50_predict_breed(img_path):
    # extract bottleneck features from pre-trained ResNet50 model
    bottleneck_feature = ResNet50(weights='imagenet', include_top=False).predict(preprocess_input(img_tensor))
    # obtain vector of prediction probabilities
    predicted_vector = model.predict(bottleneck_feature)
    # return dog breed that is predicted by the model
    return dog_names[np.argmax(predicted_vector)].replace('_',' ')

# load list of dog names from pickle file
with open('dog_names.pkl', 'rb') as f:
	dog_names = pickle.load(f)

# get predicted dog breed name
prediction = Resnet50_predict_breed(img_path).replace('_',' ')

# get correct article to use in front of breed name
vowels = ['a','e','i','o','u']
if prediction.lower()[0] in vowels:
	article = 'an'
else:
    article = 'a'

# print out predictions       
if face_detector(img_path) == True and dog_detector(img_path) == False:
    print("Hi there, human! You resemble {} {}. I'd take that as a compliment! :)".format(article, prediction)) 
elif dog_detector(img_path) == True:
    print("This doggo appears to be {} {}. What a good boye!".format(article, prediction))
else:
    print("Oops! Please make sure the image is either of a dog or a human face that is shown clearly. Otherwise the algorithm will have a ruff time!")

	



