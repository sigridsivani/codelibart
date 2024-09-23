# from PIL import Image
# import random 

# width = 100
# height = 100

# img = Image.new("HSV" , (width,height) , (0,0,0))

# for y in range(height):
#     for x in range(width):
        
        
#         r = random.random()
        
#         if r > .9:
            
#             img.putpixel( (x,y), (240,255,255) )

#     img = img.convert("RGB")

#  img.save("so-less-random.png")

from os import listdir, path
import random
from PIL import Image


files = listdir("images")
# files.remove(".DS_Store")

random_file = random.choice(files)

img = Image.open( path.join("images",random_file) )

