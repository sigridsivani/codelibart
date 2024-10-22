from os import listdir, path
from PIL import Image, ExifTags
import sys

files = listdir("images")
img = Image.open(path.join("images" , "screenshot.png"))
exifData = img.getexif()

print(exifData)
for key in img.getexif().keys():
    print(key, ExifTags.TAGS[key])

 #had to export my .HEIC photo to png
 # results for iphone pic:
 #    {322: 512, 323: 512, 34853: 2486, 296: 2, 34665: 252, 271: 'Apple', 272: 'iPhone 14 Plus', 305: '17.6.1', 274: 1, 306: '2024:10:13 14:07:28', 282: 72.0, 283: 72.0, 316: 'iPhone 14 Plus'}
# 322 TileWidth
# 323 TileLength
# 34853 GPSInfo
# 296 ResolutionUnit
# 34665 ExifOffset
# 271 Make
# 272 Model
# 305 Software
# 274 Orientation
# 306 DateTime
# 282 XResolution
# 283 YResolution
# 316 HostComputer

# results for digital camera:
# {296: 2, 282: 72.0, 34665: 288, 270: 'KODAK Digital Still Camera     ', 271: 'JK Imaging, Ltd.       ', 272: 'KODAK PIXPRO FZ55', 305: '1.05                           ', 274: 1, 306: '2024:09:13 01:50:23', 531: 2, 283: 72.0}
# 296 ResolutionUnit
# 34665 ExifOffset
# 270 ImageDescription
# 271 Make
# 272 Model
# 305 Software
# 274 Orientation
# 306 DateTime
# 531 YCbCrPositioning
# 282 XResolution
# 283 YResolution

#wanted to see if a screenshot produced a different result:
# {34665: 38, 274: 1}
# 34665 ExifOffset
# 274 Orientation
# it did! a lot shorter too


#Im taking a beyond sex and gender class where we are talking alot about epistimologies and hermeneutical disadvantages in society, and I was thinkign that it feels very relevant to what we have been learning about data sets. Im not sure yet where i want to go with it but I think it could be interesting to explore for my unit-2 project, maybe something about analysing texts or datasets to demonstrate how women have been epistimologically silenced and how the female perspective has been neglected. 