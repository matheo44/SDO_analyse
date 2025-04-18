
import os
import time

from PIL import ImageDraw
from PIL import ImageFont

from data_cleaning  import data_cleaning 
from processing import embeding
from resizing import resizing
#from recorde import create_video_from_images

start_processing = time.time()

directory = './rush'
directory_resized = "./resized_img"
resize = True
target1 = [1260,2475]
target2 = [2483,3896]
special_event = "Sunspot 4045 M3.1"

#data_cleaning(directory)

number_of_images = len(os.listdir(directory))

average_time = 0; img_processed = 0

for image in os.listdir(directory):
    
    img_processed+=1
    start_embeding = time.time()

    if(".jpg") in (directory+'/'+image):

      if resize:
        resizing(directory+'/'+image,target1,target2,image )
        result = embeding(directory_resized+'/'+image)
                 #write the metadata on the picture
        text = "Colorized SDO/AIA 131 "+image[0:4]+"-"+image[4:6]+"-"+image[6:8]+" "+image[9:11]+":"+image[11:13]+":"+image[13:15]+" UTC "+ special_event
        font = ImageFont.truetype("times-bo.ttf", 35)
        draw = ImageDraw.Draw(result)
        draw.text((50,30), text,font=font)
        result.save('result/'+image)
        #os.remove(directory_resized+'/'+image)
        #os.remove(directory+'/'+image)

      else:
         result = embeding(directory+'/'+image)
         result.save('result/'+image)
         os.remove(directory+'/'+image)

      end_embeding = time.time()
      average_time += end_embeding - start_embeding
      print(img_processed,'/', number_of_images, '(',(img_processed*100)/number_of_images,'%)',round(average_time,2), end='\r')
    
print('\n average time processing', average_time/number_of_images)

end_processing = time.time()

print('time of processing', end_processing - start_processing)

