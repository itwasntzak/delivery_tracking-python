from objects.shift import Shift
from objects.split import Split
from processes.load import shift as load_shift
from utility.file import Read
from utility.utility import now, To_Datetime
from view_objects import\
    shift as view_shift,\
    delivery as view_delivery,\
    order as view_order,\
    extra_stop as view_extra_stop,\
    split as view_split

string_ids = Read(Shift(now().date()).file_list()['completed_ids']).comma()
shift_ids = [To_Datetime(id).from_date() for id in string_ids]
shifts = [load_shift(id.date()) for id in shift_ids]

shift_id = 5

print(view_shift(shifts[shift_id]))

if isinstance(shifts[shift_id].split, Split):
    print(view_split(shifts[shift_id].split))

for delivery_id in shifts[shift_id].delivery_ids:
    print(view_delivery(shifts[shift_id].deliveries[delivery_id]))

    for order_id in range(len(shifts[shift_id].deliveries[delivery_id].orders)):
        print(view_order(shifts[shift_id].deliveries[delivery_id].orders[order_id]))

    for extra_stop_id in range(len(shifts[shift_id].deliveries[delivery_id].extra_stops)):
        print(view_extra_stop(shifts[shift_id].deliveries[delivery_id].extra_stops[extra_stop_id]))

for extra_stop_id in range(len(shifts[shift_id].extra_stops)):
    print(view_extra_stop(shifts[shift_id].extra_stops[extra_stop_id]))
