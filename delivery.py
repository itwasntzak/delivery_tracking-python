import datetime
import order

def time():
   currentTime = datetime.datetime.now().time()
   return(currentTime)


def orderEnd():
   print('waiting...\n1 to continue')
   waitForUser = int(input())
      
   while True:
      if waitForUser == 1:
         return(order.order())
      
      print('invalid input')


def startDlv():
   startTime = time()
   
   print('number of orders?')
   numbOfOrders = int(input())
   while True:
      if numbOfOrders == 1:
         orders = order.order()

      elif numbOfOrders > 1:
         orders = [order.order() for value in range(numbOfOrders)]

      print('invalid input')


   print('waiting...\n1 to continue')
   waitForUser = int(input())
   while True:
      if waitForUser == 1:
         endTime = time()
         totalMilesTrav = order.milesTrav()
         return([startTime, orders, totalMilesTrav, endTime])
      
      print('invalid input')


delivery0 = startDlv()
