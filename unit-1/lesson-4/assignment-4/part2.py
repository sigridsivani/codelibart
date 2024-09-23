import sys
from PIL import Image 


if len(sys.argv) <= 4:
    exit("This program requires more than four arguments: the name of four or more image files to combine.")


img1 = Image.open( sys.argv[1] )
img2 = Image.open( sys.argv[2] )
img3 = Image.open( sys.argv[3] )
img4 = Image.open( sys.argv[4] )



# new_image = Image.new( "RGB", (800,800), "white" )


# new_image.paste(img1, (0,0) )


# new_image.paste(img2, (400,0) )

# new_image.paste(img3, (0,400))
# new_image.paste(img4, (400,400))


# new_image.save("part2pic1.jpg")

#copied in from lesson-4 and then modified for 4 arguments

new_img = Image.new( "RGBA", (600,600), (0,0,0,0) )

img1.thumbnail( (400,400) )
img2.thumbnail( (400,400) )
img3.thumbnail( (400,400) )
img4.thumbnail( (400,400) )

new_img.paste(img1, (0,0))

img2.putalpha(128)
new_img.alpha_composite(img2, (200,50))

img3.putalpha(200)

new_img.alpha_composite(img3, (20,300))
new_img.paste(img4, (300,450))

new_img.save("part2pic3.png")

