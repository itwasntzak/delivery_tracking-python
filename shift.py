import os

import main
import utilFunc

def startShift():
    utilFunc.deliveryNumb('reset')
    os.mkdir(os.path.join("shift"))
    utilFunc.writeData("shift", "shiftStartTime.txt", utilFunc.now())


def endShift():
    utilFunc.writeData("shift", "shiftEndTime.txt", utilFunc.now())
    utilFunc.deliveryNumb('reset')


def startSplit():
    utilFunc.writeData("shift", "splitStartTime.txt", utilFunc.now())


def endSplit():
    utilFunc.writeData("shift", "splitEndTime.txt", utilFunc.now())