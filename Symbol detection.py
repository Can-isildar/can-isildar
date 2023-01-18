import pytesseract
import cv2

pytesseract.pytesseract.tesseract_cmd = "C:\\Users\\emre\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe"

vid = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_PLAIN

face_cascade = cv2.CascadeClassifier("sembol.xml")


while 1:
    
    # 5. Her kareyi tek tek okuyalım.
    ret, frame = vid.read()


    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    

    faces = face_cascade.detectMultiScale(gray, 1.4, 5)


    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        crop_img = frame[y:y+h, x:x+w]
        sayi = pytesseract.image_to_string(crop_img,lang="eng")


    try:
        cv2.imshow('video', frame)
        cv2.imshow('crop', crop_img)

        print("detect text", sayi)
    except:
        cv2.imshow('video', frame)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break



vid.release()
cv2.destroyAllWindows()

