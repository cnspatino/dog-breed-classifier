import cv2    
from keras.applications.resnet50 import preprocess_input, decode_predictions
from data_functions import path_to_tensor


def face_detector(img_path):
	### returns "True" if face is detected in image stored at img_path
    face_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_alt.xml')
    img = cv2.imread(img_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray)
    
    return len(faces) > 0


def dog_detector(img_path):
	### returns "True" if a dog is detected in the image stored at img_path
	from keras.applications.resnet50 import ResNet50

	# define ResNet50 model
	ResNet50_model = ResNet50(weights='imagenet')

	# returns prediction vector for image
	img = preprocess_input(path_to_tensor(img_path))

	# predicts label based on max probability in prediction vector
	prediction = np.argmax(ResNet50_model.predict(img))

	return ((prediction <= 268) & (prediction >= 151)) 

    
