import cv2
face_data=cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_frontalface_default.xml")
webcam=cv2.VideoCapture(0)
while True:
    sucess,frame=webcam.read()
    grayscale=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    face_coordinates=face_data.detectMultiScale(grayscale,scaleFactor=1.5,minNeighbors=5)

    for(x,y,w,h) in face_coordinates:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),10)
    cv2.imshow('fcae',frame)
    stop=cv2.waitKey(0)

    if stop==49:
      break

      
