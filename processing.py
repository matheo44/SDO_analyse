import numpy as np
from PIL import Image

import os
import time

#white_to_red multiplying each R of RGB per 255 
def white_to_red(picture): # picture need to be an numpy array

  redify_picture =  255 * picture

  return redify_picture #numpy array

#redblack_picture filters all non red pixels
def redblack_picture(picture): #picture need to be a jpg image

  redblack_picture = white_to_red(np.array(picture))

  for line in redblack_picture:
    for pixel in line:
      
      if pixel[0] < pixel[1] or pixel[0] < pixel[2]:
        pixel[0] = 0
        pixel[1] = 0
        pixel[2] = 0
      elif np.sum(pixel) > 500:
        pixel[0] = 0
        pixel[1] = 0
        pixel[2] = 0

  return redblack_picture #Numpy array


# embeding mix the original picture and the red & black picture
def embeding(picture_path): #picture_path is the path to the image folder  (string)
  picture = Image.open(picture_path)

  img_parent_array = np.array(picture)
  img_child_array = redblack_picture(picture)


  raw_number = picture.size[1]
  column_number = picture.size[0]
  
  finale_img =  np.array(picture)

  line = 0; pixel =-1

  while line < raw_number:

      while pixel < column_number:
        if np.sum(img_child_array[line][pixel]) == 0 :# or line > column_number*0.9526 #95.26% are mixed, 5% is the bottom of the image to keeep the legend ne marche plus et plus utile avec le resizing
          finale_img[line][pixel][0] = img_parent_array[line][pixel][0]
          finale_img[line][pixel][1] = img_parent_array[line][pixel][1]
          finale_img[line][pixel][2] = img_parent_array[line][pixel][2]

          pixel +=1
        else:

          finale_img[line][pixel][0] = img_child_array[line][pixel][0]
          finale_img[line][pixel][1] = img_child_array[line][pixel][1]
          finale_img[line][pixel][2] = img_child_array[line][pixel][2]

          pixel+=1
      pixel = 0
      line+=1
 

  finale_img = Image.fromarray(finale_img)

  return finale_img #image jpg