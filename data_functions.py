from keras.applications.resnet50 import ResNet50, preprocess_input, decode_predictions
from keras.preprocessing import image                  
from tqdm import tqdm
import numpy as np

def path_to_tensor(img_path):
    # loads RGB image as PIL.Image.Image type
    img = image.load_img(img_path, target_size=(224, 224))
    # convert PIL.Image.Image type to 3D tensor with shape (224, 224, 3)
    x = image.img_to_array(img)
    # convert 3D tensor to 4D tensor with shape (1, 224, 224, 3) and return 4D tensor
    return np.expand_dims(x, axis=0)

def extract_Resnet50(tensor):
	return ResNet50(weights='imagenet', include_top=False, pooling='avg').predict(preprocess_input(tensor))

def Resnet50_predict_breed(img_path, model, name_list):
    # extract bottleneck features from pre-trained ResNet50 model (output is 2D)
    bottleneck_feature = extract_Resnet50(path_to_tensor(img_path))
    # add two more dimensions
    bottleneck_feature = np.expand_dims(bottleneck_feature, axis=0)
    bottleneck_feature = np.expand_dims(bottleneck_feature, axis=0)

    # obtain vector of prediction probabilities
    predicted_vector = model.predict(bottleneck_feature)
    # return dog breed that is predicted by the model
    return name_list[np.argmax(predicted_vector)].replace('_',' ')