import datetime
import delivery as dlv

date = datetime.datetime.now().date()

def time():
    return(datetime.datetime.now().time())


def createShift():
    with open('shifts\\' + str(date) + '.py', 'w') as today:
        today.write('Start Shift = ' + "'" + str(time()) + "'")

    return(shiftMenu())


def continueShift():
    with open('shifts\\' + str(date) + '.py', 'a+') as today:
        content = today.read()
        today.seek(len(content))

    return(shiftMenu())


def createDelivery():
    with open('shifts\\' + str(date) + '.py', 'a+') as today:
        content = today.read()
        today.seek(len(content))
        today.write('\n' + str(dlv.delivery()))


def endShift():
    with open('shifts\\' + str(date) + '.py', 'a+') as today:
        content = today.read()
        today.seek(len(content))
        today.write('\nEnd Shift = ' + "'" + str(time()) + "'")


def shiftMenu():
    while True:
        print('what next?\n1 = start new delivery, 2 = end shift')
        try:
            userInput = int(input())
            if userInput == 1:
                createDelivery()
                continue

            elif userInput == 2:
                endShift()
                break

        except ValueError:
            print('invalid input...')

        else:
            print('invalid input...')


def startMenu():
    while True:
        print('what would you like to do?\n1 to start shift, 2 to continue shift')
        try:
            userInput = int(input())
            if userInput == 1:
                createShift()
                continue

            elif userInput == 2:
                continueShift()
                continue

        except ValueError:
            print('invalid input...')

        else:
            print('invalid input...')



startMenu()
