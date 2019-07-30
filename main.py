import datetime
import os
import shift
import delivery
import utilFunc

def now():
    return datetime.datetime.now()


def startMenu():
    while True:
        if os.path.exists(os.path.join("deliveryTracking", "shifts", str(now().date()) + '.py')) == False:
            print('what would you like to do?\n1 to start a new shifts | 2 to return from split')
            try:
                userInput = int(input())
                if userInput == 1:
                    shift.startShift()
                    shiftMenu()
                    continue

                elif userInput == 2:
                    shift.endSplit()
                    shiftMenu()
                    continue

            except ValueError:
                print('\ninvalid input...')

            else:
                print('\ninvalid input...')


        elif os.path.exists(os.path.join("deliveryTracking", "shifts", str(now().date()) + '.py')) == True:
            while True:
                print('what would you like to do?\n1 to continue shift | 2 to return from split | 0 to overwrite shift')
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
                        if utilFunc.overWriteCheck() == True:
                            shift.startShift()
                            shiftMenu()
                            continue

                        else:
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
                continue

            elif userInput == 2:
                shift.endShift()
                break

            elif userInput == 3:
                shift.startSplit()
                break

        except ValueError:
            print('invalid input...')

        else:
            print('invalid input...')


if __name__ == "__main__":
    startMenu()
