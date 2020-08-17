from unittest.mock import patch
import unittest

import objects
from utility.user_input import decimal

# objects
class TestShift(unittest.TestCase):
    def setUp(self):
        from utility.utility import now
        self.shift = objects.Shift(now().date())
    
    def test_add_delivery(self):
        import objects

        delivery_1 = objects.Delivery(self.shift)

        with self.assertRaises(TypeError):
            self.shift.add_delivery(objects.Extra_Stop(self.shift))
        with self.assertRaises(TypeError):
            self.shift.add_delivery(objects.Order(delivery_1))
        with self.assertRaises(TypeError):
            self.shift.add_delivery(objects.Tip())
        with self.assertRaises(TypeError):
            self.shift.add_delivery(123)
        with self.assertRaises(TypeError):
            self.shift.add_delivery('hello world')

        self.assertNotIn(0, self.shift.delivery_ids)
        self.assertNotIn(delivery_1, self.shift.deliveries)
        self.shift.add_delivery(delivery_1)
        self.assertIn(0, self.shift.delivery_ids)
        self.assertIn(delivery_1, self.shift.deliveries)

        delivery_2 = objects.Delivery(self.shift)
        self.assertNotIn(1, self.shift.delivery_ids)
        self.assertNotIn(delivery_2, self.shift.deliveries)
        self.shift.add_delivery(delivery_2)
        self.assertIn(1, self.shift.delivery_ids)
        self.assertIn(delivery_2, self.shift.deliveries)

    def test_csv(self):
        from utility.utility import To_Datetime
        not_any = 'None,None,None,None,None,None,None,None'
        self.assertEqual(self.shift.csv(), not_any)
        self.shift.miles_traveled = 12.3
        self.shift.fuel_economy = 21.2
        self.shift.vehicle_compensation = 13.07
        self.shift.device_compensation = .27
        self.shift.extra_tips_claimed = 3.0
        self.shift.total_hours = 9.7
        self.shift.start_time = To_Datetime('2020-07-13 09:00:00.000').from_datetime()
        self.shift.end_time = To_Datetime('2020-07-13 18:30:00.000').from_datetime()
        expected =\
            '12.3,21.2,13.07,0.27,3.0,9.7,2020-07-13 09:00:00,2020-07-13 18:30:00'
        self.assertEqual(self.shift.csv(), expected)
    
    @patch('objects.Shift.input_device_compensation', return_value=.4)
    def test_input_device_compensation(self, decimal):
        expected = '$0.4\nIs this correct?\t[Y/N]'
        self.assertEqual(self.shift.input_device_compensation(), expected)


class TestDelivery(unittest.TestCase):
    def setUp(self):
        from objects import Delivery, Shift
        from utility.utility import now
        self.shift = Shift(now().date())
        self.delivery = Delivery(self.shift)

    def test_add_order(self):
        import objects

        with self.assertRaises(TypeError):
            self.delivery.add_order(self.shift)
 
# track
# consolidate
# load
# select
# menus
