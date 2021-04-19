
import csv

import cv2
import os


# counting the numbers


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False



# Take image function


def capture_user_image() :
    roll = input("Enter Your Roll Number: " ).strip()
    name = input("Ente Your Name : " ).strip()

    if not is_number(roll) :
        print("Enter Numberic Roll Number!! ")
        capture_user_image()
    elif not name.isalpha():
        print("Enter Proper Name")

    camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    harcascadePath = "haarcascade_frontalface_default.xml"
    detector = cv2.CascadeClassifier(harcascadePath)
    sampleNum = 0

    folder_path = os.path.join('TrainingImages',f'{name}.{roll}')
    if os.path.isdir(folder_path):
        print("Directory Already Exists!!")
        return
    os.makedirs(folder_path)
    while(True):
        ret, img = camera.read()
        re2 , frame  = camera.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        #clr = cv2.cvtColor(img)
        faces = detector.detectMultiScale(gray, 1.3, 5, minSize=(30,30),flags = cv2.CASCADE_SCALE_IMAGE)
        for(x,y,w,h) in faces:
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)
            #incrementing sample number
            sampleNum = sampleNum+1
            #saving the captured face in the dataset folder TrainingImage

            #file_path = os.path.join()
            cv2.imwrite(folder_path+ os.sep +name + "."+roll+ '.' +
                        str(sampleNum) + ".jpg", frame)
#             cv2.imwrite("TrainingImages"+os.sep+name + os.sep +name + "."+roll+ '.' +
#                         str(sampleNum) + ".jpg", frame)
            #display the frame
            cv2.imshow('frame', img)
        #wait for 100 miliseconds
        if cv2.waitKey(100) & 0xFF == ord('q'):
            break
        # break if the sample number is more than 100
        elif sampleNum > 50:
            break
    camera.release()
    cv2.destroyAllWindows()
    res = "Images Saved for ID : " + roll + " Name : " + name
    print(res)
