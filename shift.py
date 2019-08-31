import os

<<<<<<< HEAD
import main
import utilFunc

def startShift():
    utilFunc.deliveryNumb('reset')
    os.mkdir(os.path.join("deliveryTracking", "shift"))
    utilFunc.writeData("deliveryTracking", "shift", "shiftStartTime.txt", utilFunc.now())


def endShift():
    utilFunc.writeData("deliveryTracking", "shift", "shiftEndTime.txt", utilFunc.now())
    utilFunc.deliveryNumb('reset')


def startSplit():
    utilFunc.writeData("deliveryTracking", "shift", "splitStartTime.txt", utilFunc.now())


def endSplit():
    utilFunc.writeData("deliveryTracking", "shift", "splitEndTime.txt", utilFunc.now())
=======
import util_func


def start_shift():
    util_func.delivery_number(
        option='reset'
    )
    os.mkdir(os.path.join(
        'shift'
    ))
    util_func.write_data(
        path='shift',
        file='shift_start_time.txt',
        data=util_func.now()
    )


def end_shift():
    util_func.write_data(
        path='shift',
        file='shift_end_time.txt',
        data=util_func.now()
    )
    util_func.delivery_number(
        option='reset'
    )
    exit()


def start_split():
    util_func.write_data(
        path='shift',
        file='split_start_time.txt',
        data=util_func.now()
    )
    exit()


def end_split():
    util_func.write_data(
        path='shift',
        file='split_end_time.txt',
        data=util_func.now()
    )
>>>>>>> master
