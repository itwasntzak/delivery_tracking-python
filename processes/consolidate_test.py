import unittest
from testing_tools import completed_shift

class Test_Consolidate(unittest.TestCase):
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
