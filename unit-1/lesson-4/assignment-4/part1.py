import sys
from PIL import Image 

if len(sys.argv) != 2:
    exit("This program requires one argument: the name of the image file that will be created.")

img = Image.new("RGB", (400,400) )

# for y in range(400):

#     for x in range(400):

#         r = 0
#         b = 0
#         if x % 20 == 0:
#             b = 90
            
#         if y % 50 == 0:
#             r = 150

#         if y % 60 == 0:
#             r = 80
#             b = 70

#         pixel = (r, 0, b)
#         img.putpixel( (x,y), pixel )

# img.save(sys.argv[1])
#copied and pasted from lesson-4 and changed the values



# for y in range(400):

#     for x in range(400):

#         r = 100
#         g = 0
#         b = 5
#         if x % 50 > 20:
#             r = 100

#         if y % 50 > 25:
#             b = 0

#         if x % 100 > 70 and y % 100 > 30:
#             g = 40

#         pixel = (r, g, b)
#         img.putpixel( (x,y), pixel )

# img.save(sys.argv[1])

#also from lesson-4 
for y in range(400):

    for x in range(400):

        r = 0
        g = 10
        b = 0
        if x % 50 > 20:
            r = 20

        if y % 50 > 40:
            b = 20

        if x % 50 > 70 and y % 100 > 30:
            g = 255

        pixel = (r, g, b)
        img.putpixel( (x,y), pixel )

img.save(sys.argv[1])
