import unittest

# todo: convience tests; load_shift_deliveries, load_shift_extra_stops, load_delivery_orders, 
#           load_delivery_extra_stops
# todo: none automated tests

# menus hasnt even been looked at on how to unittest
# utility hasnt even been looked at on how to unittest

# select is ready to have tests written
# view is ready to have tests written

def completed_shift():
    import objects
    from utility.utility import To_Datetime
    from utility.utility import now

    # shift
    shift = objects.Shift(now().date())
    shift.miles_traveled = 12.3
    shift.fuel_economy = 21.2
    shift.vehicle_compensation = 13.07
    shift.device_compensation = .27
    shift.extra_tips_claimed = 3.0
    shift.total_hours = 9.7
    shift.start_time =\
        To_Datetime('2020-07-13 09:00:00.100').from_datetime()
    shift.end_time =\
        To_Datetime('2020-07-13 18:30:00.100').from_datetime()
    shift.carry_out_tips = [objects.Tip(card=3.11), objects.Tip(cash=2.71)]

    # delivery 1
    delivery_1 = objects.Delivery(shift, 0)
    delivery_1.start_time =\
        To_Datetime('2020-07-13 10:30:00.100').from_datetime()
    delivery_1.end_time =\
        To_Datetime('2020-07-13 10:55:00.100').from_datetime()
    delivery_1.miles_traveled = 3.7
    delivery_1.average_speed = 21
    # order
    order_1 = objects.Order(delivery_1, 7)
    order_1.end_time =\
        To_Datetime('2020-07-13 10:43:00.100').from_datetime()
    order_1.miles_traveled = 1.8
    order_1.tip = objects.Tip(cash=5)
    # add order to delivery
    delivery_1.order_ids.append(order_1.id)
    delivery_1.orders.append(order_1)
    # add delivery to shift
    shift.delivery_ids.append(delivery_1.id)
    shift.deliveries.append(delivery_1)

    # delivery 2
    delivery_2 = objects.Delivery(shift, 1)
    delivery_2.start_time =\
        To_Datetime('2020-07-13 11:20:00.100').from_datetime()
    delivery_2.end_time =\
        To_Datetime('2020-07-13 11:47:00.100').from_datetime()
    delivery_2.miles_traveled = .7
    delivery_2.average_speed = 14
    # order
    order_2 = objects.Order(delivery_2, 36)
    order_2.end_time =\
        To_Datetime('2020-07-13 11:31:00.100').from_datetime()
    order_2.miles_traveled = 3.1
    order_2.tip = objects.Tip()
    # add order to delivery
    delivery_2.order_ids.append(order_2.id)
    delivery_2.orders.append(order_2)
    # extra stop
    extra_stop_2 = objects.Extra_Stop(delivery_2, 1)
    extra_stop_2.start_time =\
        To_Datetime('2020-08-25 13:17:38.100').from_datetime()
    extra_stop_2.location = 'mongolian grill'
    extra_stop_2.reason = 'trade food'
    extra_stop_2.miles_traveled = 4.1
    extra_stop_2.end_time =\
        To_Datetime('2020-08-25 13:27:57.100').from_datetime()
    delivery_2.extra_stop_ids.append(extra_stop_2.id)
    delivery_2.extra_stops.append(extra_stop_2)
    # add delivery to shift
    shift.delivery_ids.append(delivery_2.id)
    shift.deliveries.append(delivery_2)

    # delivery 3
    delivery_3 = objects.Delivery(shift, 2)
    delivery_3.start_time =\
        To_Datetime('2020-07-13 12:12:00.100').from_datetime()
    delivery_3.end_time =\
        To_Datetime('2020-07-13 12:41:00.100').from_datetime()
    delivery_3.miles_traveled = 6.7
    delivery_3.average_speed = 23
    # order 1
    order_3 = objects.Order(delivery_3, 47)
    order_3.end_time =\
        To_Datetime('2020-07-13 12:28:00.100').from_datetime()
    order_3.miles_traveled = 3.4
    order_3.tip = objects.Tip(card=2.78)
    # add order to delivery
    delivery_3.order_ids.append(order_3.id)
    delivery_3.orders.append(order_3)
    # order 2
    order_4 = objects.Order(delivery_3, 58)
    order_4.end_time =\
        To_Datetime('2020-07-13 12:28:00.100').from_datetime()
    order_4.miles_traveled = 3.4
    order_4.tip = objects.Tip(card=3.41, cash=3)
    # add order to delivery
    delivery_3.order_ids.append(order_4.id)
    delivery_3.orders.append(order_4)
    # add delivery to shift
    shift.delivery_ids.append(delivery_3.id)
    shift.deliveries.append(delivery_3)

    # extra stop 1
    extra_stop_1 = objects.Extra_Stop(shift, 0)
    extra_stop_1 = objects.Extra_Stop(shift)
    extra_stop_1.start_time =\
        To_Datetime('2020-08-25 10:05:33.100').from_datetime()
    extra_stop_1.location = 'bank'
    extra_stop_1.reason = 'change'
    extra_stop_1.miles_traveled = 3.6
    extra_stop_1.end_time =\
        To_Datetime('2020-08-25 10:15:33.100').from_datetime()
    # add extra stop to shift
    shift.extra_stop_ids.append(extra_stop_1.id)
    shift.extra_stops.append(extra_stop_1)

    # extra stop 2
    extra_stop_3 = objects.Extra_Stop(shift, 2)
    extra_stop_3 = objects.Extra_Stop(shift)
    extra_stop_3.start_time =\
        To_Datetime('2020-08-25 13:17:38.100').from_datetime()
    extra_stop_3.location = 'mongolian grill'
    extra_stop_3.reason = 'trade food'
    extra_stop_3.miles_traveled = 4.1
    extra_stop_3.end_time =\
        To_Datetime('2020-08-25 13:27:57.100').from_datetime()
    # add extra stop to shift
    shift.extra_stop_ids.append(extra_stop_3.id)
    shift.extra_stops.append(extra_stop_3)

    # split
    split = objects.Split(shift)
    split.start_time = To_Datetime('2020-08-25 14:03:57.100').from_datetime()
    split.miles_traveled = 3.1
    split.end_time = To_Datetime('2020-08-25 16:03:57.100').from_datetime()
    shift.split = split

    return shift


def get_tip(card=False, cash=False, both=False, unknown=False):
    import random
    from objects import Tip

    chance = random.randint(0, 3)

    # card tip
    if card is True or chance == 0:
        return Tip(random.uniform(.01, 20.0))
    # cash tip
    if cash is True or chance == 1:
        return Tip(cash=random.uniform(.01, 20.0))
    # card & cash tip
    if both is True or chance == 2:
        card_tip = random.uniform(.01, 20.0)
        cash_tip = random.uniform(.01, 20.0)
        return Tip(card_tip, cash_tip)
    # unknown
    if unknown is True or chance == 3:
        return Tip(unknown=random.uniform(.01, 20.0))

# objects
class TestShift(unittest.TestCase):
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


class TestDelivery(unittest.TestCase):
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


