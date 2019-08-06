import os
import shutil

import shift
import delivery
import utilFunc


def startMenu():
    while True:
        if os.path.exists(os.path.join("deliveryTracking", "shift", "shiftStartTime.txt")) == False:
            print('\nwhat would you like to do?\n1 to start a new shift | 0 for settings')
            try:
                userInput = int(input())
                if userInput == 1:
                    shift.startShift()
                    shiftMenu()
                    continue

                elif userInput == 0:
                    settingMenu()
                    continue

            except ValueError:
                print('\ninvalid input...')

            else:
                print('\ninvalid input...')


        elif os.path.exists(os.path.join("deliveryTracking", "shift", "shiftEndTime.txt")) == True:
            print("\nALERT:\ntoday's shift has already been ended\n\nwhat would you like to do?\n1 to continue shift | 0 for settings")
            try:
                userInput = int(input())
                if userInput == 1:
                    print('\nWARNING!!!\nthis will delete the already existing endShiftFile.txt')
                    areYouSure = utilFunc.areYouSure('delete file and continue shift,')
                    if areYouSure == True:
                        os.remove(os.path.join("deliveryTracking", "shift", "shiftEndTime.txt"))
                        with open(os.path.join("deliveryTracking", "shift", "numbOfDeliveries.txt"), 'r') as file:
                            utilFunc.writeData("", "deliveryTracking", "deliveryNumb.txt", file.read())
                        continue

                elif userInput == 0:
                    settingMenu()
                    continue

            except ValueError:
                print('\ninvalid input...')

            else:
                print('\ninvalid input...')


        elif os.path.exists(os.path.join("deliveryTracking", "shift", "shiftStartTime.txt")) == True and os.path.exists(os.path.join("shift", "splitStartTime.txt")) == False or os.path.exists(os.path.join("shift", "splitEndTime.txt")) == True:
            shiftMenu()
            print('\nwhat would you like to do?\n1 to continue shift | 0 for settings')
            try:
                userInput = int(input())
                if userInput == 1:
                    shiftMenu()
                    continue

                elif userInput == 0:
                    settingMenu()
                    continue

            except ValueError:
                print('\ninvalid input...')

            else:
                print('\ninvalid input...')


        elif os.path.exists(os.path.join("deliveryTracking", "shift", "shiftStartTime.txt")) == True and os.path.exists(os.path.join("shift", "splitStartTime.txt")) == True:
            print('\nwhat would you like to do?\n1 to end split | 0 for settings')
            try:
                userInput = int(input())
                if userInput == 1:
                    shift.endSplit()
                    shiftMenu()
                    continue

                elif userInput == 0:
                    settingMenu()
                    continue

            except ValueError:
                print('\ninvalid input...')

            else:
                print('\ninvalid input...')


def shiftMenu():
    while True:
        print('\nwhat would you like to do?\n1 to start delivery | 2 to end shift | 3 to start split | 0 for start menu')
        try:
            userInput = int(input())
            if userInput == 1:
                delivery.delivery()
                shutil.move(os.path.join("deliveryTracking", "delivery"), os.path.join("deliveryTracking", "shift", "delivery" + utilFunc.deliveryNumb('number')))
                utilFunc.deliveryNumb('update')
                continue

            elif userInput == 2:
                shift.endShift()
                exit()

            elif userInput == 3:
                shift.startSplit()
                exit()

            elif userInput == 0:
                break

        except ValueError:
            print('\ninvalid input...')

        else:
            print('\ninvalid input...')


def settingMenu():
    while True:
        print('\nwhat setting to change:\n1 to overwrite shift file | 2 to change deliver number | 3 to change order number preset | 0 to go back')
        try:
            userInput = int(input())
            if userInput == 1:
                utilFunc.overWriteCheck()
                break

            elif userInput == 2:
                print('\ncurrently delivery number is at:    ' + str(utilFunc.deliveryNumb('number')))
                utilFunc.deliveryNumb('change')
                continue

            elif userInput == 3:
                print('\ncurrently first 3 numbers of order numbers are set to:    ' + utilFunc.beginOrdNumb('number'))
                utilFunc.beginOrdNumb('change')
                continue

            elif userInput == 0:
                break

        except ValueError:
            print('\ninvalid input...')

        else:
            print('\ninvalid input...')


if __name__ == "__main__":
    startMenu()
