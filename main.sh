#!/usr/bin/env python
#!/data/data/com.termux/files/usr/bin/bash python

import datetime
import shift
import delivery

def date():
    return(str(datetime.datetime.now().date()))


def time():
    return(str(datetime.datetime.now().time()))


def startMenu():
    while True:
        print('what would you like to do?\n1 to start shift, 2 to continue shift, 3 to return from split')
        try:
            userInput = int(input())
            if userInput == 1:
                shift.startShift()
                shiftMenu()
                continue

            elif userInput == 2:
                shiftMenu()
                continue

            elif userInput == 3:
                shift.endSplit()
                shiftMenu()
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


if __name__ == "__main__":
    startMenu()
    