# track
class TestTracking(unittest.TestCase):
    def setUp(self):
        from os import mkdir, path
        from resources.system_names import\
            data_directory, shifts_directory

        self.shift = completed_shift()

        mkdir(data_directory)
        mkdir(path.join(data_directory, shifts_directory))

    def tearDown(self):
        from os import rmdir, path
        from resources.system_names import\
            data_directory, shifts_directory
        
        rmdir(path.join(data_directory, shifts_directory))
        rmdir(data_directory)

    def test_end_shift(self):
        from os import mkdir, path, remove, rmdir
        from processes.track import end_shift
        from utility.utility import To_Datetime

        file_list = self.shift.file_list()

        # make directory
        mkdir(file_list['directory'])

        # check that files dont exist
        self.assertFalse(path.exists(file_list['end_time']))
        self.assertFalse(path.exists(file_list['miles_traveled']))
        self.assertFalse(path.exists(file_list['fuel_economy']))
        self.assertFalse(path.exists(file_list['vehicle_compensation']))
        self.assertFalse(path.exists(file_list['device_compensation']))
        self.assertFalse(path.exists(file_list['total_hours']))
        self.assertFalse(path.exists(file_list['extra_tips_claimed']))

        # run function
        end_shift(self.shift)

        # check that files do exist
        self.assertTrue(path.exists(file_list['end_time']))
        self.assertTrue(path.exists(file_list['miles_traveled']))
        self.assertTrue(path.exists(file_list['fuel_economy']))
        self.assertTrue(path.exists(file_list['vehicle_compensation']))
        self.assertTrue(path.exists(file_list['device_compensation']))
        self.assertTrue(path.exists(file_list['total_hours']))
        self.assertTrue(path.exists(file_list['extra_tips_claimed']))

        # check the correct data was written to files
        # end time
        with open(file_list['end_time'], 'r') as end_time_file:
            self.assertEqual(
                To_Datetime(end_time_file.readline()).from_datetime(),
                self.shift.end_time)
        # distance
        with open(file_list['miles_traveled'], 'r') as miles_traveled_file:
            self.assertEqual(
                float(miles_traveled_file.readline()), self.shift.miles_traveled)
        # fuel economy
        with open(file_list['fuel_economy'], 'r') as fuel_economy_file:
            self.assertEqual(
                float(fuel_economy_file.readline()), self.shift.fuel_economy)
        # vehicle compensation
        with open(file_list['vehicle_compensation'], 'r') as vehicle_compensation_file:
            self.assertEqual(
                float(vehicle_compensation_file.readline()),
                self.shift.vehicle_compensation)
        # device compensation
        with open(file_list['device_compensation'], 'r') as device_compensation_file:
            self.assertEqual(
                float(device_compensation_file.readline()),
                self.shift.device_compensation)
        # total hours
        with open(file_list['total_hours'], 'r') as total_hours_file:
            self.assertEqual(
                float(total_hours_file.readline()), self.shift.total_hours)
        # extra tips claimed
        with open(file_list['extra_tips_claimed'], 'r') as extra_tips_claimed_file:
            self.assertEqual(
                float(extra_tips_claimed_file.readline()),
                self.shift.extra_tips_claimed)

        # delete files and directory
        remove(file_list['end_time'])
        remove(file_list['miles_traveled'])
        remove(file_list['fuel_economy'])
        remove(file_list['vehicle_compensation'])
        remove(file_list['device_compensation'])
        remove(file_list['total_hours'])
        remove(file_list['extra_tips_claimed'])
        rmdir(file_list['directory'])

    def test_start_shift(self):
        from os import mkdir, path, remove, rmdir
        from processes.track import start_shift
        from utility.utility import To_Datetime

        file_list = self.shift.file_list()

        # check that file and directory dont exist
        self.assertFalse(path.exists(file_list['directory']))
        self.assertFalse(path.exists(file_list['start_time']))

        # run function
        start_shift(self.shift)

        # check that the file and directory were created
        self.assertTrue(path.exists(file_list['directory']))
        self.assertTrue(path.exists(file_list['start_time']))

        # check that the correct data was saved
        with open(file_list['start_time'], 'r') as start_time_file:
            self.assertEqual(
                To_Datetime(start_time_file.readline()).from_datetime(),
                self.shift.start_time)

        # delete file and directory
        remove(file_list['start_time'])
        rmdir(file_list['directory'])

    def test_end_delivery(self):
        from os import mkdir, path, remove, rmdir
        from processes.track import end_delivery
        from utility.utility import To_Datetime

        delivery = self.shift.deliveries[0]
        file_list = delivery.file_list()

        # make directories
        mkdir(self.shift.file_list()['directory'])
        mkdir(file_list['directory'])

        # check that files dont exist
        self.assertFalse(path.exists(file_list['miles_traveled']))
        self.assertFalse(path.exists(file_list['average_speed']))
        self.assertFalse(path.exists(file_list['end_time']))

        # run function
        end_delivery(delivery)

        # check that files were created
        self.assertTrue(path.exists(file_list['miles_traveled']))
        self.assertTrue(path.exists(file_list['average_speed']))
        self.assertTrue(path.exists(file_list['end_time']))

        # check that the correct data was written to the files
        with open(file_list['miles_traveled'], 'r') as miles_traveled_file:
            self.assertEqual(
                float(miles_traveled_file.readline()), delivery.miles_traveled)
        with open(file_list['average_speed'], 'r') as average_speed_file:
            self.assertEqual(
                int(average_speed_file.readline()), delivery.average_speed)
        with open(file_list['end_time'], 'r') as end_time_file:
            self.assertEqual(
                To_Datetime(end_time_file.readline()).from_datetime(),
                delivery.end_time)

        # delete files and directories
        remove(file_list['miles_traveled'])
        remove(file_list['average_speed'])
        remove(file_list['end_time'])
        rmdir(file_list['directory'])
        rmdir(self.shift.file_list()['directory'])

    def test_start_delivery(self):
        from os import mkdir, path, remove, rmdir
        from processes.track import start_delivery
        from utility.utility import To_Datetime

        delivery = self.shift.deliveries[0]
        file_list = delivery.file_list()

        # make directories
        mkdir(self.shift.file_list()['directory'])

        # check that file and directory dont exist
        self.assertFalse(path.exists(file_list['directory']))
        self.assertFalse(path.exists(file_list['start_time']))

        # run function
        start_delivery(delivery)

        # check that file and directory were created
        self.assertTrue(path.exists(file_list['directory']))
        self.assertTrue(path.exists(file_list['start_time']))

        # check that the correct data was written to file
        with open(file_list['start_time'], 'r') as start_time_file:
            self.assertEqual(
                To_Datetime(start_time_file.readline()).from_datetime(),
                delivery.start_time)
        
        # delete file and directories
        remove(file_list['start_time'])
        rmdir(file_list['directory'])
        rmdir(self.shift.file_list()['directory'])

    def test_track_order(self):
        import objects
        from os import mkdir, path, remove, rmdir
        from processes.track import track_order
        from utility.utility import To_Datetime

        delivery = self.shift.deliveries[0]
        order = delivery.orders[0]
        file_list = order.file_list()

        # make directory
        mkdir(self.shift.file_list()['directory'])
        mkdir(delivery.file_list()['directory'])

        # check that directory and files dont exist
        self.assertFalse(path.exists(file_list['directory']))
        self.assertFalse(path.exists(file_list['id']))
        self.assertFalse(path.exists(file_list['tip']))
        self.assertFalse(path.exists(file_list['miles_traveled']))
        self.assertFalse(path.exists(file_list['end_time']))

        # run function
        track_order(order)

        # check that directory and files were created
        self.assertTrue(path.exists(file_list['directory']))
        self.assertTrue(path.exists(file_list['id']))
        self.assertTrue(path.exists(file_list['tip']))
        self.assertTrue(path.exists(file_list['miles_traveled']))
        self.assertTrue(path.exists(file_list['end_time']))

        # check that the correct data was written to the files
        with open(file_list['id'], 'r') as id_file:
            self.assertEqual(int(id_file.readline()), order.id)
        with open(file_list['tip'], 'r') as tip_file:
            tip_data = tip_file.readline().split(',')
            self.assertEqual(
                objects.Tip(tip_data[0], tip_data[1], tip_data[2]).csv(),
                order.tip.csv())
        with open(file_list['miles_traveled'], 'r') as miles_traveled_file:
            self.assertEqual(
                float(miles_traveled_file.readline()), order.miles_traveled)
        with open(file_list['end_time'], 'r') as end_time_file:
            self.assertEqual(
                To_Datetime(end_time_file.readline()).from_datetime(),
                order.end_time)

        # delete files and directories
        remove(file_list['id'])
        remove(file_list['tip'])
        remove(file_list['miles_traveled'])
        remove(file_list['end_time'])
        rmdir(file_list['directory'])
        rmdir(delivery.file_list()['directory'])
        rmdir(self.shift.file_list()['directory'])

    def test_end_split(self):
        import objects
        from os import mkdir, path, remove, rmdir
        from processes.track import end_split
        from utility.utility import To_Datetime, now

        split = self.shift.split

        file_list = split.file_list()

        # make directories needed for split
        mkdir(self.shift.file_list()['directory'])
        mkdir(file_list['directory'])
        
        # check that files dont exist
        self.assertFalse(path.exists(file_list['miles_traveled']))
        self.assertFalse(path.exists(file_list['end_time']))

        # run function
        end_split(split)

        # check that files were created
        self.assertTrue(path.exists(file_list['miles_traveled']))
        self.assertTrue(path.exists(file_list['end_time']))

        # check that the correct data was written to files
        with open(file_list['miles_traveled'], 'r') as miles_traveled_file:
            self.assertEqual(
                float(miles_traveled_file.readline()), split.miles_traveled)
        with open(file_list['end_time'], 'r') as end_time_file:
            self.assertEqual(
                To_Datetime(end_time_file.readline()).from_datetime(),
                split.end_time)

        # delete files and directories
        remove(file_list['miles_traveled'])
        remove(file_list['end_time'])
        rmdir(file_list['directory'])
        rmdir(self.shift.file_list()['directory'])

    def test_start_split(self):
        import objects
        from os import mkdir, path, remove, rmdir
        from processes.track import start_split
        from utility.utility import To_Datetime, now

        split = self.shift.split

        file_list = split.file_list()

        # make directories needed for split
        mkdir(self.shift.file_list()['directory'])

        # check that files dont exist
        self.assertFalse(path.exists(file_list['directory']))
        self.assertFalse(path.exists(file_list['start_time']))

        # run function
        start_split(split)

        # check that files were created
        self.assertTrue(path.exists(file_list['directory']))
        self.assertTrue(path.exists(file_list['start_time']))

        # check that the correct data was written to the file
        with open(file_list['start_time'], 'r') as start_time_file:
            self.assertEqual(
                To_Datetime(start_time_file.readline()).from_datetime(),
                split.start_time)

        # delete files and directories
        remove(file_list['start_time'])
        rmdir(file_list['directory'])
        rmdir(self.shift.file_list()['directory'])

    def test_track_extra_stop_shift(self):
        import objects
        from os import mkdir, path, remove, rmdir
        from processes.track import track_extra_stop
        from utility.utility import To_Datetime, now

        extra_stop = self.shift.extra_stops[0]
        file_list = extra_stop.file_list()

        # make directories needed for split
        mkdir(self.shift.file_list()['directory'])

        # check that files dont exist
        self.assertFalse(path.exists(file_list['directory']))
        self.assertFalse(path.exists(file_list['start_time']))
        self.assertFalse(path.exists(file_list['location']))
        self.assertFalse(path.exists(file_list['reason']))
        self.assertFalse(path.exists(file_list['miles_traveled']))
        self.assertFalse(path.exists(file_list['end_time']))

        # run function
        track_extra_stop(extra_stop)

        # check that files were created
        self.assertTrue(path.exists(file_list['directory']))
        self.assertTrue(path.exists(file_list['start_time']))
        self.assertTrue(path.exists(file_list['location']))
        self.assertTrue(path.exists(file_list['reason']))
        self.assertTrue(path.exists(file_list['miles_traveled']))
        self.assertTrue(path.exists(file_list['end_time']))

        # check that correct data was written to files
        with open(file_list['start_time'], 'r') as start_time_file:
            self.assertEqual(
                To_Datetime(start_time_file.readline()).from_datetime(),
                extra_stop.start_time)
        with open(file_list['location'], 'r') as location_file:
            self.assertEqual(location_file.readline(), extra_stop.location)
        with open(file_list['reason'], 'r') as reason_file:
            self.assertEqual(reason_file.readline(), extra_stop.reason)
        with open(file_list['miles_traveled'], 'r') as miles_traveled_file:
            self.assertEqual(
                float(miles_traveled_file.readline()),
                extra_stop.miles_traveled)
        with open(file_list['end_time'], 'r') as end_time_file:
            self.assertEqual(
                To_Datetime(end_time_file.readline()).from_datetime(),
                extra_stop.end_time)

        # delete files and directories
        remove(file_list['start_time'])
        remove(file_list['location'])
        remove(file_list['reason'])
        remove(file_list['miles_traveled'])
        remove(file_list['end_time'])
        rmdir(file_list['directory'])
        rmdir(self.shift.file_list()['directory'])

    def test_track_extra_stop_delivery(self):
        import objects
        from os import mkdir, path, remove, rmdir
        from processes.track import track_extra_stop
        from utility.utility import To_Datetime, now

        delivery = self.shift.deliveries[1]
        extra_stop = delivery.extra_stops[0]

        file_list = extra_stop.file_list()

        # make directories needed for split
        mkdir(self.shift.file_list()['directory'])
        mkdir(delivery.file_list()['directory'])


        # check that files dont exist
        self.assertFalse(path.exists(file_list['directory']))
        self.assertFalse(path.exists(file_list['location']))
        self.assertFalse(path.exists(file_list['reason']))
        self.assertFalse(path.exists(file_list['miles_traveled']))
        self.assertFalse(path.exists(file_list['end_time']))

        # run function
        track_extra_stop(extra_stop)

        # check that files were created
        self.assertTrue(path.exists(file_list['directory']))
        self.assertTrue(path.exists(file_list['location']))
        self.assertTrue(path.exists(file_list['reason']))
        self.assertTrue(path.exists(file_list['miles_traveled']))
        self.assertTrue(path.exists(file_list['end_time']))

        # check that correct data was written to files
        with open(file_list['location'], 'r') as location_file:
            self.assertEqual(location_file.readline(), extra_stop.location)
        with open(file_list['reason'], 'r') as reason_file:
            self.assertEqual(reason_file.readline(), extra_stop.reason)
        with open(file_list['miles_traveled'], 'r') as miles_traveled_file:
            self.assertEqual(
                float(miles_traveled_file.readline()),
                extra_stop.miles_traveled)
        with open(file_list['end_time'], 'r') as end_time_file:
            self.assertEqual(
                To_Datetime(end_time_file.readline()).from_datetime(),
                extra_stop.end_time)

        # delete files and directories
        remove(file_list['location'])
        remove(file_list['reason'])
        remove(file_list['miles_traveled'])
        remove(file_list['end_time'])
        rmdir(file_list['directory'])
        rmdir(delivery.file_list()['directory'])
        rmdir(self.shift.file_list()['directory'])


