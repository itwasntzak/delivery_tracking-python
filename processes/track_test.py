import unittest
from unittest.mock import patch
from testing_tools import completed_shift

class Test_Track(unittest.TestCase):
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
        end_shift(self.shift, test=True)

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
        start_shift(self.shift, test=True)

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
        end_delivery(delivery, test=True)

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
        start_delivery(delivery, test=True)

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
        track_order(order, test=True)

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
        end_split(split, test=True)

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
        start_split(split, test=True)

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
        track_extra_stop(extra_stop, test=True)

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
        track_extra_stop(extra_stop, test=True)

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
