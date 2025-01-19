import cv2

# reading images
# img = cv2.imread('Images/chatbot.jpg')
# img = cv2.imread('Images\cat.jpg')
# cv2.imshow("Chatbot",img)
# cv2.waitKey(0)


# reading videos
capture = cv2.VideoCapture('videos/acnee.mp4')
# dispolaythe video frame by frame  untile frame is availabel
while True:
    is_true,frame = capture.read()

    if not is_true:
        print("Video is ended")
        break
    
    # display the frame
    cv2.imshow("Acnee",frame)

    # break the loop if frame is end
    if cv2.waitKey(20) & 0xFF == ord('d'):
        break

# release the  capture 
capture.release()
cv2.destroyAllWindows()