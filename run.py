import os  # accessing the os functions
from TestCamera import test_camera

from TrainImages import train
from Attendance import _attendance
from ImageCapture import capture_user_image
# creating the title bar function


def titleBar(clear_screen=True):
    if clear_screen:
        os.system('cls')  # for windows

    # title of the program

    print("\t**********************************************")
    print("\t***** Python OpenCV Attendance System *****")
    print("\t**********************************************")


# creating the user main menu function
def main(clear_screen = True):
    titleBar(clear_screen=clear_screen)
    print("")
    print("\t(1) Check Device's Camera")
    print("\t(2) Capture Face Images")
    print("\t(3) Train Images")
    print("\t(4) Recognize Face and Mark Attendance")
    #print("\t(5) Send Mail")
    print("\t(5) Exit")

    try:
        option = int(input("Select an Option: "))
    except:
        option = -1

    if option == 1:
        CheckCam()
    elif option == 2:
        CaptureImages()
    elif option == 3:
        TrainImages()
    elif option == 4:
        MarkAttendance()
    #elif option == 5:
        # os.system("py automail.py")
     #   main()
    elif option == 5:
        print("System Exited, Thank you!")
        exit
    else:
        print("Invalid choice was selected. Select from 1-6")
        main(clear_screen = False)


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
    print("Started Training Model")
    train()
    key = input("Enter any key to return main menu")
    main()


# --------------------------------------------------------------------
# calling the recognize_attendance from recognize.py file

def MarkAttendance():
    _attendance()
    #temp()
    key = input("Enter any key to return main menu")
    main()


# ---------------main driver ------------------
main()
