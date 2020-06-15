'''
 todo: for shift, check to resume delivery or shift extra stop in the menu
       then when continuing delivery, check if delivery extra stop or order exist
       then continue entering any remaining orders, and drive back to store
'''


def delivery(delivery):
    from os import path
    from objects.order import Order
    from processes.input_data import delivery as continue_delivery
    # todo: add loading/checking for extra stop once extra stop has been writen

    order = Order(delivery)
    if path.exists(order.file_list['directory']):
        from processes.load import order as load_order
        delivery.add_order(load_order(order))

    return continue_delivery(delivery)
