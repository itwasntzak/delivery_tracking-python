import unittest
from testing_tools import completed_shift

class Test_Shift(unittest.TestCase):
    def setUp(self):
        import objects
        from utility.utility import To_Datetime
        from utility.utility import now

        self.shift = objects.Shift(now().date())

        self.miles_traveled = 12.3
        self.fuel_economy = 21.2
        self.vehicle_compensation = 13.07
        self.device_compensation = .27
        self.extra_tips_claimed = 3.0
        self.total_hours = 9.7
        self.start_time = To_Datetime('2020-07-13 09:00:00.000').from_datetime()
        self.end_time = To_Datetime('2020-07-13 18:30:00.000').from_datetime()

        self.delivery_1 = objects.Delivery(self.shift, 0)
        self.delivery_2 = objects.Delivery(self.shift, 1)
        self.delivery_3 = objects.Delivery(self.shift, 2)

        self.order_1 = objects.Order(self.delivery_1, 5)
        self.order_2 = objects.Order(self.delivery_2, 10)
        self.order_3 = objects.Order(self.delivery_3, 16)
        self.order_4 = objects.Order(self.delivery_3, 22)

    def test_add_delivery_type_error(self):
        import objects

        with self.assertRaises(TypeError):
            self.shift.add_delivery(objects.Extra_Stop(self.shift))

        with self.assertRaises(TypeError):
            self.shift.add_delivery(objects.Order(self.delivery_1))

        with self.assertRaises(TypeError):
            self.shift.add_delivery(objects.Tip())

        with self.assertRaises(TypeError):
            self.shift.add_delivery(123)

        with self.assertRaises(TypeError):
            self.shift.add_delivery('hello world')

    def test_add_delivery(self):
        self.assertNotIn(0, self.shift.delivery_ids)
        self.assertNotIn(self.delivery_1, self.shift.deliveries)

        self.shift.add_delivery(self.delivery_1)

        self.assertIn(0, self.shift.delivery_ids)
        self.assertIn(self.delivery_1, self.shift.deliveries)


        self.assertNotIn(1, self.shift.delivery_ids)
        self.assertNotIn(self.delivery_2, self.shift.deliveries)

        self.shift.add_delivery(self.delivery_2)

        self.assertIn(1, self.shift.delivery_ids)
        self.assertIn(self.delivery_2, self.shift.deliveries)

    def test_csv(self):

        expected = 'None,None,None,None,None,None,None,None'
        self.assertEqual(self.shift.csv(), expected)

        self.shift.miles_traveled = self.miles_traveled
        self.shift.fuel_economy = self.fuel_economy
        self.shift.vehicle_compensation = self.vehicle_compensation
        self.shift.device_compensation = self.device_compensation
        self.shift.extra_tips_claimed = self.extra_tips_claimed
        self.shift.total_hours = self.total_hours
        self.shift.start_time = self.start_time
        self.shift.end_time = self.end_time

        expected = '{},{},{},{},{},{},{},{}'.format(
            self.miles_traveled, self.fuel_economy, self.vehicle_compensation,
            self.device_compensation, self.extra_tips_claimed,
            self.total_hours, self.start_time, self.end_time)
        self.assertEqual(self.shift.csv(), expected)
    
    def test_all_tips(self):
        import objects

        self.assertEqual(self.shift.all_tips(), [])

        self.shift = completed_shift()

        expected_list = [
            objects.Tip(cash=5).total_amount(),
            objects.Tip().total_amount(),
            objects.Tip(card=2.78).total_amount(),
            objects.Tip(card=3.41, cash=3).total_amount(),
            objects.Tip(card=3.11).total_amount(),
            objects.Tip(cash=2.71).total_amount()
        ]

        test_list = [tip.total_amount() for tip in self.shift.all_tips()]

        self.assertEqual(test_list, expected_list)
    
    def test_card_tips(self):
        import objects

        self.assertEqual(self.shift.all_tips(), [])

        self.shift = completed_shift()

        expected_list = [
            objects.Tip(card=2.78).card,
            objects.Tip(card=3.41, cash=3).card,
            objects.Tip(card=3.11).card,
        ]

        test_list = [tip.card for tip in self.shift.card_tips()]

        self.assertEqual(test_list, expected_list)
    
    def test_cash_tips(self):
        import objects

        self.assertEqual(self.shift.all_tips(), [])

        self.shift = completed_shift()

        expected_list = [
            objects.Tip(cash=5).cash,
            objects.Tip(card=3.41, cash=3).cash,
            objects.Tip(cash=2.71).cash
        ]

        test_list = [tip.cash for tip in self.shift.cash_tips()]

        self.assertEqual(test_list, expected_list)


class Test_Delivery(unittest.TestCase):
    def setUp(self):
        from objects import Delivery, Shift
        from utility.utility import now
        self.shift = Shift(now().date())
        self.delivery = Delivery(self.shift)

    def test_add_order_type_error(self):
        import objects

        with self.assertRaises(TypeError):
            self.delivery.add_order(self.shift)

        with self.assertRaises(TypeError):
            self.delivery.add_order(self.delivery)

        with self.assertRaises(TypeError):
            self.shift.add_delivery(objects.Extra_Stop(self.shift))

        with self.assertRaises(TypeError):
            self.shift.add_delivery(objects.Tip())

        with self.assertRaises(TypeError):
            self.shift.add_delivery(123)

        with self.assertRaises(TypeError):
            self.shift.add_delivery('hello world')

        with self.assertRaises(TypeError):
            self.shift.add_delivery([1, 2, 3, 4])
    
    def test_add_order(self):
        from objects import Order

        self.assertEqual(self.delivery.orders, [])

        order_1 = Order(self.delivery, 5)
        self.delivery.add_order(order_1)
        self.assertIn(5, self.delivery.order_ids)
        self.assertIn(order_1, self.delivery.orders)

        order_2 = Order(self.delivery, 748)
        self.delivery.add_order(order_2)
        self.assertIn(748, self.delivery.order_ids)
        self.assertIn(order_2, self.delivery.orders)
 
    def test_csv(self):
        from utility.utility import To_Datetime

        expected = 'None,None,None,None'
        self.assertEqual(self.delivery.csv(), expected)

        start_time = To_Datetime('2020-08-23 12:03:00.000').from_datetime()
        end_time = To_Datetime('2020-08-23 12:37:00.000').from_datetime()
        distance = 7.2
        average_speed = 21

        self.delivery.start_time = start_time
        self.delivery.end_time = end_time
        self.delivery.miles_traveled = distance
        self.delivery.average_speed = average_speed

        expected = '{},{},{},{}'.format(distance, average_speed, start_time, end_time)
        self.assertEqual(self.delivery.csv(), expected)
