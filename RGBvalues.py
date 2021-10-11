import sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageColor
import numpy as np
from numpy import array

from PIL.ImageFilter import (
    BLUR, CONTOUR, DETAIL, EDGE_ENHANCE, EDGE_ENHANCE_MORE,
    EMBOSS, FIND_EDGES, SMOOTH, SHARPEN
)


arr = np.zeros([150, 250, 3], dtype=np.uint8)
arr[:,:100] = [255, 128, 0]
arr[:,100:] = [0, 0, 255]
img = Image.fromarray(arr)
img.show()


arr = np.zeros([150,300], dtype=np.uint8)
#Set grey value to black or white depending on x position
for x in range(300):
    for y in range(150):
        if (x % 16) // 8 == (y % 16)//8:
            arr[y, x] = 0
        else:
            arr[y, x] = 255
img = Image.fromarray(arr)
img.show()


#Open Image & create image object
img = Image.open('static/assets/exciteddog.jpeg')
#Show actual image
img.show()
#Convert an image to numpy array
img2arr = array(img)
#Print the array
print(img2arr)
#Convert numpy array back to image
arr2im = Image.fromarray(img2arr)
#Display image
arr2im.show()


img = Image.open('static/assets/exciteddog.jpeg')
d1 = ImageDraw.Draw(img)
d1.text((28, 36), "Hello, TutorialsPoint!", fill=(255, 0, 0))
img.show()


img = Image.new('RGB', (500, 300), (125, 125, 125))
draw = ImageDraw.Draw(img)
draw.line((200, 100, 300, 200), fill=(0, 0, 0), width=10)
img.show()


img = Image.new('RGB', (500, 300), (125, 125, 125))
draw = ImageDraw.Draw(img)
draw.ellipse((200, 125, 300, 200), fill=(255, 0, 0), outline=(0, 0, 0))
img.show()


img = Image.new('RGB', (500, 300), (125, 125, 125))
draw = ImageDraw.Draw(img)
draw.rectangle(
    (200, 125, 300, 200),
    fill=(255, 0, 0),
    outline=(0, 0, 0))
img.show()


img = Image.new('RGB', (500, 300), (125, 125, 125))
draw = ImageDraw.Draw(img)
draw.polygon(
    ((200, 200), (300, 100), (250, 50)),
    fill=(255, 0, 0),
    outline=(0, 0, 0))
img.show()


#Create Image object
im = Image.open("static/assets/exciteddog.jpeg")
#Draw line
draw = ImageDraw.Draw(im)
draw.line((0, 0) + im.size, fill=128)
draw.line((0, im.size[1], im.size[0], 0), fill=128)
#Show image
im.show()


# using getrgb
img = ImageColor.getrgb("blue")
print(img)
img1 = ImageColor.getrgb("purple")
print(img1)


# Create new image & get color RGB tuple.
img = Image.new("RGB", (256, 256), ImageColor.getrgb("#add8e6"))
#Show image
img.show()


# using getrgb
img = ImageColor.getrgb("skyblue")
print(img)
img1 = ImageColor.getrgb("purple")
print(img1)


#Create image object
img = Image.open('static/assets/mountain.jpeg')
#Applying the blur filter
img1 = img.filter(SMOOTH)
img1.show()


#Create image object
img = Image.open('static/assets/mountain.jpeg')
#Applying the blur filter
img1 = img.filter(SHARPEN)
img1.show()


#Create image object
img = Image.open('static/assets/mountain.jpeg')
#Applying the blur filter
img1 = img.filter(SHARPEN)
img1.show()


#Create image object
img = Image.open('static/assets/mountain.jpeg')
#Applying the blur filter
img1 = img.filter(BLUR)
img1.show()


#Create image object
img = Image.open('static/assets/mountain.jpeg')
#Applying the blur filter
img1 = img.filter(CONTOUR)
img1.show()


#Create image object
img = Image.open('static/assets/mountain.jpeg')
#Applying the blur filter
img1 = img.filter(DETAIL)
img1.show()


#Create image object
img = Image.open('static/assets/mountain.jpeg')
#Applying the blur filter
img1 = img.filter(EDGE_ENHANCE)
img1.show()


#Create image object
img = Image.open('static/assets/mountain.jpeg')
#Applying the blur filter
img1 = img.filter(EDGE_ENHANCE_MORE)
img1.show()


