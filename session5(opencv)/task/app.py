import cv2 as cv

# read the image
img = cv.imread('Images/chatbot.jpg')
cv.imshow("Chatbot",img)

# resize the image
resize_img = cv.resize(img,(300,300),interpolation=cv.INTER_AREA)
cv.imshow("resize_bot",resize_img)

# crop the image 
print(img.shape)
crop_img = img[50:-70,250:-50]
cv.imshow("crop_bot",crop_img)


# convert to grayscale
gray_img = cv.cvtColor(crop_img,cv.COLOR_BGR2GRAY)
cv.imshow("Grawy Bot",gray_img)


# rotate the image
def rotate_img(image,angle):
    height,width = image.shape[:2]
    rot_point = (width//2,height//2)

    rot_matrx = cv.getRotationMatrix2D(rot_point,angle=angle,scale=1.0)
    return cv.warpAffine(image,rot_matrx,(width,height))

rotated_img = rotate_img(img,45)
cv.imshow("rotated bot",rotated_img)

flip_img = rotate_img(img,180)
cv.imshow("flip bot",flip_img)

flip_flip_img = rotate_img(flip_img,140)
cv.imshow("flip_flip bot",flip_flip_img)
cv.waitKey(0)