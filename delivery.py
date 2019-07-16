import datetime
import order

def time():
   return(datetime.datetime.now().time())


def orderEnd():     
   while True:
      print('waiting...\n1 to continue')
      waitForUser = int(input())
      
      if waitForUser == 1:
         return(order.order())
      
      print('invalid input')


def orders():
   while True:
      print('number of orders?')
      numbOfOrders = int(input())
      if numbOfOrders == 1:
         return(orderEnd())

      elif numbOfOrders > 1:
         return([orderEnd() for value in range(numbOfOrders)])

      print('invalid input')


def startDlv():
   startTime = time()

   numbOrders = orders()

   while True:
      print('waiting...\n1 to continue')
      waitForUser = int(input())
      if waitForUser == 1:
         endTime = time()
         totalMilesTrav = order.milesTrav()
         return([startTime, numbOrders, totalMilesTrav, endTime])
      
      print('invalid input')


delivery0 = startDlv()
