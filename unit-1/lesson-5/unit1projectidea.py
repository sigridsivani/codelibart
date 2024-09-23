from os import listdir, path
import random
from PIL import Image

# create dir of random images 
#code1 - take bright pixels of one image and dark pixels of another image and merge into one picture
# files = listdir("random_images")


# random_file = random.choice(files)

# img1 = Image.open( path.join("images",random_file) )
# img2 = Image.open( path.join("images",random_file) )

# img1_hsv = img1.convert(mode="HSV")
# img1_hsv_data = img1_hsv.getdata()
# new_img1_data = []

# for p in img1_hsv_data:
#     if p[2] < 50:
#         new_img1_data.append( (255,255,255) )
#     else:
#         new_img1_data.append(p)
 #replace (255,255,255) with the transperency if possible

# img2_hsv = img2.convert(mode="HSV")
# img2_hsv_data = img2_hsv.getdata()
# for p in img2_hsv_data:
#     if p[2] > 50:
#         new_img2_data.append( (255,255,255) )
#     else:
#         new_img2_data.append(p)
 #replace (255,255,255) with the transperency if possible

#  new_img = Image.blend(img1,img2,.5)

# new_img.save("newimage.jpg")