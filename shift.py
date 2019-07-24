import main

def startShift():
    with open(main.date() + '.py', 'w') as today:
        today.write('startShift = ' + "'" + main.time() + "'")


def endShift():
    with open(main.date() + '.py', 'a+') as today:
        content = today.read()
        today.seek(len(content))
        today.write('\nendShift = ' + "'" + main.time() + "'")

    with open('dlvNumb.txt', 'w') as dlvNumb:
        dlvNumb.write('0')


def startSplit():
    with open(main.date() + '.py', 'a+') as today:
        content = today.read()
        today.seek(len(content))
        today.write('\nstartSplit = ' + "'" + main.time() + "'")


def endSplit():
    with open(main.date() + '.py', 'a+') as today:
        content = today.read()
        today.seek(len(content))
        today.write('\nendSplit = ' + "'" + main.time() + "'")
