import datetime


def milesTrav(varWord = ''):
   while True:
      print('\n' + varWord + 'mile traveled:')
      try:
         milesTravInput = float(input())
         return milesTravInput

      except ValueError:
         print('\ninvalid input...')


def overWriteCheck():
    while True:
        print("\nALERT:\nare you sure you want to overwrite today's file?\n1 for yes | 2 for no")
        try:
            userInput = int(input())
            if userInput == 1:
                return True

            elif userInput == 2:
                return False

        except ValueError:
            print('\ninvalid input')

        else:
            print('\ninvalid input')


def timeTook(startTime, endTime, varWord):
    timeDif = endTime - startTime
    mins = int(timeDif.total_seconds() / 60)
    secs = timeDif.total_seconds() - (mins * 60)

    if mins == 0:
        print('\nit took you ' + str(secs) + ' seconds to complete this ' + varWord)

    elif mins == 1:
        print('\nit took you ' + str(mins) + ' minute and ' + str(secs) + ' seconds to complete this ' + varWord)

    elif mins > 1:
        print('\nit took you ' + str(mins) + ' minutes and ' + str(secs) + ' seconds to complete this ' + varWord)

    elif mins >= 60:
        print('\nit took you more then an hour to complete this order')
