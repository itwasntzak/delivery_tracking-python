import datetime
import order

def time():
   return(datetime.datetime.now().time())


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
         orders = orderEnd()

      elif numbOfOrders > 1:
         orders = [orderEnd() for value in range(numbOfOrders)]

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
