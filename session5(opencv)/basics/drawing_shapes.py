import cv2

img = cv2.imread("Images/cat.jpg")

# resize the image
resize_img = cv2.resize(img,(500,500))

# drawing shapes
cv2.rectangle(resize_img,(0,0),(200,200),(0,0,100),thickness=2)

# draw circle
# cv2.circle(resize_img,(200,200),50,(0,255,0),thickness=2)
cv2.circle(resize_img,(200,200),50,(0,255,0),thickness=cv2.FILLED)

# draw line
cv2.line(resize_img,(0,0),(200,200),(255,0,0),thickness=2)

# draw text 
cv2.putText(resize_img,"Thsi is my cat",(100,100),fontFace=cv2.FONT_HERSHEY_SIMPLEX,fontScale=1,color=(255,255,255),thickness=2)
cv2.imshow('Image',resize_img )
cv2.waitKey(0)