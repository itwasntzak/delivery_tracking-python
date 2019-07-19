def startShift():
    with open(main.date() + '.txt', 'w') as today:
        today.write('startShift = ' + "'" + main.time() + "'")


def endShift():
    with open(main.date() + '.txt', 'a+') as today:
        content = today.read()
        today.seek(len(content))
        today.write('\nendShift = ' + "'" + main.time() + "'")


def startSplit():
    with open(main.date() + '.txt', 'a+') as today:
        content = today.read()
        today.seek(len(content))
        today.write('\nstartSplit = ' + "'" + main.time() + "'")


def endSplit():
    with open(main.date() + '.txt', 'a+') as today:
        content = today.read()
        today.seek(len(content))
        today.write('\nendSplit = ' + "'" + main.time() + "'")
