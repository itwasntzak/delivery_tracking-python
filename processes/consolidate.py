from utility.file import save


def order(order):
    from objects.order import Order
    if isinstance(order, Order):
        from os import remove
        from utility.file import save
        from utility.save import order as save_order

        file_list = order.file_list()
        # save data to one file
        save(order.csv(), order.file_list()['info_file'])
        # delete individual data files
        remove(file_list['id']), remove(file_list['tip'])
        remove(file_list['miles']), remove(file_list['end_time'])
        # create or update order ids file
        save(order.id, file_list['completed_ids'], separator=',')

    else:
        from resources.error_messages import\
            consolidate__order__wrong_parameter as error_messages
        raise TypeError(f'{error_messages}{type(order)}')
