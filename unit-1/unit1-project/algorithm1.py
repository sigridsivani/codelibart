from os import listdir, path
import random
from PIL import Image
import sys

files = listdir("collage")


if len(files) >= 2:
    random_files = random.sample(files, 2)
    #making sure we are chosing 2 different files

img1 = Image.open( path.join("collage", random_files[0]))
img2 = Image.open( path.join("collage", random_files[1]))

img = Image.new ("RGBA", (400,400), (0,0,0,0))


img1.thumbnail((400,400))
img1 = img1.convert('RGBA')
img2.thumbnail((400,400))
img2 = img2.convert('RGBA')

pixels1 = img1.load()
pixels2 = img2.load()
#getting the pixel data from both images
width, height = img1.size 

for x in range(width):
    for y in range(height):
        r1, g1, b1, a1 = pixels1[x,y]

        brightness1 = (0.299 * r1 + 0.587 * g1 + 0.114 * b1)
        #calculating brightness for image1, copied from stack, formula to determine percieved brightness of RGB

        if brightness1 < 128: 
            pixels1[x,y] = (r1, g1, b1, 0)
        else: 
            pixels1[x,y] = (r1, g1, b1, 255)
        #128 is 50% brightness, so if it is smaller than 50% it will be 0 alpha and if not 255 alpha

        r2, g2, b2, a2 = pixels2[x,y]
        brightness2 = (0.299 * r2 + 0.587 * g2 + 0.114 * b2)
        
        if brightness2 >= 128:
            pixels2[x,y] = (r2, g2, b2, 0)
        else:
            pixels2[x,y] = (r2, g2, b2, 255)
            
        #same formula but opposite on img2

img.paste(img1, (0,0), img1)
img.paste(img2, (0,0), img2)

img.save('alg1_collage3.png')


