from objects import Shift
from processes import view
from utility.file import Read
from utility.utility import now, To_Datetime

shifts_ids = Read(Shift(now().date()).file_list()['completed_ids']).comma()
shifts_ids = [To_Datetime(id).from_date() for id in shifts_ids]

shifts = [Shift(id.date()).load_completed() for id in shifts_ids]

for shift in shifts:
    if shift.id.month == 10:
        print(view.View_Shift(shift).main())
        # deliveries
        for delivery in shift.deliveries:
            print(view.View_Delivery(delivery).main())
            # orders
            for order in delivery.orders:
                print(view.view_order(order))
            # delivery extra stops
            for extra_stops in delivery.extra_stops:
                print(view.view_extra_stops(extra_stops))
        # shift extra stops
        for extra_stops in shift.extra_stops:
            print(view.view_extra_stops(extra_stops))
