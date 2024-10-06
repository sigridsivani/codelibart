from os import listdir, path
import random
from PIL import Image

files = listdir("collage")


if len(files) >= 3:
    random_files = random.sample(files, 3)
    #making sure we are chosing 3 different files

img1 = Image.open( path.join("collage", random_files[0]))
img2 = Image.open( path.join("collage", random_files[1]))
img3 = Image.open( path.join("collage", random_files[2]))

img = Image.new ("RGBA", (400,400), (0,0,0,0))


img1.thumbnail((400,400)) 
img1 = img1.convert('RGBA')
img2.thumbnail((400,400))
img2 = img2.convert('RGBA')
img3.thumbnail((400,400))
img3 = img3.convert('RGBA')

def isolate_color(image, target_color):
    pixels = image.getdata()
    #get image data as list

    new_pixels = []
    #new list to hold updates pixels 

    for pixel in pixels:
        r, g, b, a = pixel

        if target_color == 'red':
            new_pixel = (r, g, b, a)if r > 128  else (0, 0, 0, 0)
       #keeping red pixels and make the rest transparent
        elif target_color == 'green':
            new_pixel = (r, g, b, a)if g > 128 else (0, 0, 0, 0)
        #same with green
        elif target_color == 'blue':
            new_pixel = (r, g, b, a)if b > 128 else (0, 0, 0, 0)

        new_pixels.append(new_pixel)
        #adds the new pixels into list

    isolated_image = Image.new('RGBA', image.size)
    isolated_image.putdata(new_pixels)
    #convert pixel data into image

    return isolated_image

red_isolated = isolate_color(img1, 'red')
green_isolated = isolate_color(img2, 'green')
blue_isolated = isolate_color(img3, 'blue')

img.paste(red_isolated, (0,0), red_isolated) #transperancy mask 
img.paste(green_isolated, (0,0), green_isolated) #transperancy mask
img.paste(blue_isolated, (0,0), blue_isolated) #transperancy mask
#pasting the different isolated colors onto original new image

img.save('newalg2test.png')

