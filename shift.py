import os

import main
import utilFunc

def startShift():
    utilFunc.deliveryNumb('reset')
    os.mkdir(os.path.join("shift"))
    utilFunc.writeData("deliveryTracking", "shift", "shiftStartTime.txt", utilFunc.now())


def endShift():
    utilFunc.writeData("deliveryTracking", "shift", "shiftEndTime.txt", utilFunc.now())
    utilFunc.deliveryNumb('reset')


def startSplit():
    utilFunc.writeData("deliveryTracking", "shift", "splitStartTime.txt", utilFunc.now())


def endSplit():
    utilFunc.writeData("deliveryTracking", "shift", "splitEndTime.txt", utilFunc.now())
