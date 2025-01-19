import cv2
# reading images
# img = cv2.imread('images/cat.jpg')
# print(img.shape)
# # resize the image
# height = 500
# width = 500
# img = cv2.resize(img,(height,width))

# cv2.imshow('Image',img)
# cv2.waitKey(0)



# resizeing the video

# make a fun for resize the video
def rescale_frame(frame,scale=0.5):
    height = int(frame.shape[0]*scale)
    width = int(frame.shape[1]*scale)

    # make a dimension 
    dimension =(height,width)
    resie_img = cv2.resize(frame,dimension)
    return resie_img

video = cv2.VideoCapture('videos/acnee.mp4')
# display the video frame by frame
while True:
    is_true,frame = video.read()
    
    if not is_true:
        break
    
    # resize the frame
    resize_frame = rescale_frame(frame,scale=0.2)
    # display the frame 
    cv2.imshow("Video",frame)
    cv2.imshow("Video Resized",resize_frame)

    # break the video is not frame is available
    if cv2.waitKey(20) & 0xFF == ord('d'):
        break

video.release()
cv2.destroyAllWindows()