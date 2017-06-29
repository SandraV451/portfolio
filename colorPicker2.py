from PIL import Image

def azulMarino(pixel):
    red = pixel[0]
    green = pixel[1]
    blue = pixel [2]

    newRed = 0
    newGreen = 51
    newBlue = 76
    

    p = (newRed, newGreen, newBlue)
    newPixelList.append(p)
    
def rojo(pixel):
    red = pixel[0]
    green = pixel[1]
    blue = pixel [2]

    newRed = 217
    newGreen = 26
    newBlue = 33

    p = (newRed, newGreen, newBlue)
    newPixelList.append(p)

def azulClaro(pixel):
    red = pixel[0]
    green = pixel[1]
    blue = pixel [2]

    newRed = 112
    newGreen = 150
    newBlue = 158

    p = (newRed, newGreen, newBlue)
    newPixelList.append(p)

def amarillo(pixel):
    red = pixel[0]
    green = pixel[1]
    blue = pixel [2]

    newRed = 252
    newGreen = 227
    newBlue = 166

    p = (newRed, newGreen, newBlue)
    newPixelList.append(p)
    

#Import the image and make pizel list
myImage = Image.open("billNye.jpg")
imageData = myImage.getdata() #information of the picture-- pixels
pixelList = list(imageData)

newPixelList = []


#pixel manipulation
for pixel in pixelList:
    red = pixel[0]
    green = pixel[1]
    blue = pixel [2]

    intensity = red + green + blue

    if (intensity < 182):
        azulMarino(pixel)
        
    elif (182 <= intensity < 364):
        rojo(pixel)

    elif (364 <= intensity < 546):
        azulClaro(pixel)

    elif (intensity >= 546):
        amarillo(pixel)








#open the image
newImage = Image.new("RGB", myImage.size)
newImage.putdata(newPixelList)
newImage.show()
newImage.save("newPhoto.jpg", "jpg")
