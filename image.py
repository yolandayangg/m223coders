from PIL import Image, ImageFilter, ImageDraw, ImageFont, ImageColor

#Import all the enhancement filter from pillow

from PIL.ImageFilter import (
    BLUR, CONTOUR, DETAIL, EDGE_ENHANCE, EDGE_ENHANCE_MORE,
    EMBOSS, FIND_EDGES, SMOOTH, SHARPEN
)

#Using Image Module
#Open image using Image module
im = Image.open("static/assets/mountain.jpeg")
#Show actual Image
im.show()
#Show rotated Image
im = im.rotate(45)
im.show()

#Working with Images
image = Image.open('static/assets/mountain.jpeg')
image.show()
image.save('beach1.bmp')
image1 = Image.open('beach1.bmp')
image1.show()

#Flip and Rotate Images
# Open an already existing image
imageObject = Image.open("static/assets/mountain.jpeg")
# Do a flip of left and right
hori_flippedImage = imageObject.transpose(Image.FLIP_LEFT_RIGHT)
# Show the original image
imageObject.show()
# Show the horizontal flipped image
hori_flippedImage.show()

# Open an already existing image
imageObject = Image.open("static/assets/mountain.jpeg")

# Do a flip of left and right
hori_flippedImage = imageObject.transpose(Image.FLIP_LEFT_RIGHT)

# Show the original image
imageObject.show()

# Show vertically flipped image
Vert_flippedImage = imageObject.transpose(Image.FLIP_TOP_BOTTOM)
Vert_flippedImage.show()


#Resizing an Image
#Create an Image Object from an Image
im = Image.open("static/assets/mountain.jpeg")
#Display actual image
im.show()
#Make the new image half the width and half the height of the original image
resized_im = im.resize((round(im.size[0]*0.5), round(im.size[1]*0.5)))
#Display the resized imaged
resized_im.show()
#Save the cropped image
resized_im.save('resizedBeach1.jpg')


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
#Save watermarked image
im.save('images/watermark.jpg')


#Colors on an Image
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


#ImageDraw Module
#Create Image object
im = Image.open("static/assets/mountain.jpeg")

#Draw line
draw = ImageDraw.Draw(im)
draw.line((0, 0) + im.size, fill=128)
draw.line((0, im.size[1], im.size[0], 0), fill=128)

#Show image
im.show()

# get an image
base = Image.open('static/assets/mountain.jpeg').convert('RGBA')

# make a blank image for the text, initialized to transparent text color
txt = Image.new('RGBA', base.size, (255,255,255,0))

# get a font
fnt = ImageFont.truetype('E:/PythonPillow/Fonts/Pacifico.ttf', 40)

# get a drawing context
d = ImageDraw.Draw(txt)

# draw text, half opacity
d.text((14,14), "Tutorials", font=fnt, fill=(255,255,255,128))

# draw text, full opacity
d.text((14,60), "Point", font=fnt, fill=(255,255,255,255))
out = Image.alpha_composite(base, txt)

#Show image
out.show()

img = Image.new('RGB', (500, 300), (125, 125, 125))
draw = ImageDraw.Draw(img)
draw.line((200, 100, 300, 200), fill=(0, 0, 0), width=10)

img.show()



#Image Sequences
img = Image.open('static/assets/mountain.jpeg')
#Skip to the second frame
img.seek(1)
try:
    while 1:
        img.seek(img.tell() + 1)
        #do_something to img
except EOFError:
    #End of sequence
    pass

#Adding Filters to an image
im = Image.open('static/assets/mountain.jpeg')
im1 = im.filter(ImageFilter.BLUR)
im1.show()
im2 = im.filter(ImageFilter.MinFilter(3))
im2.show()
im3 = im.filter(ImageFilter.MinFilter) # same as MinFilter(3)
im3.show()
ImageFilter.MinFilter(size=3)
#Create image object
img = Image.open('static/assets/mountain.jpeg')
#Applying the blur filter
img1 = img.filter(BLUR)
img1.save('images/ImageFilter_blur.jpg')
img1.show()
#Create image object
img = Image.open('static/assets/mountain.jpeg')
#Applying the blur filter
img1 = img.filter(CONTOUR)
img1.save('images/ImageFilter_blur.jpg')
img1.show()
#Create image object
img = Image.open('static/assets/mountain.jpeg')
#Applying the blur filter
img1 = img.filter(DETAIL)
img1.save('images/ImageFilter_blur.jpg')
img1.show()
#Create image object
img = Image.open('static/assets/mountain.jpeg')
#Applying the blur filter
img1 = img.filter(EDGE_ENHANCE)
img1.save('images/ImageFilter_blur.jpg')
img1.show()
#Create image object
img = Image.open('static/assets/mountain.jpeg')
#Applying the blur filter
img1 = img.filter(EDGE_ENHANCE_MORE)
img1.save('images/ImageFilter_blur.jpg')
img1.show()
#Create image object
img = Image.open('static/assets/mountain.jpeg')
#Applying the blur filter
img1 = img.filter(EMBOSS)
img1.save('images/ImageFilter_blur.jpg')
img1.show()
#Create image object
img = Image.open('static/assets/mountain.jpeg')
#Applying the blur filter
img1 = img.filter(FIND_EDGES)
img1.save('images/ImageFilter_blur.jpg')
img1.show()
#Create image object
img = Image.open('static/assets/mountain.jpeg')
#Applying the blur filter
img1 = img.filter(SMOOTH)
img1.save('images/ImageFilter_blur.jpg')
img1.show()
#Create image object
img = Image.open('static/assets/mountain.jpeg')
#Applying the blur filter
img1 = img.filter(SHARPEN)
img1.save('images/ImageFilter_blur.jpg')
img1.show()
#Create image object
img = Image.open('static/assets/mountain.jpeg')
#Applying the blur filter
img1 = img.filter(SHARPEN)
img1.save('images/ImageFilter_blur.jpg')
img1.show()


#Merging two Images
#Read the two images
image1 = Image.open('static/assets/mountain.jpeg')
image1.show()
image2 = Image.open('static/assets/ncs_logo.png')
image2.show()
#resize, first image
image1 = image1.resize((426, 240))
image1_size = image1.size
image2_size = image2.size
new_image = Image.new('RGB',(2*image1_size[0], image1_size[1]), (250,250,250))
new_image.paste(image1,(0,0))
new_image.paste(image2,(image1_size[0],0))
new_image.save("images/merged_image.jpg","JPEG")
new_image.show()

#Blur an Image
#Import required Image library
#Open existing image
OriImage = Image.open('static/assets/mountain.jpeg')
OriImage.show()


#Merging Images
image = Image.open("static/assets/mountain.jpeg")
r, g, b = image.split()
image.show()
image = Image.merge("RGB", (b, g, r))
image.show()
blurImage = OriImage.filter(ImageFilter.BLUR)
blurImage.show()
#Save blurImage
blurImage.save('images/simBlurImage.jpg')

#Create an Image Object from an Image
im = Image.open('static/assets/mountain.jpeg')

#Display actual image
im.show()

#left, upper, right, lowe
#Crop
cropped = im.crop((1,2,300,300))

#Display the cropped portion
cropped.show()

#Save the cropped image
cropped.save('images/croppedBeach1.jpg')

#Creating Thumbnails
def tnails():
    try:
        image = Image.open('images/cat.jpg')
        image.thumbnail((90,90))
        image.save('images/thumbnail.jpg')
        image1 = Image.open('images/thumbnail.jpg')
        image1.show()
    except IOError:
        pass
tnails()