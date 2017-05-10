import numpy as np
import cv2
import time

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FPS , 2)


while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    #time.sleep(1)

    # Our operations on the frame come here, copy output
   
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    img = frame.copy()
    cimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)	    

    circles = cv2.HoughCircles(cimg,cv2.HOUGH_GRADIENT,3,500,param1=50,param2=30,minRadius=100,maxRadius=1000)

    circles = np.uint16(np.around(circles))
    
    for i in circles[0,:]:
    	cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
    
    	cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)
   

    cv2.imshow('detected circles',cimg)
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
    	break

 # When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
