# import packages
from dogclassifierapp.prediction_scripts.detector_functions import face_detector, dog_detector
from dogclassifierapp.prediction_scripts.data_functions import path_to_tensor, extract_Resnet50, Resnet50_predict_breed
from keras.models import load_model
from keras.applications.resnet50 import ResNet50, preprocess_input
import pickle
import numpy as np


def predict_breed(img_path, checkpoint='/Users/cadpav/Documents/Udacity/Data_Scientist_Nanodegree/Term2/Projects/Capstone_project/dog_classifier_webapp/dogclassifierapp/prediction_scripts/resnet50_model.h5', names_pkl='/Users/cadpav/Documents/Udacity/Data_Scientist_Nanodegree/Term2/Projects/Capstone_project/dog_classifier_webapp/dogclassifierapp/prediction_scripts/dog_names.pkl'):
	"""
	This function loads a trained network from a checkpoint file and uses the model to 
	predict the dog breed for an input image. When the input image is of a dog, it 
	returns the predicted breed in a friendly message. When the input image is of a 
	human, it returns the most resembling breed in a corresponding message.

	Inputs:    			- img_path: type str, filepath to single image
	                    - checkpoint: type str, checkpoint filepath for trained network
	                    - names_pkl: type str, path to pkl file of list of dog names

	Output:				- prediction message
	                    

	"""

	# load model
	model = load_model(checkpoint)

	# load list of dog names from pickle file
	with open(names_pkl, 'rb') as f:
		dog_names = pickle.load(f)

	# return dog breed that is predicted by the model
	prediction = Resnet50_predict_breed(img_path, model, dog_names)

	# get correct article to use in front of breed name
	vowels = ['a','e','i','o','u']
	if prediction.lower()[0] in vowels:
		article = 'an'
	else:
	    article = 'a'

	# return prediction with friendly message      
	if face_detector(img_path) == True and dog_detector(img_path) == False:
	    return "Hi there, human! You resemble {} {}. I'd take that as a compliment! :)".format(article, prediction)
	elif dog_detector(img_path) == True:
	    return "This doggo appears to be {} {}. What a good boye!".format(article, prediction)
	else:
	    return "Oops, the algorithm won't work with this image! Please make sure the image is either of a dog or a front-facing human face."

	



