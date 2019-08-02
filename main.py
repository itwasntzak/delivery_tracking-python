import datetime
import os
import shelve

import shift
import delivery
import order
import utilFunc


def startMenu():
    while True:
        if os.path.exists(os.path.join("deliveryTracking", "shifts", str(utilFunc.now().date()) + '.py')) == False:
            print('what would you like to do?\n1 to start a new shifts | 0 for settings')
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


        elif os.path.exists(os.path.join("deliveryTracking", "shifts", str(utilFunc.now().date()) + '.py')) == True:
            while True:
                print('what would you like to do?\n1 to continue shift | 2 to return from split | 0 for settings')
                try:
                    userInput = int(input())
                    if userInput == 1:
                        shiftMenu()
                        continue

                    elif userInput == 2:
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
        print('\nwhat next?\n1 to start delivery | 2 to end shift | 3 to start split')
        try:
            userInput = int(input())
            if userInput == 1:
                delivery.createDelivery()
                utilFunc.deliveryNumb('update')
                continue

            elif userInput == 2:
                shift.endShift()
                break

            elif userInput == 3:
                shift.startSplit()
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
                continue

            elif userInput == 2:
                print('\ncurrently delivery number is at:    ' + str(utilFunc.deliveryNumb('number')))
                utilFunc.deliveryNumb('change')
                continue

            elif userInput == 3:
                print('\ncurrently first 3 numbers of order numbers are set to:    ' + utilFunc.beginOrdNumb('whatIs'))
                utilFunc.beginOrdNumb('change')
                continue

            elif userInput == 0:
                return 'return'

        except ValueError:
            print('\ninvalid input...')

        else:
            print('\ninvalid input...')


if __name__ == "__main__":
    startMenu()
