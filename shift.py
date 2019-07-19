import datetime
import main

date = datetime.datetime.now().date()

def time():
    return(str(datetime.datetime.now().time()))


def startShift():
    with open(str(date) + '.txt', 'w') as today:
        today.write('startShift = ' + "'" + time() + "'")

    return(main.shiftMenu())


def continueShift():
    return(main.shiftMenu())


def endShift():
   with open(str(date) + '.txt', 'a+') as today:
      content = today.read()
      today.seek(len(content))
      today.write('\nendShift = ' + "'" + time() + "'")

      return(main.startMenu())


def startSplit():
   with open(str(date) + '.txt', 'a+') as today:
      content = today.read()
      today.seek(len(content))
      today.write('\nstartSplit = ' + "'" + time() + "'")

      return(main.startMenu())


def endSplit():
   with open(str(date) + '.txt', 'a+') as today:
      content = today.read()
      today.seek(len(content))
      today.write('\nendSplit = ' + "'" + time() + "'")

      return(main.shiftMenu())
