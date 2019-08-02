import os

import main
import utilFunc

def startShift():
    with open(os.path.join("shifts", str(utilFunc.now().date()) + '.py'), 'w') as today:
        today.write('startShift = ' + str(utilFunc.now()))


def endShift():
    with open(os.path.join("shifts", str(utilFunc.now().date()) + '.py'), 'a+') as today:
        content = today.read()
        today.seek(len(content))
        today.write('\nendShift = ' + str(utilFunc.now()))
        utilFunc.deliveryNumb('reset')


def startSplit():
    with open(os.path.join("shifts", str(utilFunc.now().date()) + '.py'), 'a+') as today:
        content = today.read()
        today.seek(len(content))
        today.write('\nstartSplit = ' + str(utilFunc.now()))


def endSplit():
    with open(os.path.join("shifts", str(utilFunc.now().date()) + '.py'), 'a+') as today:
        content = today.read()
        today.seek(len(content))
        today.write('\nendSplit = ' + str(utilFunc.now()))