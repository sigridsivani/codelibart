import sys
from PIL import Image


if len(sys.argv) != 3:
    exit("This command requires one argument: the name of an image file and a number")

img = Image.open( sys.argv[1] )
#copied from lesson 3

rotated_img = img.rotate( int(sys.argv[2]) )
rotated_img.save("rotated-" + sys.argv[1])



