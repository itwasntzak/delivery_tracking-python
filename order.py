import datetime

def order():
   endTime = datetime.datetime.now().time()
   return([orderNumb(), [tip(), milesTrav(), endTime]])


def orderNumb():
   print('order number:')
   orderNumb = int(input())
   return(orderNumb)


def tip():
   print('tip?\n1 = yes, 2 = no')
   tipOption = int(input())
   while True:
      if tipOption == 1:
         print('tip amount:')
         tipAmount = float(input())
         return([tipAmount, tipType()])

      elif userInput == 2:
         return('N/A')

      print('invalid input')


def tipType():
   print('type of tip?\n1 = card, 2 = cash')
   tipTypeOption = int(input())
   while True:
      if tipTypeOption == 1:
         return('card')

      elif tipTypeOption == 2:
         return('cash')

      print('invalid input')


def milesTrav():
   print('mile traveled:')
   milesTrav = float(input())
   return(milesTrav)
