import datetime
import order

def time():
   return(datetime.datetime.now().time())


def orderEnd():     
   while True:
      print('driving to address...\nafter returning to car, 1 to continue')
      waitForUser = int(input())
      
      if waitForUser == 1:
         return(order.order())
      
      print('invalid input')


def numbOfOrders():
   while True:
      print('number of orders?')
      numbOfOrders = int(input())
      if numbOfOrders == 1:
         return(orderEnd())

      elif numbOfOrders > 1:
         return([orderEnd() for value in range(numbOfOrders)])

      print('invalid input')


def delivery():
   startTime = time()

   orders = numbOfOrders()

   while True:
      print('returning to store...\nupon arival, 1 to continue')
      waitForUser = int(input())
      if waitForUser == 1:
         endTime = time()
         return([startTime, orders, order.milesTrav('Total '), endTime])
      
      print('invalid input')
