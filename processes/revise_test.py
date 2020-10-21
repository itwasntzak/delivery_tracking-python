import unittest

class Test_Revise(unittest.TestCase):
    def setUp(self):
        from testing_tools import completed_shift
        self.shift = completed_shift()

    def test_revise_delivery_build_confirmation(self):
        from processes.revise import Revise_Delivery
        from objects import Shift, Delivery, Order
        from utility.utility import now

        delivery = Delivery(Shift(now().date()))
        test = Revise_Delivery(delivery, test=True)

    def test_revise_delivery_build_prompt(self):
        from datetime import datetime
        from processes.revise import Revise_Delivery
        from objects import Shift, Delivery, Order, Extra_Stop
        from utility.utility import now

        # no data added yet
        delivery = Delivery(Shift(now().date()))
        test = Revise_Delivery(delivery, test=True)
        test.build_prompt()
        expected =\
            '\n- Revise Delivery -\n'\
            'Please select an option:\n'\
            '1. Add start time\n'\
            '2. Add miles traveled\n'\
            '3. Add average speed\n'\
            '4. Add end time\n'\
            'O. Add order\n'\
            'V. View current delivery\n'\
            'S. Save changes\n'\
            'B. Go back\n'
        self.assertEqual(test.prompt, expected)
        # start time added
        test.delivery.start_time = datetime.strptime('15:27:42', '%H:%M:%S')
        test.build_prompt()
        expected =\
            '\n- Revise Delivery -\n'\
            'Please select an option:\n'\
            '1. Revise start time\n'\
            '2. Add miles traveled\n'\
            '3. Add average speed\n'\
            '4. Add end time\n'\
            'O. Add order\n'\
            'V. View current delivery\n'\
            'S. Save changes\n'\
            'B. Go back\n'
        self.assertEqual(test.prompt, expected)
        # miles traveled added
        test.delivery.miles_traveled = 4.7
        test.build_prompt()
        expected =\
            '\n- Revise Delivery -\n'\
            'Please select an option:\n'\
            '1. Revise start time\n'\
            '2. Revise miles traveled\n'\
            '3. Add average speed\n'\
            '4. Add end time\n'\
            'O. Add order\n'\
            'V. View current delivery\n'\
            'S. Save changes\n'\
            'B. Go back\n'
        self.assertEqual(test.prompt, expected)
        # average speed added
        test.delivery.average_speed = 17
        test.build_prompt()
        expected =\
            '\n- Revise Delivery -\n'\
            'Please select an option:\n'\
            '1. Revise start time\n'\
            '2. Revise miles traveled\n'\
            '3. Revise average speed\n'\
            '4. Add end time\n'\
            'O. Add order\n'\
            'V. View current delivery\n'\
            'S. Save changes\n'\
            'B. Go back\n'
        self.assertEqual(test.prompt, expected)
        # end time added
        test.delivery.end_time = datetime.strptime('15:37:42', '%H:%M:%S')
        test.build_prompt()
        expected =\
            '\n- Revise Delivery -\n'\
            'Please select an option:\n'\
            '1. Revise start time\n'\
            '2. Revise miles traveled\n'\
            '3. Revise average speed\n'\
            '4. Revise end time\n'\
            'O. Add order\n'\
            'V. View current delivery\n'\
            'S. Save changes\n'\
            'B. Go back\n'
        self.assertEqual(test.prompt, expected)
        # one order added
        test.delivery.order_id = [0]
        test.delivery.orders = [Order(delivery)]
        test.build_prompt()
        expected =\
            '\n- Revise Delivery -\n'\
            'Please select an option:\n'\
            '1. Revise start time\n'\
            '2. Revise miles traveled\n'\
            '3. Revise average speed\n'\
            '4. Revise end time\n'\
            'O. Revise order/Add order\n'\
            'V. View current delivery\n'\
            'S. Save changes\n'\
            'B. Go back\n'
        self.assertEqual(test.prompt, expected)
        # two orders added
        test.delivery.order_id = [0, 1]
        test.delivery.orders = [Order(delivery), Order(delivery, 1)]
        test.build_prompt()
        expected =\
            '\n- Revise Delivery -\n'\
            'Please select an option:\n'\
            '1. Revise start time\n'\
            '2. Revise miles traveled\n'\
            '3. Revise average speed\n'\
            '4. Revise end time\n'\
            'O. Select an order/Add order\n'\
            'V. View current delivery\n'\
            'S. Save changes\n'\
            'B. Go back\n'
        self.assertEqual(test.prompt, expected)
        # extra stop added
        test.delivery.extra_stop_id = [0]
        test.delivery.extra_stops = [Extra_Stop(delivery)]
        test.build_prompt()
        expected =\
            '\n- Revise Delivery -\n'\
            'Please select an option:\n'\
            '1. Revise start time\n'\
            '2. Revise miles traveled\n'\
            '3. Revise average speed\n'\
            '4. Revise end time\n'\
            'O. Select an order/Add order\n'\
            'E. Revise extra stop\n'\
            'V. View current delivery\n'\
            'S. Save changes\n'\
            'B. Go back\n'
        self.assertEqual(test.prompt, expected)
        # two extra stops added
        test.delivery.extra_stop_id = [0, 1]
        test.delivery.extra_stops =\
            [Extra_Stop(delivery), Extra_Stop(delivery, 1)]
        test.build_prompt()
        expected =\
            '\n- Revise Delivery -\n'\
            'Please select an option:\n'\
            '1. Revise start time\n'\
            '2. Revise miles traveled\n'\
            '3. Revise average speed\n'\
            '4. Revise end time\n'\
            'O. Select an order/Add order\n'\
            'E. Select an extra stop\n'\
            'V. View current delivery\n'\
            'S. Save changes\n'\
            'B. Go back\n'
        self.assertEqual(test.prompt, expected)

    def test_revise_order_build_confirmation(self):
        from objects import Shift, Delivery, Order, Tip
        from processes.revise import Revise_Order
        from utility.utility import now

        # id
        order = Order(Delivery(Shift(now().date())))
        test = Revise_Order(order, test=True)
        test.user_selection = '1'
        test.build_confirmation()
        # tip
        order = Order(Delivery(Shift(now().date())))
        test = Revise_Order(order, test=True)
        test.user_selection = '2'
        test.build_confirmation()
        # distance
        order = Order(Delivery(Shift(now().date())))
        test = Revise_Order(order, test=True)
        test.user_selection = '3'
        test.build_confirmation()
        # end time
        order = Order(Delivery(Shift(now().date())))
        test = Revise_Order(order, test=True)
        test.user_selection = '4'
        test.build_confirmation()
        # save
        order = Order(Delivery(Shift(now().date())))
        test = Revise_Order(order, test=True)
        test.user_selection = 's'
        test.build_confirmation()

    def test_revise_order_build_prompt(self):
        from objects import Shift, Delivery, Order, Tip
        from processes.revise import Revise_Order
        from utility.utility import now

        order = Order(Delivery(Shift(now().date())))
        test = Revise_Order(order, test=True)
        test.build_prompt()
        expected =\
            '\n- Revise Order -\n'\
            '1. Add/edit I.D.\n'\
            '2. Add/edit tip\n'\
            '3. Add/edit miles traveled\n'\
            '4. Add/edit end time\n'\
            'V. View current order values\n'\
            'S. Save changes\n'\
            'B. Go back\n'
        self.assertEqual(test.prompt, expected)

    def test_revise_tip_build_confirmation(self):
        from objects import Tip
        from processes.revise import Revise_Tip

        tip = Tip()
        test = Revise_Tip(tip, test=True)

        # card
        # zero
        expected = 'Add a card tip'
        test.user_selection = '1'
        test.build_confirmation()
        self.assertEqual(test.confirmation, expected)
        # not zero
        expected = 'Edit card tip'
        tip = Tip(card=5)
        test = Revise_Tip(tip, test=True)
        test.user_selection = '1'
        test.build_confirmation()
        self.assertEqual(test.confirmation, expected)

        # cash
        # zero
        expected = 'Add a cash tip'
        tip = Tip()
        test = Revise_Tip(tip, test=True)
        test.user_selection = '2'
        test.build_confirmation()
        self.assertEqual(test.confirmation, expected)
        # not zero
        expected = 'Edit cash tip'
        tip = Tip(cash=5)
        test = Revise_Tip(tip, test=True)
        test.user_selection = '2'
        test.build_confirmation()
        self.assertEqual(test.confirmation, expected)

        # card and cash
        expected = 'Edit/add both card and cash tips'
        tip = Tip()
        test = Revise_Tip(tip, test=True)
        test.user_selection = '3'
        test.build_confirmation()
        self.assertEqual(test.confirmation, expected)

        # unknown
        # zero
        expected = 'Add a tip of unknown type'
        tip = Tip()
        test = Revise_Tip(tip, test=True)
        test.user_selection = 'u'
        test.build_confirmation()
        self.assertEqual(test.confirmation, expected)
        # not zero
        expected = 'Edit tip of unknown type'
        tip = Tip(unknown=5)
        test = Revise_Tip(tip, test=True)
        test.user_selection = 'u'
        test.build_confirmation()
        self.assertEqual(test.confirmation, expected)

        # save
        expected = 'Save changes'
        test.user_selection = 's'
        test.build_confirmation()
        self.assertEqual(test.confirmation, expected)

    def test_revise_tip_build_prompt(self):
        from processes.revise import Revise_Tip

        tip = self.shift.deliveries[0].orders[0].tip
        test = Revise_Tip(tip, test=True)
        test.build_prompt()
        expected =\
            '\n- Revise Tip -\n'\
            'Please select an option:\n'\
            '1. Add a card tip\n'\
            '2. Edit cash tip\n'\
            '3. Edit/add both card and cash tips\n'\
            'U. Add a tip of unknown type\n'\
            "V. View tip's current values\n"\
            'S. Save changes\n'\
            'B. Go back\n'
        
        self.assertEqual(test.prompt, expected)
