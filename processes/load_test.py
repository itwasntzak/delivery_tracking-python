import unittest
from testing_tools import completed_shift


class Test_Load(unittest.TestCase):
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

