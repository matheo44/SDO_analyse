import numpy as np
from PIL import Image

#resizing prende l'image et deux point puis créer une image avec tout les pixels entre ces points


def resizing(picture_path, target1, target2, nom_img):
    
    picture = Image.open(picture_path)
    picture = np.array(picture)

    raw_px = target1[0]; column_px = target1[1];
    resized_img = []
    #print(raw_px, target2[0], '-----------------------------')
    while raw_px < target2[0]:

        column_px = target1[1]
        line = []

        while column_px < target2[1]:
            line.append(picture[raw_px][column_px].tolist())
            column_px +=1
        raw_px += 1
        #print(picture)

        resized_img.append(line)

    #coversion de l'image array -> jpg
    #print(resized_img)
    img = np.array(resized_img, dtype=np.uint8)
    
    return Image.fromarray(img).save("resized_img/"+nom_img)


#resizing("rush/20250329_200544_4096_0131.jpg", [800,100], [900,1000], "20250329_200544_4096_0131.jpg")

