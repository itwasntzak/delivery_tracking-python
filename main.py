import datetime
import shift
import delivery

def startMenu():
    while True:
        print('what would you like to do?\n1 to start shift, 2 to continue shift, 3 to return from split')
        try:
            userInput = int(input())
            if userInput == 1:
                shift.startShift()
                continue

            elif userInput == 2:
                shift.continueShift()
                continue

            elif userInput == 3:
                shift.endSplit()
                continue

        except ValueError:
            print('invalid input...')

        else:
            print('invalid input...')


def shiftMenu():
    while True:
        print('what next?\n1 to start new delivery, 2 to end shift, 3 to start split')
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



startMenu()
