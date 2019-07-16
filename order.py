import datetime

def order():
   endTime = datetime.datetime.now().time()
   return([orderNumb(), [tip(), milesTrav(), endTime]])


def orderNumb():
   print('order number:')
   return(int(input()))


def tip():
   while True:
      print('tip?\n1 = yes, 2 = no')
      tipOption = int(input())
      if tipOption == 1:
         print('tip amount:')
         return([float(input()), tipType()])

      elif userInput == 2:
         return('N/A')

      print('invalid input')


def tipType():
   while True:
      print('type of tip?\n1 = card, 2 = cash')
      tipTypeOption = int(input())
      if tipTypeOption == 1:
         return('card')

      elif tipTypeOption == 2:
         return('cash')

      print('invalid input')


def milesTrav():
   print('mile traveled:')
   return(float(input()))
