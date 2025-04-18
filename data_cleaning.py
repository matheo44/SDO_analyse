import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import os

# data_cleaning function put in trash folder black images
# this function drive throught the rush folder if the sum of all pixels of the image have less than 1.500.000px delete it and move in trash folder.
# WARNING this function work only for an 1024px resolution

def data_cleaning(directory):

    for image in os.listdir(directory):

        if(".jpg") in (directory+'/'+image):
            # print(directory+'/'+image)
            picture = Image.open(directory+'/'+image)
            
            if np.sum(picture) <= 1500000:
                picture.save('trash/'+image)
                os.remove(directory+'/'+image)
    return print(directory, "is now clean")
