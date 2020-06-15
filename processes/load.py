from utility.file import Read


def delivery(delivery):
    from objects.delivery import Delivery
    # delivery info
    if isinstance(delivery, Delivery):
        try:
            delivery_data = Read(delivery.file_list['directory']).comma()
        except FileNotFoundError:
            # todo: still not sure how to handle when file isnt found
            pass
        else:
            from utility.utility import to_datetime
            delivery.miles_traveled = float(delivery_data[0])
            delivery.average_speed = int(delivery_data[1])
            delivery.start_time = to_datetime(delivery_data[2])
            delivery.end_time = to_datetime(delivery_data[3])

        # orders
        from objects.order import Order
        try:
            order_ids = Read(Order(delivery).file_list['completed_ids']).comma()
        except FileNotFoundError:
            # todo: still not sure how to handle when file isnt found
            pass
        else:
            for id in order_ids:
                delivery.add_order(order(Order(delivery, id)))

        # todo: need to add loading extra stops

        # return loaded delivery
        return delivery
    else:
        # todo: need to write error message
        raise TypeError


def order(order):
    from objects.order import Order
    if isinstance(order, Order):
        try:
            order_data = Read(order.info_file(), order.directory()).comma
        except AttributeError:
            # todo: present user with option to input id
            # todo: present user with option to cancel order
            pass
        except FileNotFoundError:
            # todo: present user with the option to change the id
            # todo: present user with option to enter data for the order
            # todo: present user with option to remove the order id
            from resources.error_messages import Order__load__file_not_found
            print(Order__load__file_not_found)
        else:
            from objects.tip import Tip
            from utility.utility import to_datetime
            tip_instance = Tip()
            tip_instance.order_data = order_data
            order.tip = tip(tip_instance)
            order.miles_traveled = float(order_data[3])
            order.end_time = to_datetime(order_data[4])
            return order
    else:
        from resources.error_messages import\
            load__order__wrong_parameter as error_message
        raise TypeError(error_message)


def tip(tip):
    """
    file_path=sting of file path or\n
    order_data=list/tuple
    """

    try:
        if tip.file_path:
            tip.__init__(Read(tip.file_path).floats())
    except AttributeError:
        # todo: not sure how to handle this
        pass

    try:
        if tip.order_data:
            tip.__init__(tip.order_data[0], tip.order_data[1], tip.order_data[2])
    except AttributeError:
        # todo: not sure how to handle this
        pass

    return tip


def carry_out_tips(tip, tip_list=[]):
    pass
