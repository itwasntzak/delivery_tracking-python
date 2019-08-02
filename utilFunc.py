import datetime
import os

import shift


def now():
    return datetime.datetime.now()


def deliveryNumb(option):
    if option == 'number':
        with open(os.path.join('deliveryNumb.txt'), 'r') as dlvNumb:
            return dlvNumb.read()

    elif option == 'update':
        with open(os.path.join('deliveryNumb.txt'), 'r+') as dlvNumb:
            prevDlvNumb = int(dlvNumb.read())
            dlvNumb.seek(0)
            dlvNumb.write(str(prevDlvNumb + 1))

    elif option == 'reset':
        with open(os.path.join('deliveryNumb.txt'), 'w') as dlvNumb:
            dlvNumb.write('0')

    elif option == 'change':
        while True:
            print('\nALERT!!!\nare you sure you want to change the delivery number?\n1 for yes | 2 for no')
            try:
                userInput = int(input())
                if userInput == 1:
                    print('\nwhat is the new current delivery number:')
                    try:
                        changeDeliveryNumb = int(input())
                        with open(os.path.join('deliveryNumb.txt'), 'w') as dlvNumb:
                            dlvNumb.write(str(changeDeliveryNumb))
                            break

                    except ValueError:
                        print('\ninvalid input...')

                elif userInput == 2:
                    break

            except ValueError:
                print('\ninvalid input...')

            else:
                print('\ninvalid input...')


def beginOrdNumb(option):
   if option == 'whatIs':
      with open(os.path.join('beginOrdNumb.txt'), 'r') as first3:
         return first3.read()

   elif option == 'change':
      while True:
          print('\nALERT!!!\nare you sure you want to change the order number preset?\n1 for yes | 2 for no')
          try:
              userInput = int(input())
              if userInput == 1:
                  print('\nwhat is the new set of 3 numbers for order number preset:')
                  first3Numbs = input()
                  with open(os.path.join('beginOrdNumb.txt'), 'w') as first3:
                      first3.write(str(first3Numbs))
                  return first3Numbs

              elif userInput == 2:
                  break

          except ValueError:
              print('\ninvalid input...')

          else:
              print('\ninvalid input...')


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
        print("\nALERT!!!\nare you sure you want to overwrite today's file?\n1 for yes | 2 for no")
        try:
            userInput = int(input())
            if userInput == 1:
                shift.startShift()
                break

            elif userInput == 2:
                break

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
