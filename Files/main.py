import os  # accessing the os functions
from TestCamera import test_camera
from ImageCapture import capture_user_image ,takeImages
import Train_Image
import Recognize


# creating the title bar function

def titleBar():
    # os.system('cls')  # for windows

    # title of the program

    print("\t**********************************************")
    print("\t***** Python OpenCV Attendance System *****")
    print("\t**********************************************")


# creating the user main menu function
def main():
    titleBar()
    print("")
    print("\t(1) Check Device's Camera")
    print("\t(2) Capture Face Images")
    print("\t(3) Train Images")
    print("\t(4) Recognize Face and Mark Attendance")
    print("\t(5) Send Mail")
    print("\t(5) Exit")

    option = int(input("Select an Option: "))

    if option == 1:
        CheckCam()
    elif option == 2:
        CaptureImages()
    elif option == 3:
        TrainImages()
    elif option == 4:
        MarkAttendance()
    elif option == 5:
        # os.system("py automail.py")
        main()
    elif option == 6:
        print("System Exited, Thank you!")
        exit
    else:
        print("Invalid choice was selected. Select from 1-6")
        main()


# ---------------------------------------------------------
# calling the camera test function from check camera.py file

def CheckCam():
    test_camera()
    key = input("Enter any key to return main menu")
    main()


# --------------------------------------------------------------
# calling the take image function form capture image.py file

def CaptureImages():
    # takeImages()
    capture_user_image() 
    key = input("Enter any key to return main menu")
    main()


# -----------------------------------------------------------------
# calling the train images from train_images.py file

def TrainImages():
    Train_Image.TrainImages()
    key = input("Enter any key to return main menu")
    main()


# --------------------------------------------------------------------
# calling the recognize_attendance from recognize.py file

def MarkAttendance():
    Recognize.recognize_attendence()
    key = input("Enter any key to return main menu")
    main()


# ---------------main driver ------------------
main()
