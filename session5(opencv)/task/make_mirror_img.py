import cv2 as cv
import numpy as np
# read the image
img = cv.imread('Images/acnee.jpg')
cv.imshow("Chatbot",img)

# create a empty image
blank_img = np.zeros((img.shape),dtype='uint8')
cv.imshow("blank_img",blank_img)


# change the color of the blank image to the original image
pixel_color = img[50,50]
# blank_img[:] = pixel_color
cv.imshow("blank_img",blank_img) 

# extract the bot from image
bot = img[:,img.shape[1]//2:]
# cv.imshow("bot",bot)

# rotate the image to get the mirror image
rotated_bot = cv.flip(bot,1)
# cv.imshow("rotated_bot",rotated_bot)


# apply bitwise operation with blank image
blank_img[:,:bot.shape[1]] = rotated_bot
blank_img[:,bot.shape[1]:] = bot

# place text on the image
cv.putText(blank_img,"Brother Bot",(blank_img.shape[0]//2,blank_img.shape[1]//2),cv.FONT_HERSHEY_COMPLEX,1.0,(0,0,0),2)
cv.imshow("Mirror_bot",blank_img)
cv.waitKey(0)