from PIL import Image
## Functions

def top(pixel):
    red = pixel[0]
    green = pixel[1]
    blue = pixel [2]
   
    newRed = red*2
    if newRed > 255:
        newRed = 255
    newGreen = green
    if newGreen > 255:
        newGreen = 255
    newBlue = blue
    if newBlue > 255:
       newBlue = 255

    p = (newRed, newGreen, newBlue)
    newPixelList.append(p)


def middle(pixel):
    red = pixel[0]
    green = pixel[1]
    blue = pixel [2]

    avg = int((red + blue + green) // 3)

    newRed = avg
    if newRed > 255: 
        newRed = 255
    newGreen = avg
    if newGreen > 255:
        newGreen = 255
    newBlue = avg
    if newBlue > 255:
       newBlue = 255

    p = (newRed, newGreen, newBlue)
    newPixelList.append(p)

def bottom(pixel):
    red = pixel[0]
    green = pixel[1]
    blue = pixel [2]

    newRed = red
    if newRed > 255:
        newRed = 255
    newGreen = green
    if newGreen > 255:
        newGreen = 255
    newBlue = blue*2
    if newBlue > 255:
       newBlue = 255

    p = (newRed, newGreen, newBlue)
    newPixelList.append(p)


##RUNNINGCODE
#Import the image and make pizel list
myImage = Image.open("ele2.jpg")
imageData = myImage.getdata() #information of the picture-- pixels
pixelList = list(imageData)

newPixelList = []

length = len(pixelList)
top1 = length // 3
middle1 = (2 * length ) // 3
bottom1 = length 

counter = 0

#pixel manipulation
for pixel in pixelList:
    red = pixel[0]
    green = pixel[1]
    blue = pixel [2]

    counter += 1

    if (counter < top1):
        top(pixel)

    elif (top1 <= counter < middle1 ):
        middle(pixel)

    elif (middle1 <= counter < bottom1):
        bottom(pixel)

##    else:
##        negative(pixel)
##    counter += 1


##    newRed = red*2
##    if newRed > 255:
##        newRed = 255
##    newGreen = green*2
##    if newGreen > 255:
##        newGreen = 255
##    newBlue = blue*2
##    if newBlue > 255:
##        newBlue = 255

    #p = (newRed, newGreen, newBlue)




#add pixel to new pixel list
    #newPixelList.append(p)


#open the image
newImage = Image.new("RGB", myImage.size)
newImage.putdata(newPixelList)
newImage.show()
#newImage.save("newPhoto.jpeg", "jpeg")
