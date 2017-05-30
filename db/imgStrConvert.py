import base64


#Converting image to string
def imgToStr(image):
    with open(image,"rb") as imageFile:
        str = base64.b64encode(imageFile.read())
        print str
        return str

imgToStr("randImg.png")


#Converting string to image
def strToImg(imageText):
    #fh = open("imageToSave.png","wb")
   # fh.write(imageText.decode('base64'))
    print imageText.decode('base64')
    return imageText.decod('base64')
    #fh.close()

strToImg(imgToStr("randImg.png"))
#THEY BOTH WORK....how will we display image though? I dont want to create a new image everytime we open up the string of it...possibly just return to the decode portion