#Create image object
img = Image.open('static/assets/mountain.jpeg')
#Applying the blur filter
img1 = img.filter(EMBOSS)
img1.show()


#Create image object
img = Image.open('static/assets/mountain.jpeg')
#Applying the blur filter
img1 = img.filter(FIND_EDGES)
img1.show()


im = Image.open('static/assets/mountain.jpeg')
im1 = im.filter(ImageFilter.BLUR)
im1.show()
im2 = im.filter(ImageFilter.MinFilter(3))
im2.show()
im3 = im.filter(ImageFilter.MinFilter) # same as MinFilter(3)
im3.show()


#Simple blur
#Open existing image
OriImage = Image.open('static/assets/mountain.jpeg')
blurImage = OriImage.filter(ImageFilter.BLUR)
blurImage.show()


#Open existing image
OriImage = Image.open('static/assets/mountain.jpeg')
#Applying BoxBlur filter
boxImage = OriImage.filter(ImageFilter.BoxBlur(5))
boxImage.show()


#Open existing image
OriImage = Image.open('static/assets/mountain.jpeg')
#Applying GaussianBlur filter
gaussImage = OriImage.filter(ImageFilter.GaussianBlur(5))
gaussImage.show()


#Using Image Module
#Open image using Image module
im = Image.open("static/assets/mountain.jpeg")
#Show rotated Image
im = im.rotate(45)
im.show()


#Flip and Rotate Images
# Open an already existing image
imageObject = Image.open("static/assets/mountain.jpeg")
# Do a flip of left and right
hori_flippedImage = imageObject.transpose(Image.FLIP_LEFT_RIGHT)
# Show the original image
# Show the horizontal flipped image
hori_flippedImage.show()


# Open an already existing image
imageObject = Image.open("static/assets/mountain.jpeg")
# Do a flip of left and right
hori_flippedImage = imageObject.transpose(Image.FLIP_LEFT_RIGHT)
# Show the original image
#show 90 degree flipped image
degree_flippedImage = imageObject.transpose(Image.ROTATE_90)
degree_flippedImage.show()


# Open an already existing image
imageObject = Image.open("static/assets/mountain.jpeg")
# Do a flip of left and right
hori_flippedImage = imageObject.transpose(Image.FLIP_LEFT_RIGHT)
# Show the original image
# Show vertically flipped image
Vert_flippedImage = imageObject.transpose(Image.FLIP_TOP_BOTTOM)
Vert_flippedImage.show()


#Resizing an Image
#Create an Image Object from an Image
im = Image.open("static/assets/mountain.jpeg")
#Make the new image half the width and half the height of the original image
resized_im = im.resize((round(im.size[0]*0.5), round(im.size[1]*0.5)))
#Display the resized imaged
resized_im.show()
#Save the cropped image


image = Image.open("static/assets/mountain.jpeg")
r, g, b = image.split()
image = Image.merge("RGB", (b, g, r))
image.show()


#Creating a Watermark
#Create an Image Object from an Image
im = Image.open('static/assets/mountain.jpeg')
width, height = im.size
draw = ImageDraw.Draw(im)
text = "sample watermark"
font = ImageFont.truetype('arial.ttf', 36)
textwidth, textheight = draw.textsize(text, font)
# calculate the x,y coordinates of the text
margin = 10
x = width - textwidth - margin
y = height - textheight - margin
# draw watermark in the bottom right corner
draw.text((x, y), text, font=font)
im.show()


#Read the two images
image1 = Image.open('static/assets/black.png')
image1.show()
image2 = Image.open('static/assets/blue.png')
image2.show()
#resize, first image
image1 = image1.resize((426, 240))
image2 = image2.resize((426, 240))
image1_size = image1.size
image2_size = image2.size
new_image = Image.new('RGB',(2*image1_size[0], image1_size[1]), (250,250,250))
new_image.paste(image1,(0,0))
new_image.paste(image2,(image1_size[0],0))
new_image.show()


#Create an Image Object from an Image
im = Image.open('static/assets/mountain.jpeg')
#Display actual image
im.show()
#left, upper, right, lowe
#Crop
cropped = im.crop((1,2,100,100))
#Display the cropped portion
cropped.show()







