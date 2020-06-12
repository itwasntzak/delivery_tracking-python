from utility.file import Read


def tip(tip):
    """
    file_path=sting of file path or\n
    order_data=list/tuple
    """

    try:
        if tip.file_path:
            tip.__init__(Read(tip.file_path).floats())
    except AttributeError:
        # not sure how to handle this
        pass

    try:
        if tip.order_data:
            tip.__init__(tip.order_data[0], tip.order_data[1], tip.order_data[2])
    except AttributeError:
        # not sure how to handle this
        pass

    return tip


def carry_out_tips(tip, tip_list=[]):
    pass


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
            from utility import to_datetime
            order.tip = tip(order_data)
            order.miles_traveled = float(order_data[3])
            order.end_time = to_datetime(order_data[4])
            return order
    else:
        from resources.error_messages import\
            load__order__wrong_parameter as error_message
        raise TypeError(error_message)


def delivery(delivery, file_path=None):
    """
    file_path=sting of file path or\n
    file_path=a list/tuple with directory path and file name
    """
    if isinstance(file_path, str):
        delivery_data = Read(file_path).comma()

    elif isinstance(file_path, list or tuple):
        delivery_data = Read(file_path[1], directory_path=file_path[0]).comma()


class Load:

    def __init__(self):
        pass
