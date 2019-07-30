import os
import main

def startShift():
    with open(os.path.join("deliveryTracking", "shifts", str(main.now().date()) + '.py'), 'w') as today:
        today.write('startShift = ' + str(main.now()))


def endShift():
    with open(os.path.join("deliveryTracking", "shifts", str(main.now().date()) + '.py'), 'a+') as today:
        content = today.read()
        today.seek(len(content))
        today.write('\nendShift = ' + str(main.now()))

    with open(os.path.join("deliveryTracking", "dlvNumb.txt"), 'w') as dlvNumb:
        dlvNumb.write('0')


def startSplit():
    with open(os.path.join("deliveryTracking", "shifts", str(main.now().date()) + '.py'), 'a+') as today:
        content = today.read()
        today.seek(len(content))
        today.write('\nstartSplit = ' + str(main.now()))


def endSplit():
    with open(os.path.join("deliveryTracking", "shifts", str(main.now().date()) + '.py'), 'a+') as today:
        content = today.read()
        today.seek(len(content))
        today.write('\nendSplit = ' + str(main.now()))
