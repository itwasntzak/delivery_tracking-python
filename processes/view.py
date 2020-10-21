
class View_Shift:
    def __init__(self, shift):
        from objects import Shift
        if not isinstance(shift, Shift):
            raise TypeError

        self.shift = shift

    def main(self):
        shift_parts = self.shift.view()

        string = '\n- Shift -\n'
        # id
        string +=  f"\t{shift_parts['id']}\n"
        # start time
        if 'start_time' in shift_parts.keys():
            string += f"\t{shift_parts['start_time']}\n"
        # end time
        if 'end_time' in shift_parts.keys():
            string += f"\t{shift_parts['end_time']}\n"
        # distance
        if 'distance' in shift_parts.keys():
            string += f"\t{shift_parts['distance']}\n"
        # fuel economy
        if 'fuel_economy' in shift_parts.keys():
            string += f"\t{shift_parts['fuel_economy']}\n"
        # vehicle compensation
        if 'vehicle_comp' in shift_parts.keys():
            string += f"\t{shift_parts['vehicle_comp']}\n"
        # device compensation
        if 'device_comp' in shift_parts.keys():
            string += f"\t{shift_parts['device_comp']}\n"
        # total hours
        if 'total_hours' in shift_parts.keys():
            string += f"\t{shift_parts['total_hours']}\n"
        # extra tips claimed
        if 'extra_tips_claimed' in shift_parts.keys():
            string += f"\t{shift_parts['extra_tips_claimed']}\n"
        # carry out tips
        if 'carry_out_tips' in shift_parts.keys():
            string += f"\t{shift_parts['carry_out_tips']}\n"
        # total tips
        string += f"\t{shift_parts['total_tips']}\n"
        # card tips
        string += f"\t{shift_parts['card_tips']}\n"
        # cash tips
        string += f"\t{shift_parts['cash_tips']}\n"
        # number of deliveries
        string += f"\t{shift_parts['deliveries']}\n"
        # number of extra stops
        if 'extra_stops' in shift_parts.keys():
            string += f"\t{shift_parts['extra_stops']}\n"

        return string

    def quick(self):
        shift_parts = self.shift.view()

        string = '- Shift -\n'
        # id
        string +=  f"\t{shift_parts['id']}\n"
        # start time
        if 'start_time' in shift_parts.keys():
            string += f"\t{shift_parts['start_time']}\n"
        # number of deliveries
        string += f"\t{shift_parts['deliveries']}\n"
        # number of extra stops
        if 'extra_stops' in shift_parts.keys():
            string += f"\t{shift_parts['extra_stops']}\n"
        # carry out tips
        if 'carry_out_tips' in shift_parts.keys():
            string += f"\t{shift_parts['carry_out_tips']}\n"
        # total tips
        string += f"\t{shift_parts['total_tips']}\n"
        # card tips
        string += f"\t{shift_parts['card_tips']}\n"
        # cash tips
        string += f"\t{shift_parts['cash_tips']}\n"

        return string


class View_Delivery:
    def __init__(self, delivery):
        from objects import Delivery
        if not isinstance(delivery, Delivery):
            raise TypeError

        self.delivery = delivery

    def main(self):
        delivery_parts = self.delivery.view()

        # id
        string = f"\n{delivery_parts['id']}\n"

        # total duration
        if 'total_duration' in delivery_parts.keys():
            string += f"\t{delivery_parts['total_duration']}\n"

        # start time
        if 'start_time' in delivery_parts.keys():
            string += f"\t{delivery_parts['start_time']}\n"

        # end time
        if 'end_time' in delivery_parts.keys():
            string += f"\t{delivery_parts['end_time']}\n"

        # number of orders
        string += f"\t{delivery_parts['order_quantity']}\n"

        # number of extra stops
        if 'extra_stops' in delivery_parts.keys():
            string += f"\t{delivery_parts['extra_stops']}\n"

        # order ids
        if 'order_ids' in delivery_parts.keys():
            string += f"\t{delivery_parts['order_ids']}\n"

        # distance
        if 'distance' in delivery_parts.keys():
            string += f"\t{delivery_parts['distance']}\n"

        # average speed
        if 'average_speed' in delivery_parts.keys():
            string += f"\t{delivery_parts['average_speed']}\n"

        return string

    def quick(self):
        delivery_parts = self.delivery.view()

        # id
        string = f"{delivery_parts['id']}\n"

        # start time
        if 'start_time' in delivery_parts.keys():
            string += f"\t{delivery_parts['start_time']}\n"

        # number of orders
        string += f"\t{delivery_parts['order_quantity']}\n"

        return string


def view_order(order):
    from objects import Order
    if not isinstance(order, Order):
        raise TypeError

    order_parts = order.view()
    # id
    string = f"{order_parts['id']}\n"
    # tip
    # total amount
    if (order.tip.card != 0.0 and order.tip.cash != 0.0) or\
            order.tip.collection() == (0.0, 0.0, 0.0):
        string += f"\t{order.tip.view()['total']}\n"
    # card
    if order.tip.card != 0.0:
        string += f"\t{order.tip.view()['card']}\n"
    # cash
    if order.tip.cash != 0.0:
        string += f"\t{order.tip.view()['cash']}\n"
    # unknown
    if order.tip.unknown != 0.0:
        string += f"\t{order.tip.view()['unknown']}\n"
    # distance
    if 'distance' in order_parts.keys():
        string += f"\t{order_parts['distance']}\n"
    # end time
    if 'end_time' in order_parts.keys():
        string += f"\t{order_parts['end_time']}\n"

    return string


def view_tip(tip):
    text = tip.view()
    string = '\n'
    # card and cash
    if (tip.card != 0.0 and tip.cash != 0.0) or\
            tip.collection() == (0.0, 0.0, 0.0):
        string += f"{text['total']}\n"
    # card
    if tip.card != 0.0:
        string += f"{text['card']}\n"
    # cash
    if tip.cash != 0.0:
        string += f"{text['cash']}\n"
    # unknown
    if tip.unknown != 0.0:
        string += f"{text['unknown']}\n"

    return string


def view_split(split):
    from objects import Split
    if not isinstance(split, Split):
        raise TypeError
    if split.start_time is None:
        raise ValueError('split must have at least a start time to be viewed')

    split_parts = split.view()

    string = '\n- Split -\n'\
            f"\t{split_parts['start_time']}\n"

    if 'end_time' in split_parts.keys():
        string += f"\t{split_parts['end_time']}\n"

    if 'distance' in split_parts.keys():
        string += f"\t{split_parts['distance']}\n"

    return string


def view_extra_stop(extra_stop):
    from objects import Extra_Stop
    if not isinstance(extra_stop, Extra_Stop):
        raise TypeError(f'{type(extra_stop)}')

    extra_stop_parts = extra_stop.view()

    string = f"\n{extra_stop_parts['id']}\n"

    if 'start_time' in extra_stop_parts.keys():
        string += f"\t{extra_stop_parts['start_time']}\n"
    
    if 'end_time' in extra_stop_parts.keys():
        string += f"\t{extra_stop_parts['end_time']}\n"
    
    if 'location' in extra_stop_parts.keys():
        string += f"\t{extra_stop_parts['location']}\n"
    
    if 'reason' in extra_stop_parts.keys():
        string += f"\t{extra_stop_parts['reason']}\n"
    
    if 'distance' in extra_stop_parts.keys():
        string += f"\t{extra_stop_parts['distance']}\n"
    
    return string
