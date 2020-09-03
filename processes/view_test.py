import unittest
from testing_tools import completed_shift

class Test_View(unittest.TestCase):
    def test_view_shift(self):
        from processes.view import view_shift

        shift = completed_shift()

        expected =\
            f'Shift date:\t{shift.id}\n'\
            f'Shift was started at:\t{shift.start_time.strftime("%I:%M:%S %p")}\n'\
            f'Shift was ended at:\t{shift.end_time.strftime("%I:%M:%S %p")}\n'\
            f'Number of deliveries:\t{len(shift.deliveries)}\n'\
            f'Number of extra stops:\t{len(shift.extra_stops)}\n'\
             'Total made in carry out tips:\t'\
            f'${sum([tip.total_amount() for tip in shift.carry_out_tips])}\n'\
            f'Work recorded hours:\t{shift.total_hours} hours\n'\
            f'Total distance traveled:\t{shift.miles_traveled} miles\n'\
            f'Average fuel economy:\t{shift.fuel_economy} mpg\n'\
            f'Amount paid for vehicle usage:\t${shift.vehicle_compensation}\n'\
            f'Compensation for use of device\t${shift.device_compensation}\n'\
            f'Extra tips reported for taxes:\t${shift.extra_tips_claimed}\n'

        self.assertEqual(expected, view_shift(shift))

        # print(view_shift(shift))

    def test_view_delivery(self):
        from processes.view import view_delivery

        shift = completed_shift()
        delivery = shift.deliveries[1]

        expected =\
            f'Delivery #:\t{delivery.id + 1}\n'\
            f'Total time on delivery:\t{delivery.end_time - delivery.start_time}\n'\
            f'Started at:\t{delivery.start_time.strftime("%I:%M:%S %p")}\n'\
            f'Completed at:\t{delivery.end_time.strftime("%I:%M:%S %p")}\n'\
            f'Number of orders:\t{len(delivery.orders)}\n'\
            f'Number of extra stops:\t{len(delivery.extra_stops)}\n'\
            f'Order I.D. #:\t{delivery.orders[0].id}\n'\
            f'Total distance traveled for delivery:\t{delivery.miles_traveled} miles\n'\
            f'Average speed for delivery:\t{delivery.average_speed} mph\n'
        
        self.assertEqual(view_delivery(delivery), expected)

        # print(view_delivery(delivery))
    
    def test_view_order(self):
        from processes.view import view_order

        shift = completed_shift()
        order = shift.deliveries[1].orders[0]

        expected =\
            f'Order I.D. #:\t{order.id}\n'\
            f'Completed at:\t{order.end_time.strftime("%I:%M:%S %p")}\n'\
            f'Distance to address:\t{order.miles_traveled} miles\n'
        
        self.assertEqual(view_order(order), expected)

        # print(view_order(order))

    def test_view_split(self):
        from processes.view import view_split

        shift = completed_shift()
        split = shift.split

        expected =\
            f'Split was started at:\t{split.start_time.strftime("%I:%M:%S %p")}\n'\
            f'Split was ended at:\t{split.end_time.strftime("%I:%M:%S %p")}\n'\
            f'Miles traveled on split:\t{split.miles_traveled} miles\n'

        self.assertEqual(view_split(split), expected)

        # print(view_split(split))

    def test_view_extra_stop_shift(self):
        from processes.view import view_extra_stop

        shift = completed_shift()
        extra_stop = shift.extra_stops[0]

        expected =\
            f'Extra stop id #:\t{extra_stop.id + 1}\n'\
            f'{extra_stop.start_time.strftime("%I:%M:%S %p")}\n'\
            f'Extra stop was completed at:\t{extra_stop.end_time.strftime("%I:%M:%S %p")}\n'\
            f'Location:\t{extra_stop.location.capitalize()}\n'\
            f'Reason:\t{extra_stop.reason.capitalize()}\n'\
            f'Distance to extra stop:\t{extra_stop.miles_traveled} miles\n'
        
        self.assertEqual(view_extra_stop(extra_stop), expected)

        # print(view_extra_stop(extra_stop))

    def test_view_extra_stop_delivery(self):
        from processes.view import view_extra_stop

        shift = completed_shift()
        extra_stop = shift.deliveries[1].extra_stops[0]

        expected =\
            f'Extra stop id #:\t{extra_stop.id + 1}\n'\
            f'Extra stop was completed at:\t{extra_stop.end_time.strftime("%I:%M:%S %p")}\n'\
            f'Location:\t{extra_stop.location.capitalize()}\n'\
            f'Reason:\t{extra_stop.reason.capitalize()}\n'\
            f'Distance to extra stop:\t{extra_stop.miles_traveled} miles\n'
        
        self.assertEqual(view_extra_stop(extra_stop), expected)

        # print(view_extra_stop(extra_stop))
        