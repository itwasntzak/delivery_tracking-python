from os import remove, rmdir

from utility.file import save


def delivery(delivery):
    from objects.delivery import Delivery
    if isinstance(delivery, Delivery):
        file_list = delivery.file_list()
        # save data to one file
        save(delivery.csv(), file_list['info_file'])
        # delete individual data files
        remove(file_list['average_speed']), remove(file_list['end_time'])
        remove(file_list['miles']), remove(file_list['order_quantity'])
        remove(file_list['start_time'])
        # create or update delivery ids file
        save(delivery.id, file_list['completed_ids'], separator=',')

    else:
        # todo: need to write error message for this
        raise TypeError


def order(order):
    from objects.order import Order
    if isinstance(order, Order):
        file_list = order.file_list()
        # save data to one file
        save(order.csv(), order.file_list()['info_file'])
        # delete individual data files
        remove(file_list['id']), remove(file_list['tip'])
        remove(file_list['miles']), remove(file_list['end_time'])
        rmdir(file_list['directory'])
        # create or update order ids file
        save(order.id, file_list['completed_ids'], separator=',')

    else:
        from resources.error_messages import\
            consolidate__order__wrong_parameter as error_messages
        raise TypeError(f'{error_messages} {type(order)}')
