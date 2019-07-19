import order


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
         return([numbOfOrders, orderEnd()])

      elif numbOfOrders > 1:
         return([numbOfOrders, [orderEnd() for value in range(numbOfOrders)]])

      print('invalid input')


def delivery():
   startTime = main.time()

   orders = numbOfOrders()

   while True:
      print('returning to store...\nupon arival, 1 to continue')
      waitForUser = int(input())
      if waitForUser == 1:
         endTime = main.time()
         return([startTime, orders, order.milesTrav('Total '), endTime])
      
      print('invalid input')


def createDelivery():
   while True:
      print('What delivery number is this?')
      try:
         dlvNumbInput = int(input())

         with open(main.date() + '.txt', 'a+') as today:
            content = today.read()
            today.seek(len(content))
            today.write('\ndlv' + str(dlvNumbInput) + ' = ' + str(delivery()))
            break

      except ValueError:
         print('invalid input...')
