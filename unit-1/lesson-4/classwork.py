import sys
from PIL import Image 

# if len(sys.argv) != 2:
#     exit("This program requires one argument: the name of the image file that will be created.")

# # Make a new 10x10 image
# img = Image.new("RGB", (10,10) )

# img.save(sys.argv[1])

# if len(sys.argv) != 2:
#     exit("This program requires one argument: the name of the image file that will be created.")

# # Make a new 10x10 image
# img = Image.new("RGB", (10,10) )

# data = []
# for i in range(100):
#     pixel = (i, 0, 0)
#     data.append( pixel )

# img.putdata(data)

# img.save(sys.argv[1])

# import sys
# from PIL import Image 

# if len(sys.argv) != 2:
#     exit("This program requires one argument: the name of the image file that will be created.")

# # Make a new 400x400 image
# img = Image.new("RGB", (400,400) )

# data = []
# for i in range(160000):
#     pixel = (i, 0, 255-i)
#     data.append( pixel )

# img.putdata(data)

# img.save(sys.argv[1])

# for i in range(255):
#     print(i % 255)


# if len(sys.argv) != 2:
#     exit("This program requires one argument: the name of the image file that will be created.")

# # Make a new 400x400 image
# img = Image.new("RGB", (400,400) )

# for y in range(400):

#     for x in range(400):

#         pixel = (x % 255, 0, y % 255)
#         img.putpixel( (x,y), pixel )

# img.save(sys.argv[1])


# import sys
# from PIL import Image 

# if len(sys.argv) != 2:
#     exit("This program requires one argument: the name of the image file that will be created.")

# # Make a new 400x400 image
# img = Image.new("RGB", (400,400) )

# for y in range(400):

#     for x in range(400):

#         r = 0
#         b = 0
#         if x % 50 == 0:
#             b = 255
            
#         if y % 20 == 0:
#             r = 255

#         if y % 30 == 0:
#             r = 255
#             b = 255

#         pixel = (r, 0, b)
#         img.putpixel( (x,y), pixel )

# img.save(sys.argv[1])

import sys
from PIL import Image 

if len(sys.argv) != 2:
    exit("This program requires one argument: the name of the image file that will be created.")

# Make a new 400x400 image
img = Image.new("RGB", (400,400) )

for y in range(400):

    for x in range(400):

        r = 0
        g = 0
        b = 0
        if x % 50 > 25:
            r = 255

        if y % 50 > 25:
            b = 255

        if x % 100 > 50 and y % 100 > 50:
            g = 255

        pixel = (r, g, b)
        img.putpixel( (x,y), pixel )

img.save(sys.argv[1])