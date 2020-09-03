
# todo: need to update all of these to classes be able to generate different views

def view_shift(shift):
    from objects import Shift
    if not isinstance(shift, Shift):
        raise TypeError

    shift_parts = shift.view()

    string =  f"{shift_parts['id']}\n"
    if 'start_time' in shift_parts.keys():
        string += f"{shift_parts['start_time']}\n"
    if 'end_time' in shift_parts.keys():
        string += f"{shift_parts['end_time']}\n"

    string += f"{shift_parts['deliveries']}\n"

    if 'extra_stops' in shift_parts.keys():
        string += f"{shift_parts['extra_stops']}\n"
    if 'carry_out_tips' in shift_parts.keys():
        string += f"{shift_parts['carry_out_tips']}\n"
    if 'total_hours' in shift_parts.keys():
        string += f"{shift_parts['total_hours']}\n"
    if 'distance' in shift_parts.keys():
        string += f"{shift_parts['distance']}\n"
    if 'fuel_economy' in shift_parts.keys():
        string += f"{shift_parts['fuel_economy']}\n"
    if 'vehicle_comp' in shift_parts.keys():
        string += f"{shift_parts['vehicle_comp']}\n"
    if 'device_comp' in shift_parts.keys():
        string += f"{shift_parts['device_comp']}\n"
    if 'extra_tips_claimed' in shift_parts.keys():
        string += f"{shift_parts['extra_tips_claimed']}\n"
    
    return string


def view_delivery(delivery):
    from objects import Delivery
    if not isinstance(delivery, Delivery):
        raise TypeError

    delivery_parts = delivery.view()

    string = f"{delivery_parts['id']}\n"

    if 'total_duration' in delivery_parts.keys():
        string += f"{delivery_parts['total_duration']}\n"

    if 'start_time' in delivery_parts.keys():
        string += f"{delivery_parts['start_time']}\n"
    
    if 'end_time' in delivery_parts.keys():
        string += f"{delivery_parts['end_time']}\n"
    
    string += f"{delivery_parts['order_quantity']}\n"
    
    if 'extra_stops' in delivery_parts.keys():
        string += f"{delivery_parts['extra_stops']}\n"
    
    if 'order_ids' in delivery_parts.keys():
        string += f"{delivery_parts['order_ids']}\n"
    
    if 'distance' in delivery_parts.keys():
        string += f"{delivery_parts['distance']}\n"
    
    if 'average_speed' in delivery_parts.keys():
        string += f"{delivery_parts['average_speed']}\n"

    
    return string


def view_order(order):
    # todo: these need to add conditionals for end time or distance for older shifts
    from objects import Order
    if not isinstance(order, Order):
        raise TypeError

    order_parts = order.view()

    string = f"{order_parts['id']}\n"\
             f"{order_parts['end_time']}\n"\
             f"{order_parts['distance']}\n"
    
    if 'card' in order_parts.keys():
        string += f"{order_parts['card']}\n"
    
    if 'cash' in order_parts.keys():
        string += f"{order_parts['cash']}\n"

    if 'unknown' in order_parts.keys():
        string += f"{order_parts['unknown']}\n"

    return string


def view_split(split):
    from objects import Split
    if not isinstance(split, Split):
        raise TypeError

    split_parts = split.view()

    string = f"{split_parts['start_time']}\n"

    if 'end_time' in split_parts.keys():
        string += f"{split_parts['end_time']}\n"

    if 'distance' in split_parts.keys():
        string += f"{split_parts['distance']}\n"

    return string


def view_extra_stop(extra_stop):
    # todo: need to add test for start time view part for shift extra stops
    from objects import Extra_Stop
    if not isinstance(extra_stop, Extra_Stop):
        raise TypeError(f'{type(extra_stop)}')

    extra_stop_parts = extra_stop.view()

    string = f"{extra_stop_parts['id']}\n"

    if 'start_time' in extra_stop_parts.keys():
        string += f"{extra_stop_parts['start_time']}\n"
    
    string += f"{extra_stop_parts['end_time']}\n"\
              f"{extra_stop_parts['location']}\n"\
              f"{extra_stop_parts['reason']}\n"\
              f"{extra_stop_parts['distance']}\n"
    
    return string
