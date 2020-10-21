import unittest
from testing_tools import completed_shift

class Test_View(unittest.TestCase):
    def test_view_shift_main(self):
        from processes.view import View_Shift

        shift = completed_shift()
        test = View_Shift(shift).main()

        carry_out_tips =\
            round(sum([tip.total_amount() for tip in shift.carry_out_tips]), 2)
        total_tips =\
            round(sum([tip.total_amount() for tip in shift.all_tips()]), 2)
        card_tips = round(sum([tip.card for tip in shift.card_tips()]), 2)
        cash_tips = round(sum([tip.cash for tip in shift.cash_tips()]), 2)

        expected =\
            '- Shift -\n'\
            f'\tDate: {shift.id}\n'\
            f'\tStarted at: {shift.start_time.strftime("%I:%M:%S %p")}\n'\
            f'\tEnded at: {shift.end_time.strftime("%I:%M:%S %p")}\n'\
            f'\tTotal miles traveled: {shift.miles_traveled} miles\n'\
            f'\tAverage fuel economy: {shift.fuel_economy} mpg\n'\
            f'\tAmount paid for vehicle usage: ${shift.vehicle_compensation}\n'\
            f'\tCompensation for use of device: ${shift.device_compensation}\n'\
            f'\tWork recorded hours: {shift.total_hours} hours\n'\
            '\tExtra tips reported for taxes: $'\
            + '{:.2f}\n'.format(shift.extra_tips_claimed)\
            + '\tTotal made in carry out tips: ${:.2f}\n'.format(carry_out_tips)\
            + '\tTotal tips: ${:.2f}\n'.format(total_tips)\
            + '\tCard tips: ${:.2f}\n'.format(card_tips)\
            + '\tCash tips: ${:.2f}\n'.format(cash_tips)\
            + f'\tNumber of deliveries: {len(shift.deliveries)}\n'\
            f'\tNumber of extra stops: {len(shift.extra_stops)}\n'

        self.assertEqual(test, expected)

    def test_view_shift_quick(self):
        from processes.view import View_Shift

        shift = completed_shift()
        test = View_Shift(shift).quick()

        carry_out_tips =\
            round(sum([tip.total_amount() for tip in shift.carry_out_tips]), 2)
        total_tips =\
            round(sum([tip.total_amount() for tip in shift.all_tips()]), 2)
        card_tips = round(sum([tip.card for tip in shift.card_tips()]), 2)
        cash_tips = round(sum([tip.cash for tip in shift.cash_tips()]), 2)

        expected =\
            '- Shift -\n'\
            f'\tDate: {shift.id}\n'\
            f'\tStarted at: {shift.start_time.strftime("%I:%M:%S %p")}\n'\
            f'\tNumber of deliveries: {len(shift.deliveries)}\n'\
            f'\tNumber of extra stops: {len(shift.extra_stops)}\n'\
            + '\tTotal made in carry out tips: ${:.2f}\n'.format(carry_out_tips)\
            + '\tTotal tips: ${:.2f}\n'.format(total_tips)\
            + '\tCard tips: ${:.2f}\n'.format(card_tips)\
            + '\tCash tips: ${:.2f}\n'.format(cash_tips)


        self.assertEqual(test, expected)

    def test_view_delivery_main(self):
        from processes.view import View_Delivery

        shift = completed_shift()
        delivery = shift.deliveries[0]
        test = View_Delivery(delivery).main()

        expected =\
            f'Delivery #: {delivery.id + 1}\n'\
            f'\tTotal time on delivery: {delivery.end_time - delivery.start_time}\n'\
            f'\tStarted at: {delivery.start_time.strftime("%I:%M:%S %p")}\n'\
            f'\tCompleted at: {delivery.end_time.strftime("%I:%M:%S %p")}\n'\
            f'\tNumber of orders: {len(delivery.orders)}\n'\
            f'\tOrder I.D. #: {delivery.orders[0].id}\n'\
            f'\tTotal distance traveled for delivery: {delivery.miles_traveled} miles\n'\
            f'\tAverage speed for delivery: {delivery.average_speed} mph\n'
        
        self.assertEqual(test, expected)

    def test_view_delivery_quick(self):
        from processes.view import View_Delivery

        shift = completed_shift()
        delivery = shift.deliveries[0]
        test = View_Delivery(delivery).quick()

        expected =\
            f'Delivery #: {delivery.id + 1}\n'\
            f'\tStarted at: {delivery.start_time.strftime("%I:%M:%S %p")}\n'\
            f'\tNumber of orders: {len(delivery.orders)}\n'\
        
        self.assertEqual(test, expected)

    def test_view_order_main(self):
        from datetime import datetime
        from objects import Shift, Delivery, Order, Tip
        from processes.view import view_order
        from utility.utility import now, To_Datetime

        # no data entered
        order = Order(Delivery(Shift(now().date())), 123)
        test = view_order(order)
        expected = 'Order I.D. #: 123\n'\
                   '\tTotal tip: $0.00\n'
        self.assertEqual(test, expected)
        # card
        order.tip = Tip(3.97)
        test = view_order(order)
        expected = 'Order I.D. #: 123\n'\
                   '\tCard tip: $3.97\n'
        self.assertEqual(test, expected)
        # cash
        order.tip = Tip(cash=3.97)
        test = view_order(order)
        expected = 'Order I.D. #: 123\n'\
                   '\tCash tip: $3.97\n'
        self.assertEqual(test, expected)
        # card and cash
        order.tip = Tip(3, 2)
        test = view_order(order)
        expected = 'Order I.D. #: 123\n'\
                   '\tTotal tip: $5.00\n'\
                   '\tCard tip: $3.00\n'\
                   '\tCash tip: $2.00\n'
        self.assertEqual(test, expected)
        # unknown
        order.tip = Tip(unknown=3.97)
        test = view_order(order)
        expected = 'Order I.D. #: 123\n'\
                   '\tUnknown tip: $3.97\n'
        self.assertEqual(test, expected)
        # distance
        order.miles_traveled = 3.9
        test = view_order(order)
        expected = 'Order I.D. #: 123\n'\
                   '\tUnknown tip: $3.97\n'\
                   '\tDistance to address: 3.9 miles\n'
        self.assertEqual(test, expected)
        # end time
        order.end_time = datetime.strptime('15:27:42', '%H:%M:%S')
        test = view_order(order)
        expected = 'Order I.D. #: 123\n'\
                   '\tUnknown tip: $3.97\n'\
                   '\tDistance to address: 3.9 miles\n'\
                   '\tCompleted at: 03:27:42 PM\n'
        self.assertEqual(test, expected)

    def test_view_tip(self):
        from objects import Tip
        from processes.view import view_tip

        # card and cash
        tip = Tip(3.0, 2.0)
        test = view_tip(tip)
        expected = '\nTotal tip: $5.00\nCard tip: $3.00\nCash tip: $2.00\n'
        self.assertEqual(test, expected)
        # card
        tip = Tip(3.0)
        test = view_tip(tip)
        expected = '\nCard tip: $3.00\n'
        self.assertEqual(test, expected)
        # cash
        tip = Tip(cash=3.0)
        test = view_tip(tip)
        expected = '\nCash tip: $3.00\n'
        self.assertEqual(test, expected)
        # unknown
        tip = Tip(unknown=3.0)
        test = view_tip(tip)
        expected = '\nUnknown tip: $3.00\n'
        self.assertEqual(test, expected)
        # no tip
        tip = Tip()
        test = view_tip(tip)
        expected = '\nTotal tip: $0.00\n'
        self.assertEqual(test, expected)

    def test_view_split(self):
        from processes.view import view_split

        shift = completed_shift()
        split = shift.split
        test = view_split(split)

        expected =\
            '- Split -\n'\
            f'\tStarted at: {split.start_time.strftime("%I:%M:%S %p")}\n'\
            f'\tEnded at: {split.end_time.strftime("%I:%M:%S %p")}\n'\
            f'\tMiles traveled: {split.miles_traveled} miles\n'

        self.assertEqual(test, expected)

    def test_view_extra_stop_shift(self):
        from processes.view import view_extra_stop

        shift = completed_shift()
        extra_stop = shift.extra_stops[0]
        test = view_extra_stop(extra_stop)

        expected =\
            f'Extra stop id #: {extra_stop.id + 1}\n'\
            f'\t{extra_stop.start_time.strftime("%I:%M:%S %p")}\n'\
            f'\tExtra stop was completed at: {extra_stop.end_time.strftime("%I:%M:%S %p")}\n'\
            f'\tLocation: {extra_stop.location.capitalize()}\n'\
            f'\tReason: {extra_stop.reason.capitalize()}\n'\
            f'\tDistance to extra stop: {extra_stop.miles_traveled} miles\n'
        
        self.assertEqual(test, expected)

    def test_view_extra_stop_delivery(self):
        from processes.view import view_extra_stop

        shift = completed_shift()
        extra_stop = shift.deliveries[1].extra_stops[0]
        test = view_extra_stop(extra_stop)

        expected =\
            f'Extra stop id #: {extra_stop.id + 1}\n'\
            f'\tExtra stop was completed at: {extra_stop.end_time.strftime("%I:%M:%S %p")}\n'\
            f'\tLocation: {extra_stop.location.capitalize()}\n'\
            f'\tReason: {extra_stop.reason.capitalize()}\n'\
            f'\tDistance to extra stop: {extra_stop.miles_traveled} miles\n'
        
        self.assertEqual(test, expected)
