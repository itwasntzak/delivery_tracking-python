import datetime

def time():
   return(str(datetime.datetime.now().time()))

def order():
   endTime = time()
   orderInfo = [orderNumb(), [tip(), milesTrav(), endTime]]
   return(orderInfo)


def orderNumb():
   while True:
      print('enter order number: ######')
      try:
         orderNumb = int(input())
         return(orderNumb)

      except ValueError:
         print('invalid input...')


def tip():
   while True:
      print('did they tip?\n1 = yes, 2 = no')
      try:
         tipOption = int(input())
         if tipOption == 1:
            while True:
               print('enter tip amount: #.##')
               try:
                  tipAmount = float(input())
                  return([tipAmount, tipType()])

               except ValueError:
                  print('invalid input...')

         elif tipOption == 2:
            return('N/A')

      except ValueError:
         print('invalid input...')

      else:
         print('invalid input...')


def tipType():
   while True:
      print('type of tip?\n1 = card, 2 = cash')
      try:
         tipTypeOption = int(input())
         if tipTypeOption == 1:
            return('card')

         elif tipTypeOption == 2:
            return('cash')

      except ValueError:
         print('invalid input...')

      else:
         print('invalid input...')


def milesTrav(varWord = ''):
   while True:
      print(varWord + 'mile traveled:')
      try:
         milesTravInput = float(input())
         return(milesTravInput)

      except ValueError:
         print('invalid input...')
