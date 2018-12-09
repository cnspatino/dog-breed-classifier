# import packages
from dogclassifierapp.prediction_scripts.detector_functions import face_detector, dog_detector
from dogclassifierapp.prediction_scripts.data_functions import path_to_tensor, extract_Resnet50, Resnet50_predict_breed
from keras.models import load_model
from keras.applications.resnet50 import ResNet50, preprocess_input
import pickle
import numpy as np
from os import listdir
from os.path import isfile, join
from keras import backend as K
from dogclassifierapp import app
import logging


def predict_breed(img_path, checkpoint='static/resnet50_model.h5', names_pkl='static/dog_names.pkl'):
	"""
	This function loads a trained network from a checkpoint file and uses the model to 
	predict the dog breed for an input image. When the input image is of a dog, it 
	returns the predicted breed in a friendly message. When the input image is of a 
	human, it returns the most resembling breed in a corresponding message.

	Inputs:    			- img_path: type str, filepath to single image
						- checkpoint: type str, checkpoint filepath for trained network
						- names_pkl: type str, path to pkl file of list of dog names

	Output:				- prediction message, path to breed image (if human) or empty string (if dog)
						

	"""

	logging.warning('in predict_breed')
	# clear Keras session to reset before loading model
	K.clear_session()

	# add root paths to file path inputs
	checkpoint = join(app.root_path, checkpoint)
	names_pkl = join(app.root_path, names_pkl)

	# add root path to prediction image paths
	breeds = join(app.root_path, 'static/breeds')
	dog_return_img = join(app.root_path, 'static/img/dog.jpg')
	other_return_img = join(app.root_path,'static/img/oops.png')

	logging.warning('predict_breed: load model')
	# load model
	model = load_model(checkpoint)
	logging.warning('predict_breed: loaded model')

	# load list of dog names from pickle file
	with open(names_pkl, 'rb') as f:
		dog_names = pickle.load(f)

	logging.warning('predict_breed: calling resnet_50_predict_breed')
	# return dog breed that is predicted by the model
	prediction = Resnet50_predict_breed(img_path, model, dog_names)
	logging.warning('predict_breed: returned prediction')
	# get correct article to use in front of breed name
	vowels = ['a','e','i','o','u']
	if prediction.lower()[0] in vowels:
		article = 'an'
	else:
		article = 'a'

	# return prediction with friendly message      
	if face_detector(img_path) == True and dog_detector(img_path) == False:
	
		# get list of filenames for breed images in breeds folder	
		breed_files = [f for f in listdir(breeds) if isfile(join(breeds, f))]
	
		# get filename that matches breed prediction
		for filename in breed_files:
			if prediction.replace(' ', '_') in filename:
				breed_img = os.path.join(breeds, filename)
		# return prediction message and breed image
		return "Hi there, human! Your furry doppelganger is {} {}. I'd take that as a compliment! :)".format(article, prediction), breed_img
	
	elif dog_detector(img_path) == True:
		return "This doggo appears to be {} {}. What a good boye!".format(article, prediction), dog_return_img
	
	else:
		return "Oops, the algorithm won't work with this image! Please make sure the image is either of a dog or a front-facing human face.", other_return_img

	



