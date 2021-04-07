import os  
import check_camera
import Capture_Image
import Train_Image
import Recognize


def titleBar():
    os.system('cls')  # for windows

    print("\t----------------------------------------------")
    print("\t------------- Attendance System --------------")
    print("\t----------------------------------------------")


# main function

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

def CheckCam():
    check_camera.checkCam()
    key = input("Enter any key to go to the main menu")
    main()

def CaptureImages():
    Capture_Image.captureImages()
    key = input("Enter any key to go to the main menu")
    main()

def TrainImages():
    Train_Image.trainImages()
    key = input("Enter any key to go to the main menu")
    main()

def MarkAttendance():
    Recognize.markAttendence()
    key = input("Enter any key to go to the main menu")
    main()

#calling the main menu
main()
