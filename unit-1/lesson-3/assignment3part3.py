import sys
from PIL import Image


if len(sys.argv) != 3:
    exit("This command requires two arguments : two different file names")

img1 = Image.open( sys.argv[1] )
img2 = Image.open( sys.argv[2] )

blended_img = Image.blend(img1,img2,.5)

blended_img.save("blended3.jpg")