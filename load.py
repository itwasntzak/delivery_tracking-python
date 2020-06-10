from file import Read

from utility import to_datetime


def tip(tip, file_path=None, order_data=None):
    """
    file_path=sting of file path or\n
    file_path=a list/tuple with directory path and file name,\n
    order_data=list/tuple
    """
    if file_path is not None and isinstance(file_path, str):
        tip = Tip(Read(file_path).floats())
    elif file_path is not None and isinstance(file_path, list or tuple):
        tip = Tip(Read(file_path[1], directory_path=file_path[0]).floats())
    elif file_path is not None:
        raise TypeError

    if order_data is not None and isinstance(order_data, list or tuple):
        tip = Tip(order_data[0], order_data[1], order_data[2])
    elif order_data is not None:
        raise TypeError

    if isinstance(tip, Tip):
        return tip


def carry_out_tips(tip, tip_list=None):
    if tip_list is None:
        tip_list = []


def order(order, file_path=None):
    """
    file_path=sting of file path or\n
    file_path=a list/tuple with directory path and file name
    """
    if file_path is not None and isinstance(file_path, str):
        order_data = Read(file_path).comma
        order.tip = tip(order_data=order_data)
        order.miles_traveled = float(order_data[3])
        order.end_time = to_datetime(order_data[4])
        return order

    elif file_path is not None and isinstance(file_path, list or tuple):
        order_data = Read(file_path[1], directory_path=file_path[0]).comma()
        order.tip = tip(order_data=order_data)
        order.miles_traveled = float(order_data[3])
        order.end_time = to_datetime(order_data[4])
        return order


def delivery(delivery, file_path=None):
    """
    file_path=sting of file path or\n
    file_path=a list/tuple with directory path and file name
    """
    if file_path is not None and isinstance(file_path, str):
        delivery_data = Read(file_path).comma()

    elif file_path is not None and isinstance(file_path, list or tuple):
        delivery_data = Read(file_path[1], directory_path=file_path[0]).comma()
