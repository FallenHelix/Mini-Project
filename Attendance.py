import math
import cv2, pickle, time, datetime
from sklearn import neighbors
import os, os.path
import pandas as pd
from PIL import Image
import numpy as np
import face_recognition

def load_model(model_path = "trained_knn_model.clf"):
    with open(model_path, 'rb') as f:
        knn_clf = pickle.load(f)
    return knn_clf



def predict_results(knn_clf, face_locations, faces_encodings):

    distance_threshold = 0.6
    # Use the KNN model to find the best matches for the test face
    closest_distances = knn_clf.kneighbors(faces_encodings, n_neighbors=1)
    are_matches = [closest_distances[0][i][0] <= distance_threshold for i in range(len(face_locations))]
    # Predict classes and remove classifications that aren't within the threshold
    return [(pred, loc) if rec else ("unknown", loc) for pred, loc, rec in zip(knn_clf.predict(faces_encodings), face_locations, are_matches)]




def start_attendance(attendance):
    font = cv2.FONT_HERSHEY_SIMPLEX
    harcascadePath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(harcascadePath)
    knn_clf = load_model()
    if(knn_clf == None):
        print("knn is null")
        return
    # Initialize and start realtime video capture



    print("starting Video Capture")
    cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
 #   cam.set(3, 640)  # set video width
#    cam.set(4, 480)  # set video height
    # Define min window size to be recognized as a face
    minW = 0.1 * cam.get(3)
    minH = 0.1 * cam.get(4)
    dict_name =  set(attendance['Name'])
    process_this_frame = True
    while(True):
        ret , frame = cam.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        #convert BGR to RGB data.
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = small_frame[: , : , ::-1]
        faces = faceCascade.detectMultiScale(gray, 1.2, 5,minSize = (int(minW), int(minH)),flags = cv2.CASCADE_SCALE_IMAGE)
#         for(x, y, w, h) in faces:
#             cv2.rectangle(frame, (x, y), (x+w, y+h), (10, 159, 255), 2)
#
        if process_this_frame:
            face_locations = face_recognition.face_locations(rgb_small_frame)
            if(len(face_locations) !=0):
                face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
                predictions = predict_results(knn_clf=knn_clf , face_locations=face_locations, faces_encodings=face_encodings)
            else:
                predictions = None
        process_this_frame = not process_this_frame

        if predictions is not None:
            for name, (top, right , bottom, left) in predictions:
                top *=4
                bottom *= 4
                left *=4
                right *= 4
                name , Id  = name.split(".")
                #print(name, Id)
                cv2.rectangle(frame, (left,top), (right,bottom),(10, 159, 255), 2)
                cv2.putText(frame, str(name),(bottom - 10, top-10),font, 1, (255, 255, 255), 2)
                # Add Names to attendance
                #roll, a_name = name.split('.')
                if name not in dict_name:
                    dict_name.add(name)  ;
                    ts = time.time()
                    date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
                    timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
                    attendance.loc[len(attendance)] = [Id, name, date, timeStamp]

        cv2.imshow('Attendance' , frame)
        if(cv2.waitKey(1) == ord('q')):
            break

    attendance = attendance.drop_duplicates(subset=['Id'], keep='first')
#     ts = time.time()
#     date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
#     timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
#     Hour, Minute, Second = timeStamp.split(":")
#     fileName = "Attendance"+os.sep+"Attendance_"+date
#     if(os.path.isfile(fileName))
#     #+"_"+Hour+"-"+Minute+"-"+Second+".csv"
#     attendance.to_csv(fileName, index=False)
    cam.release()
    cv2.destroyAllWindows()
    return attendance


def _attendance():
    #Dataframe for attendance
    col_names = ['Id', 'Name', 'Date', 'Time']
    attendance = pd.DataFrame(columns=col_names)

    ts = time.time()
    date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
    timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
    Hour, Minute, Second = timeStamp.split(":")
    fileName = "Attendance"+os.sep+"Attendance_"+date+".csv"
    if(os.path.isfile(fileName)):
        attendance = pd.read_csv(fileName)
    attendance= start_attendance(attendance=attendance)

    attendance.to_csv(fileName, index=False)
    print("Attendance Successful")