# consolidate
class TestConsolidate(unittest.TestCase):
    # todo: a lot of these tests need to add more cases of cosolidating objects
    #           for the sake of properly testing the completed ids

    def setUp(self):
        from resources.system_names import\
            data_directory, shifts_directory
        from os import mkdir, path

        self.shift = completed_shift()
        mkdir(data_directory)
        mkdir(path.join(data_directory, shifts_directory))
        mkdir(self.shift.file_list()['directory'])

    def tearDown(self):
        from resources.system_names import\
            data_directory, shifts_directory
        from os import rmdir, path

        rmdir(self.shift.file_list()['directory'])
        rmdir(path.join(data_directory, shifts_directory))
        rmdir(data_directory)

    def test_consolidate_shift(self):
        from processes.consolidate import consolidate_shift
        from os import mkdir, remove, rmdir, path
        from utility.utility import To_Datetime

        file_list = self.shift.file_list()

        # write indavidual files
        # start time
        with open(file_list['start_time'], 'w') as start_time_file:
            start_time_file.write(str(self.shift.start_time))
        # end time
        with open(file_list['end_time'], 'w') as end_time_file:
            end_time_file.write(str(self.shift.end_time))
        # distance
        with open(file_list['miles_traveled'], 'w') as miles_traveled_file:
            miles_traveled_file.write(str(self.shift.miles_traveled))
        # fuel economy
        with open(file_list['fuel_economy'], 'w') as fuel_economy_file:
            fuel_economy_file.write(str(self.shift.fuel_economy))
        # vehicle compensation
        with open(file_list['vehicle_compensation'], 'w') as vehicle_compensation_file:
            vehicle_compensation_file.write(str(self.shift.vehicle_compensation))
        # device compensation
        with open(file_list['device_compensation'], 'w') as device_compensation_file:
            device_compensation_file.write(str(self.shift.device_compensation))
        # total hours
        with open(file_list['total_hours'], 'w') as total_hours_file:
            total_hours_file.write(str(self.shift.total_hours))
        # extra tips claimed
        with open(file_list['extra_tips_claimed'], 'w') as extra_tips_claimed_file:
            extra_tips_claimed_file.write(str(self.shift.extra_tips_claimed))

        # check that files were created and the others dont
        self.assertTrue(path.exists(file_list['start_time']))
        self.assertTrue(path.exists(file_list['end_time']))
        self.assertTrue(path.exists(file_list['miles_traveled']))
        self.assertTrue(path.exists(file_list['fuel_economy']))
        self.assertTrue(path.exists(file_list['vehicle_compensation']))
        self.assertTrue(path.exists(file_list['device_compensation']))
        self.assertTrue(path.exists(file_list['total_hours']))
        self.assertTrue(path.exists(file_list['extra_tips_claimed']))
        self.assertFalse(path.exists(file_list['info']))
        self.assertFalse(path.exists(file_list['completed_ids']))

        # run function
        consolidate_shift(self.shift)

        # check indavidual files were deleted and two was created
        self.assertFalse(path.exists(file_list['start_time']))
        self.assertFalse(path.exists(file_list['end_time']))
        self.assertFalse(path.exists(file_list['miles_traveled']))
        self.assertFalse(path.exists(file_list['fuel_economy']))
        self.assertFalse(path.exists(file_list['vehicle_compensation']))
        self.assertFalse(path.exists(file_list['device_compensation']))
        self.assertFalse(path.exists(file_list['total_hours']))
        self.assertFalse(path.exists(file_list['extra_tips_claimed']))
        self.assertTrue(path.exists(file_list['info']))
        self.assertTrue(path.exists(file_list['completed_ids']))

        # check that the correct data was written to the files
        # info file
        with open(file_list['info'], 'r') as info_file:
            data = info_file.readline().split(',')
            self.assertEqual(float(data[0]), self.shift.miles_traveled)
            self.assertEqual(float(data[1]), self.shift.fuel_economy)
            self.assertEqual(float(data[2]), self.shift.vehicle_compensation)
            self.assertEqual(float(data[3]), self.shift.device_compensation)
            self.assertEqual(float(data[4]), self.shift.extra_tips_claimed)
            self.assertEqual(float(data[5]), self.shift.total_hours)
            self.assertEqual(
                To_Datetime(data[6]).from_datetime(), self.shift.start_time)
            self.assertEqual(
                To_Datetime(data[7]).from_datetime(), self.shift.end_time)
        # id file
        with open(file_list['completed_ids'], 'r') as completed_ids_file:
            self.assertEqual(
                To_Datetime(completed_ids_file.readline()).from_date().date(),
                self.shift.id)

        # delete files and directory
        remove(file_list['completed_ids'])
        remove(file_list['info'])

    def test_consolidate_delivery(self):
        from processes.consolidate import consolidate_delivery
        from os import mkdir, remove, rmdir, path
        from utility.utility import To_Datetime
        
        delivery = self.shift.deliveries[0]
        file_list = delivery.file_list()

        # make directory
        mkdir(file_list['directory'])

        # create indavidual files
        with open(file_list['start_time'], 'w') as start_time_file:
            start_time_file.write(str(delivery.start_time))
        with open(file_list['miles_traveled'], 'w') as miles_traveled_file:
            miles_traveled_file.write(str(delivery.miles_traveled))
        with open(file_list['average_speed'], 'w') as average_speed_file:
            average_speed_file.write(str(delivery.average_speed))
        with open(file_list['end_time'], 'w') as end_time_file:
            end_time_file.write(str(delivery.end_time))

        # check that files were created and others dont exist
        self.assertTrue(path.exists(file_list['start_time']))
        self.assertTrue(path.exists(file_list['miles_traveled']))
        self.assertTrue(path.exists(file_list['average_speed']))
        self.assertTrue(path.exists(file_list['end_time']))
        self.assertFalse(path.exists(file_list['info']))
        self.assertFalse(path.exists(file_list['completed_ids']))

        # run the function
        consolidate_delivery(delivery)

        # check that the files were deleted and created
        self.assertFalse(path.exists(file_list['start_time']))
        self.assertFalse(path.exists(file_list['miles_traveled']))
        self.assertFalse(path.exists(file_list['average_speed']))
        self.assertFalse(path.exists(file_list['end_time']))
        self.assertTrue(path.exists(file_list['info']))
        self.assertTrue(path.exists(file_list['completed_ids']))

        # check that correct data was written to files
        with open(file_list['info'], 'r') as info_file:
            data = info_file.readline().split(',')
            self.assertEqual(float(data[0]), delivery.miles_traveled)
            self.assertEqual(int(data[1]), delivery.average_speed)
            self.assertEqual(
                To_Datetime(data[2]).from_datetime(), delivery.start_time)
            self.assertEqual(
                To_Datetime(data[3]).from_datetime(), delivery.end_time)
        with open(file_list['completed_ids'], 'r') as completed_ids_file:
            self.assertEqual(int(completed_ids_file.readline()), delivery.id)

        # delete files and directories
        remove(file_list['completed_ids'])
        remove(file_list['info'])
        rmdir(file_list['directory'])

    def test_consolidate_order(self):
        from objects import Tip
        from os import mkdir, remove, rmdir, path
        from processes.consolidate import consolidate_order
        from utility.utility import To_Datetime
        
        delivery = self.shift.deliveries[0]
        parent_directory = delivery.file_list()['directory']
        order = delivery.orders[0]
        file_list = order.file_list()
        
        # create directories
        mkdir(parent_directory)
        mkdir(file_list['directory'])

        # create indavidual files
        with open(file_list['id'], 'w') as id_file:
            id_file.write(str(order.id))
        with open(file_list['tip'], 'w') as tip_file:
            tip_file.write(str(order.tip.csv()))
        with open(file_list['miles_traveled'], 'w') as miles_traveled_file:
            miles_traveled_file.write(str(order.miles_traveled))
        with open(file_list['end_time'], 'w') as end_time_file:
            end_time_file.write(str(order.end_time))

        # check that files were created and others dont exist
        self.assertTrue(path.exists(file_list['id']))
        self.assertTrue(path.exists(file_list['tip']))
        self.assertTrue(path.exists(file_list['miles_traveled']))
        self.assertTrue(path.exists(file_list['end_time']))
        self.assertFalse(path.exists(file_list['info']))
        self.assertFalse(path.exists(file_list['completed_ids']))

        # run the function
        consolidate_order(order)

        # check that the files were deleted and created
        self.assertFalse(path.exists(file_list['id']))
        self.assertFalse(path.exists(file_list['tip']))
        self.assertFalse(path.exists(file_list['miles_traveled']))
        self.assertFalse(path.exists(file_list['end_time']))
        self.assertTrue(path.exists(file_list['info']))
        self.assertTrue(path.exists(file_list['completed_ids']))

        # check that correct data was written to files
        with open(file_list['info'], 'r') as info_file:
            data = info_file.readline().split(',')
            self.assertEqual(
                Tip(float(data[0]), float(data[1]), float(data[2])).csv(),
                order.tip.csv())
            self.assertEqual(float(data[3]), order.miles_traveled)
            self.assertEqual(
                To_Datetime(data[4]).from_datetime(), order.end_time)
        with open(file_list['completed_ids'], 'r') as completed_ids_file:
            self.assertEqual(int(completed_ids_file.readline()), order.id)

        # delete files and directories
        remove(file_list['info'])
        remove(file_list['completed_ids'])
        rmdir(parent_directory)

    def test_consolidate_split(self):
        from objects import Split
        from os import mkdir, remove, rmdir, path
        from processes.consolidate import consolidate_split
        from utility.utility import To_Datetime

        split = self.shift.split
        file_list = split.file_list()

        # create directory
        mkdir(file_list['directory'])

        # create indavidual files
        with open(file_list['start_time'], 'w') as start_time_file:
            start_time_file.write(str(split.start_time))
        with open(file_list['miles_traveled'], 'w') as miles_traveled_file:
            miles_traveled_file.write(str(split.miles_traveled))
        with open(file_list['end_time'], 'w') as end_time_file:
            end_time_file.write(str(split.end_time))

        # check that files were created and others dont exist
        self.assertTrue(path.exists(file_list['start_time']))
        self.assertTrue(path.exists(file_list['miles_traveled']))
        self.assertTrue(path.exists(file_list['end_time']))
        self.assertFalse(path.exists(file_list['info']))

        # run the function
        consolidate_split(split)

        # check that the files were deleted and created
        self.assertFalse(path.exists(file_list['start_time']))
        self.assertFalse(path.exists(file_list['miles_traveled']))
        self.assertFalse(path.exists(file_list['end_time']))
        self.assertTrue(path.exists(file_list['info']))

        # check that correct data was written to files
        with open(file_list['info'], 'r') as info_file:
            data = info_file.readline().split(',')
            self.assertEqual(float(data[0]), split.miles_traveled)
            self.assertEqual(
                To_Datetime(data[1]).from_datetime(), split.start_time)
            self.assertEqual(
                To_Datetime(data[2]).from_datetime(), split.end_time)

        # delete files and directories
        remove(file_list['info'])

    def test_consolidate_extra_stop_shift(self):
        from objects import Extra_Stop
        from os import mkdir, remove, rmdir, path
        from processes.consolidate import consolidate_extra_stop
        from utility.utility import To_Datetime

        extra_stop = self.shift.extra_stops[0]

        file_list = extra_stop.file_list()

        # create directory
        mkdir(file_list['directory'])

        # create indavidual files
        with open(file_list['start_time'], 'w') as start_time_file:
            start_time_file.write(str(extra_stop.start_time))
        with open(file_list['location'], 'w') as location_file:
            location_file.write(extra_stop.location)
        with open(file_list['reason'], 'w') as reason_file:
            reason_file.write(extra_stop.reason)
        with open(file_list['miles_traveled'], 'w') as miles_traveled_file:
            miles_traveled_file.write(str(extra_stop.miles_traveled))
        with open(file_list['end_time'], 'w') as end_time_file:
            end_time_file.write(str(extra_stop.end_time))

        # check that files were created and others dont exist
        self.assertTrue(path.exists(file_list['start_time']))
        self.assertTrue(path.exists(file_list['location']))
        self.assertTrue(path.exists(file_list['reason']))
        self.assertTrue(path.exists(file_list['miles_traveled']))
        self.assertTrue(path.exists(file_list['end_time']))
        self.assertFalse(path.exists(file_list['info']))
        self.assertFalse(path.exists(file_list['completed_ids']))

        # run the function
        consolidate_extra_stop(extra_stop)

        # check that the files were deleted and created
        self.assertFalse(path.exists(file_list['location']))
        self.assertFalse(path.exists(file_list['reason']))
        self.assertFalse(path.exists(file_list['miles_traveled']))
        self.assertFalse(path.exists(file_list['start_time']))
        self.assertFalse(path.exists(file_list['end_time']))
        self.assertTrue(path.exists(file_list['info']))
        self.assertTrue(path.exists(file_list['completed_ids']))

        # check that correct data was written to files
        with open(file_list['info'], 'r') as info_file:
            data = info_file.read().split('\n')
            self.assertEqual(data[0], extra_stop.location)
            self.assertEqual(data[1], extra_stop.reason)
            self.assertEqual(float(data[2]), extra_stop.miles_traveled)
            self.assertEqual(
                To_Datetime(data[3]).from_datetime(), extra_stop.start_time)
            self.assertEqual(
                To_Datetime(data[4]).from_datetime(), extra_stop.end_time)
        with open(file_list['completed_ids'], 'r') as completed_ids_file:
            self.assertEqual(int(completed_ids_file.readline()), extra_stop.id)

        # delete files and directories
        remove(file_list['info'])
        remove(file_list['completed_ids'])
        remove(file_list['running_id'])

    def test_consolidate_extra_stop_delivery(self):
        from objects import Extra_Stop
        from os import mkdir, remove, rmdir, path
        from processes.consolidate import consolidate_extra_stop
        from utility.utility import To_Datetime

        delivery = self.shift.deliveries[1]
        extra_stop = delivery.extra_stops[0]
        file_list = extra_stop.file_list()

        # create directory
        mkdir(delivery.file_list()['directory'])
        mkdir(file_list['directory'])

        # create indavidual files
        with open(file_list['location'], 'w') as location_file:
            location_file.write(extra_stop.location)
        with open(file_list['reason'], 'w') as reason_file:
            reason_file.write(extra_stop.reason)
        with open(file_list['miles_traveled'], 'w') as miles_traveled_file:
            miles_traveled_file.write(str(extra_stop.miles_traveled))
        with open(file_list['end_time'], 'w') as end_time_file:
            end_time_file.write(str(extra_stop.end_time))

        # check that files were created and others dont exist
        self.assertTrue(path.exists(file_list['location']))
        self.assertTrue(path.exists(file_list['reason']))
        self.assertTrue(path.exists(file_list['miles_traveled']))
        self.assertTrue(path.exists(file_list['end_time']))
        self.assertFalse(path.exists(file_list['info']))
        self.assertFalse(path.exists(file_list['completed_ids']))

        # run the function
        consolidate_extra_stop(extra_stop)

        # check that the files were deleted and created
        self.assertFalse(path.exists(file_list['location']))
        self.assertFalse(path.exists(file_list['reason']))
        self.assertFalse(path.exists(file_list['miles_traveled']))
        self.assertFalse(path.exists(file_list['end_time']))
        self.assertTrue(path.exists(file_list['info']))
        self.assertTrue(path.exists(file_list['completed_ids']))

        # check that correct data was written to files
        with open(file_list['info'], 'r') as info_file:
            data = info_file.read().split('\n')
            self.assertEqual(data[0], extra_stop.location)
            self.assertEqual(data[1], extra_stop.reason)
            self.assertEqual(float(data[2]), extra_stop.miles_traveled)
            self.assertEqual(
                To_Datetime(data[3]).from_datetime(), extra_stop.end_time)
        with open(file_list['completed_ids'], 'r') as completed_ids_file:
            self.assertEqual(int(completed_ids_file.readline()), extra_stop.id)

        # delete files and directories
        remove(file_list['info'])
        remove(file_list['completed_ids'])
        remove(file_list['running_id'])
        rmdir(delivery.file_list()['directory'])


# load
class TestLoad(unittest.TestCase):
    def setUp(self):
        from resources.system_names import\
            data_directory, shifts_directory
        from os import mkdir, path

        self.shift = completed_shift()
        mkdir(data_directory)
        mkdir(path.join(data_directory, shifts_directory))
        mkdir(self.shift.file_list()['directory'])

    def tearDown(self):
        from resources.system_names import\
            data_directory, shifts_directory
        from os import rmdir, path

        rmdir(self.shift.file_list()['directory'])
        rmdir(path.join(data_directory, shifts_directory))
        rmdir(data_directory)

    # shift
    def test_load_shift_completed(self):
        from objects import Shift
        from os import path, remove
        from processes.load import load_shift
        from utility.utility import now

        shift = Shift(now().date())
        file_list = self.shift.file_list()

        # create file
        with open(file_list['info'], 'w') as shift_file:
            shift_file.write(self.shift.csv())

        # check file was created and baseline
        self.assertTrue(path.exists(file_list['info']))
        self.assertNotEqual(shift.miles_traveled, self.shift.miles_traveled)
        self.assertNotEqual(shift.fuel_economy, self.shift.fuel_economy)
        self.assertNotEqual(shift.vehicle_compensation, self.shift.vehicle_compensation)
        self.assertNotEqual(shift.device_compensation, self.shift.device_compensation)
        self.assertNotEqual(shift.extra_tips_claimed, self.shift.extra_tips_claimed)
        self.assertNotEqual(shift.total_hours, self.shift.total_hours)
        self.assertNotEqual(shift.start_time, self.shift.start_time)
        self.assertNotEqual(shift.end_time, self.shift.end_time)

        # run function
        shift = load_shift(shift)

        # check that data was loaded correctly
        self.assertEqual(shift.miles_traveled, self.shift.miles_traveled)
        self.assertEqual(shift.fuel_economy, self.shift.fuel_economy)
        self.assertEqual(shift.vehicle_compensation, self.shift.vehicle_compensation)
        self.assertEqual(shift.device_compensation, self.shift.device_compensation)
        self.assertEqual(shift.extra_tips_claimed, self.shift.extra_tips_claimed)
        self.assertEqual(shift.total_hours, self.shift.total_hours)
        self.assertEqual(shift.start_time, self.shift.start_time)
        self.assertEqual(shift.end_time, self.shift.end_time)

        # delete file
        remove(file_list['info'])

    def test_load_shift_current(self):
        from objects import Shift
        from os import path, remove
        from processes.load import load_shift
        from utility.utility import now

        shift = Shift(now().date())
        file_list = self.shift.file_list()

        # create files
        with open(file_list['start_time'], 'w') as start_time_file:
            start_time_file.write(str(self.shift.start_time))
        with open(file_list['end_time'], 'w') as end_time_file:
            end_time_file.write(str(self.shift.end_time))
        with open(file_list['miles_traveled'], 'w') as miles_traveled_file:
            miles_traveled_file.write(str(self.shift.miles_traveled))
        with open(file_list['fuel_economy'], 'w') as fuel_economy_file:
            fuel_economy_file.write(str(self.shift.fuel_economy))
        with open(file_list['vehicle_compensation'], 'w') as vehicle_compensation_file:
            vehicle_compensation_file.write(str(self.shift.vehicle_compensation))
        with open(file_list['device_compensation'], 'w') as device_compensation_file:
            device_compensation_file.write(str(self.shift.device_compensation))
        with open(file_list['total_hours'], 'w') as total_hours_file:
            total_hours_file.write(str(self.shift.total_hours))
        with open(file_list['extra_tips_claimed'], 'w') as extra_tips_claimed_file:
            extra_tips_claimed_file.write(str(self.shift.extra_tips_claimed))

        # check files were created and baseline
        self.assertTrue(path.exists(file_list['start_time']))
        self.assertTrue(path.exists(file_list['end_time']))
        self.assertTrue(path.exists(file_list['miles_traveled']))
        self.assertTrue(path.exists(file_list['fuel_economy']))
        self.assertTrue(path.exists(file_list['vehicle_compensation']))
        self.assertTrue(path.exists(file_list['device_compensation']))
        self.assertTrue(path.exists(file_list['total_hours']))
        self.assertTrue(path.exists(file_list['extra_tips_claimed']))
        self.assertNotEqual(shift.start_time, self.shift.start_time)
        self.assertNotEqual(shift.end_time, self.shift.end_time)
        self.assertNotEqual(shift.miles_traveled, self.shift.miles_traveled)
        self.assertNotEqual(shift.fuel_economy, self.shift.fuel_economy)
        self.assertNotEqual(shift.vehicle_compensation, self.shift.vehicle_compensation)
        self.assertNotEqual(shift.device_compensation, self.shift.device_compensation)
        self.assertNotEqual(shift.total_hours, self.shift.total_hours)
        self.assertNotEqual(shift.extra_tips_claimed, self.shift.extra_tips_claimed)

        # run function
        shift = load_shift(shift, current=True)

        # check that data was loaded correctly
        self.assertEqual(shift.start_time, self.shift.start_time)
        self.assertEqual(shift.end_time, self.shift.end_time)
        self.assertEqual(shift.miles_traveled, self.shift.miles_traveled)
        self.assertEqual(shift.fuel_economy, self.shift.fuel_economy)
        self.assertEqual(shift.vehicle_compensation, self.shift.vehicle_compensation)
        self.assertEqual(shift.device_compensation, self.shift.device_compensation)
        self.assertEqual(shift.total_hours, self.shift.total_hours)
        self.assertEqual(shift.extra_tips_claimed, self.shift.extra_tips_claimed)

        # delete files
        remove(file_list['start_time'])
        remove(file_list['end_time'])
        remove(file_list['miles_traveled'])
        remove(file_list['fuel_economy'])
        remove(file_list['vehicle_compensation'])
        remove(file_list['device_compensation'])
        remove(file_list['total_hours'])
        remove(file_list['extra_tips_claimed'])

    def test_load_carry_out_tips(self):
        from objects import Shift
        from os import path, remove
        from processes.load import load_carry_out_tips
        from utility.utility import now

        shift = Shift(now().date())
        file_list = self.shift.file_list()

        # create file
        with open(file_list['tips'], 'w') as carry_out_tips_file:
            carry_out_tips_file.write(
                '3.11,0.0,0.0\n'\
                '0.0,2.71,0.0')

        # check file exists and baseline
        self.assertTrue(path.exists(file_list['tips']))
        self.assertTrue(len(shift.carry_out_tips) == 0)

        # run function
        shift = load_carry_out_tips(shift)

        # check data was loaded correctly
        self.assertTrue(len(shift.carry_out_tips) > 0)
        self.assertEqual(
            shift.carry_out_tips[0].total_amount(),
            self.shift.carry_out_tips[0].total_amount())
        self.assertEqual(
            shift.carry_out_tips[1].total_amount(),
            self.shift.carry_out_tips[1].total_amount())
        self.assertEqual(
            shift.carry_out_tips[0].csv(), self.shift.carry_out_tips[0].csv())
        self.assertEqual(
            shift.carry_out_tips[1].csv(), self.shift.carry_out_tips[1].csv())

        # delete files
        remove(file_list['tips'])

    # delivery
    def test_load_delivery_completed(self):
        from objects import Delivery
        from os import mkdir, remove, rmdir, path
        from processes.load import load_delivery

        delivery = Delivery(self.shift)
        file_list = delivery.file_list()

        # create all file and directory
        mkdir(file_list['directory'])
        with open(file_list['info'], 'w') as info_file:
            info_file.write(self.shift.deliveries[0].csv())
        
        # check file was created and baseline
        self.assertTrue(path.exists(file_list['info']))
        self.assertNotEqual(
            delivery.miles_traveled, self.shift.deliveries[0].miles_traveled)
        self.assertNotEqual(
            delivery.average_speed, self.shift.deliveries[0].average_speed)
        self.assertNotEqual(
            delivery.start_time, self.shift.deliveries[0].start_time)
        self.assertNotEqual(
            delivery.end_time, self.shift.deliveries[0].end_time)

        # run function
        load_delivery(delivery)

        # check that data was loaded correctly
        self.assertEqual(delivery.miles_traveled, self.shift.deliveries[0].miles_traveled)
        self.assertEqual(delivery.average_speed, self.shift.deliveries[0].average_speed)
        self.assertEqual(delivery.start_time, self.shift.deliveries[0].start_time)
        self.assertEqual(delivery.end_time, self.shift.deliveries[0].end_time)

        # delete file and directory
        remove(file_list['info'])
        rmdir(file_list['directory'])

    def test_load_delivery_current(self):
        from objects import Delivery
        from os import mkdir, remove, rmdir, path
        from processes.load import load_delivery

        delivery = Delivery(self.shift)
        file_list = delivery.file_list()

        # create all file and directory
        mkdir(file_list['directory'])
        with open(file_list['miles_traveled'], 'w') as info_file:
            info_file.write(str(self.shift.deliveries[0].miles_traveled))
        with open(file_list['average_speed'], 'w') as info_file:
            info_file.write(str(self.shift.deliveries[0].average_speed))
        with open(file_list['start_time'], 'w') as info_file:
            info_file.write(str(self.shift.deliveries[0].start_time))
        with open(file_list['end_time'], 'w') as info_file:
            info_file.write(str(self.shift.deliveries[0].end_time))
        
        # check file was created and baseline
        self.assertTrue(path.exists(file_list['miles_traveled']))
        self.assertTrue(path.exists(file_list['average_speed']))
        self.assertTrue(path.exists(file_list['start_time']))
        self.assertTrue(path.exists(file_list['end_time']))
        self.assertNotEqual(
            delivery.miles_traveled, self.shift.deliveries[0].miles_traveled)
        self.assertNotEqual(
            delivery.average_speed, self.shift.deliveries[0].average_speed)
        self.assertNotEqual(
            delivery.start_time, self.shift.deliveries[0].start_time)
        self.assertNotEqual(
            delivery.end_time, self.shift.deliveries[0].end_time)

        # run function
        load_delivery(delivery, current=True)

        # check that data was loaded correctly
        self.assertEqual(delivery.miles_traveled, self.shift.deliveries[0].miles_traveled)
        self.assertEqual(delivery.average_speed, self.shift.deliveries[0].average_speed)
        self.assertEqual(delivery.start_time, self.shift.deliveries[0].start_time)
        self.assertEqual(delivery.end_time, self.shift.deliveries[0].end_time)

        # delete file and directory
        remove(file_list['miles_traveled'])
        remove(file_list['average_speed'])
        remove(file_list['start_time'])
        remove(file_list['end_time'])
        rmdir(file_list['directory'])

    # order
    def test_load_order_completed(self):
        from objects import Order
        from os import mkdir, remove, rmdir, path
        from processes.load import load_order

        order = Order(self.shift.deliveries[0])
        file_list = order.file_list()

        # create file and directory
        mkdir(self.shift.deliveries[0].file_list()['directory'])
        with open(file_list['info'], 'w') as info_file:
            info_file.write(self.shift.deliveries[0].orders[0].csv())

        # check that file was created and baseline
        self.assertTrue(path.exists(file_list['info']))
        self.assertIsNot(order.tip, self.shift.deliveries[0].orders[0].tip)
        self.assertNotEqual(
            order.miles_traveled,
            self.shift.deliveries[0].orders[0].miles_traveled)
        self.assertNotEqual(
            order.end_time, self.shift.deliveries[0].orders[0].end_time)

        # run function
        order = load_order(order)

        # check that data was loaded correctly
        self.assertEqual(
            order.tip.csv(), self.shift.deliveries[0].orders[0].tip.csv())
        self.assertEqual(
            order.miles_traveled,
            self.shift.deliveries[0].orders[0].miles_traveled)
        self.assertEqual(
            order.end_time, self.shift.deliveries[0].orders[0].end_time)

        # delete file and directory
        remove(file_list['info'])
        rmdir(self.shift.deliveries[0].file_list()['directory'])

    def test_load_order_current(self):
        from objects import Order
        from os import mkdir, remove, rmdir, path
        from processes.load import load_order

        order = Order(self.shift.deliveries[0])
        file_list = order.file_list()

        # create file and directory
        mkdir(self.shift.deliveries[0].file_list()['directory'])
        mkdir(file_list['directory'])
        with open(file_list['tip'], 'w') as info_file:
            info_file.write(str(self.shift.deliveries[0].orders[0].tip.csv()))
        with open(file_list['miles_traveled'], 'w') as info_file:
            info_file.write(str(self.shift.deliveries[0].orders[0].miles_traveled))
        with open(file_list['end_time'], 'w') as info_file:
            info_file.write(str(self.shift.deliveries[0].orders[0].end_time))

        # check that file was created and baseline
        self.assertTrue(path.exists(file_list['tip']))
        self.assertTrue(path.exists(file_list['miles_traveled']))
        self.assertTrue(path.exists(file_list['end_time']))
        self.assertIsNot(order.tip, self.shift.deliveries[0].orders[0].tip)
        self.assertNotEqual(
            order.miles_traveled,
            self.shift.deliveries[0].orders[0].miles_traveled)
        self.assertNotEqual(
            order.end_time, self.shift.deliveries[0].orders[0].end_time)

        # run function
        order = load_order(order, current=True)

        # check that data was loaded correctly
        self.assertEqual(
            order.tip.csv(), self.shift.deliveries[0].orders[0].tip.csv())
        self.assertEqual(
            order.miles_traveled,
            self.shift.deliveries[0].orders[0].miles_traveled)
        self.assertEqual(
            order.end_time, self.shift.deliveries[0].orders[0].end_time)

        # delete file and directory
        remove(file_list['tip'])
        remove(file_list['miles_traveled'])
        remove(file_list['end_time'])
        rmdir(file_list['directory'])
        rmdir(self.shift.deliveries[0].file_list()['directory'])

    # split
    def test_load_split_completed(self):
        from objects import Split
        from os import remove, path
        from processes.load import load_split

        split = Split(self.shift)
        file_list = split.file_list()

        # create file
        with open(file_list['info'], 'w') as info_file:
            info_file.write(self.shift.split.csv())

        # check file was created and baseline
        self.assertTrue(path.exists(file_list['info']))
        self.assertNotEqual(split.miles_traveled, self.shift.split.miles_traveled)
        self.assertNotEqual(split.start_time, self.shift.split.start_time)
        self.assertNotEqual(split.end_time, self.shift.split.end_time)

        # run function
        split = load_split(split)

        # check that data was loaded correctly
        self.assertEqual(split.miles_traveled, self.shift.split.miles_traveled)
        self.assertEqual(split.start_time, self.shift.split.start_time)
        self.assertEqual(split.end_time, self.shift.split.end_time)

        # delete files and directories
        remove(file_list['info'])

    def test_load_split_currrent(self):
        from objects import Split
        from os import mkdir, remove, rmdir, path
        from processes.load import load_split

        split = Split(self.shift)
        file_list = split.file_list()

        # create file
        mkdir(file_list['directory'])
        with open(file_list['miles_traveled'], 'w') as info_file:
            info_file.write(str(self.shift.split.miles_traveled))
        with open(file_list['start_time'], 'w') as info_file:
            info_file.write(str(self.shift.split.start_time))
        with open(file_list['end_time'], 'w') as info_file:
            info_file.write(str(self.shift.split.end_time))

        # check file was created and baseline
        self.assertTrue(path.exists(file_list['miles_traveled']))
        self.assertTrue(path.exists(file_list['start_time']))
        self.assertTrue(path.exists(file_list['end_time']))
        self.assertNotEqual(split.miles_traveled, self.shift.split.miles_traveled)
        self.assertNotEqual(split.start_time, self.shift.split.start_time)
        self.assertNotEqual(split.end_time, self.shift.split.end_time)

        # run function
        split = load_split(split, current=True)

        # check that data was loaded correctly
        self.assertEqual(split.miles_traveled, self.shift.split.miles_traveled)
        self.assertEqual(split.start_time, self.shift.split.start_time)
        self.assertEqual(split.end_time, self.shift.split.end_time)

        # delete files and directories
        remove(file_list['miles_traveled'])
        remove(file_list['start_time'])
        remove(file_list['end_time'])
        rmdir(file_list['directory'])

    # extra stop
    def test_load_extra_stop_shift_completed(self):
        from objects import Extra_Stop
        from os import remove, path
        from processes.load import load_extra_stop

        extra_stop = Extra_Stop(self.shift)
        file_list = extra_stop.file_list()

        # create file
        with open(file_list['info'], 'w') as info_file:
            info_file.write(self.shift.extra_stops[0].nlsv())

        # check that file was created and baseline
        self.assertTrue(path.exists(file_list['info']))
        self.assertNotEqual(
            extra_stop.location, self.shift.extra_stops[0].location)
        self.assertNotEqual(extra_stop.reason, self.shift.extra_stops[0].reason)
        self.assertNotEqual(
            extra_stop.miles_traveled, self.shift.extra_stops[0].miles_traveled)
        self.assertNotEqual(
            extra_stop.start_time, self.shift.extra_stops[0].start_time)
        self.assertNotEqual(
            extra_stop.end_time, self.shift.extra_stops[0].end_time)

        # run function
        extra_stop = load_extra_stop(extra_stop)

        # check that data was loaded correctly
        self.assertEqual(
            extra_stop.location, self.shift.extra_stops[0].location)
        self.assertEqual(extra_stop.reason, self.shift.extra_stops[0].reason)
        self.assertEqual(
            extra_stop.miles_traveled, self.shift.extra_stops[0].miles_traveled)
        self.assertEqual(
            extra_stop.start_time, self.shift.extra_stops[0].start_time)
        self.assertEqual(
            extra_stop.end_time, self.shift.extra_stops[0].end_time)

        # delete file
        remove(file_list['info'])
    
    def test_load_extra_stop_shift_current(self):
        from objects import Extra_Stop
        from os import mkdir, path, remove, rmdir
        from processes.load import load_extra_stop

        extra_stop = Extra_Stop(self.shift)
        file_list = extra_stop.file_list()

        # create file
        mkdir(file_list['directory'])
        with open(file_list['location'], 'w') as location_file:
            location_file.write(self.shift.extra_stops[0].location)
        with open(file_list['reason'], 'w') as reason_file:
            reason_file.write(self.shift.extra_stops[0].reason)
        with open(file_list['miles_traveled'], 'w') as miles_traveled_file:
            miles_traveled_file.write(str(self.shift.extra_stops[0].miles_traveled))
        with open(file_list['start_time'], 'w') as start_time_file:
            start_time_file.write(str(self.shift.extra_stops[0].start_time))
        with open(file_list['end_time'], 'w') as end_time_file:
            end_time_file.write(str(self.shift.extra_stops[0].end_time))

        # check that file was created and baseline
        self.assertTrue(path.exists(file_list['location']))
        self.assertTrue(path.exists(file_list['reason']))
        self.assertTrue(path.exists(file_list['miles_traveled']))
        self.assertTrue(path.exists(file_list['start_time']))
        self.assertTrue(path.exists(file_list['end_time']))
        self.assertNotEqual(
            extra_stop.location, self.shift.extra_stops[0].location)
        self.assertNotEqual(extra_stop.reason, self.shift.extra_stops[0].reason)
        self.assertNotEqual(
            extra_stop.miles_traveled, self.shift.extra_stops[0].miles_traveled)
        self.assertNotEqual(
            extra_stop.start_time, self.shift.extra_stops[0].start_time)
        self.assertNotEqual(
            extra_stop.end_time, self.shift.extra_stops[0].end_time)

        # run function
        extra_stop = load_extra_stop(extra_stop, current=True)

        # check that data was loaded correctly
        self.assertEqual(
            extra_stop.location, self.shift.extra_stops[0].location)
        self.assertEqual(extra_stop.reason, self.shift.extra_stops[0].reason)
        self.assertEqual(
            extra_stop.miles_traveled, self.shift.extra_stops[0].miles_traveled)
        self.assertEqual(
            extra_stop.start_time, self.shift.extra_stops[0].start_time)
        self.assertEqual(
            extra_stop.end_time, self.shift.extra_stops[0].end_time)

        # delete file
        remove(file_list['location'])
        remove(file_list['reason'])
        remove(file_list['miles_traveled'])
        remove(file_list['start_time'])
        remove(file_list['end_time'])
        rmdir(file_list['directory'])
    
    def test_load_extra_stop_delivery_completed(self):
        from objects import Extra_Stop
        from os import mkdir, path, rmdir, remove
        from processes.load import load_extra_stop

        delivery = self.shift.deliveries[1]
        extra_stop = Extra_Stop(delivery)
        file_list = extra_stop.file_list()

        # create file and directory
        mkdir(delivery.file_list()['directory'])
        with open(file_list['info'], 'w') as info_file:
            info_file.write(delivery.extra_stops[0].nlsv())

        # check that file was created and baseline
        self.assertTrue(path.exists(file_list['info']))
        self.assertNotEqual(
            extra_stop.location, delivery.extra_stops[0].location)
        self.assertNotEqual(extra_stop.reason, delivery.extra_stops[0].reason)
        self.assertNotEqual(
            extra_stop.miles_traveled, delivery.extra_stops[0].miles_traveled)
        self.assertNotEqual(
            extra_stop.end_time, delivery.extra_stops[0].end_time)

        # run function
        extra_stop = load_extra_stop(extra_stop)

        # check that data was loaded correctly
        self.assertEqual(
            extra_stop.location, delivery.extra_stops[0].location)
        self.assertEqual(extra_stop.reason, delivery.extra_stops[0].reason)
        self.assertEqual(
            extra_stop.miles_traveled, delivery.extra_stops[0].miles_traveled)
        self.assertEqual(
            extra_stop.end_time, delivery.extra_stops[0].end_time)

        # delete file
        remove(file_list['info'])
        rmdir(delivery.file_list()['directory'])
    
    def test_load_extra_stop_delivery_currernt(self):
        from objects import Extra_Stop
        from os import mkdir, path, remove, rmdir
        from processes.load import load_extra_stop

        extra_stop = Extra_Stop(self.shift)
        file_list = extra_stop.file_list()

        # create file
        mkdir(file_list['directory'])
        with open(file_list['location'], 'w') as location_file:
            location_file.write(self.shift.extra_stops[0].location)
        with open(file_list['reason'], 'w') as reason_file:
            reason_file.write(self.shift.extra_stops[0].reason)
        with open(file_list['miles_traveled'], 'w') as miles_traveled_file:
            miles_traveled_file.write(str(self.shift.extra_stops[0].miles_traveled))
        with open(file_list['end_time'], 'w') as end_time_file:
            end_time_file.write(str(self.shift.extra_stops[0].end_time))

        # check that file was created and baseline
        self.assertTrue(path.exists(file_list['location']))
        self.assertTrue(path.exists(file_list['reason']))
        self.assertTrue(path.exists(file_list['miles_traveled']))
        self.assertTrue(path.exists(file_list['end_time']))
        self.assertNotEqual(
            extra_stop.location, self.shift.extra_stops[0].location)
        self.assertNotEqual(extra_stop.reason, self.shift.extra_stops[0].reason)
        self.assertNotEqual(
            extra_stop.miles_traveled, self.shift.extra_stops[0].miles_traveled)
        self.assertNotEqual(
            extra_stop.end_time, self.shift.extra_stops[0].end_time)

        # run function
        extra_stop = load_extra_stop(extra_stop, current=True)

        # check that data was loaded correctly
        self.assertEqual(
            extra_stop.location, self.shift.extra_stops[0].location)
        self.assertEqual(extra_stop.reason, self.shift.extra_stops[0].reason)
        self.assertEqual(
            extra_stop.miles_traveled, self.shift.extra_stops[0].miles_traveled)
        self.assertEqual(
            extra_stop.end_time, self.shift.extra_stops[0].end_time)

        # delete file
        remove(file_list['location'])
        remove(file_list['reason'])
        remove(file_list['miles_traveled'])
        remove(file_list['end_time'])
        rmdir(file_list['directory'])
