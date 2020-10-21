
def delete_delivery(delivery)
    '''    
        this function deletes the files for delivery
        the delivery is not removed from shift delivery lists when this is called
    '''
    from objects import Delivery
    if not isinstance(delivery, Delivery):
        raise TypeError

    import os
    # get file paths
    file_list = delivery.file_list()

    # delivery still being tracked
    if delivery.in_progress is True:
        # start time
        if os.path.exists(file_list['start_time']):
            os.remove(file_list['start_time'])
        # distance
        if os.path.exists(file_list['distance']):
            os.remove(file_list['distance'])
        # average speed
        if os.path.exists(file_list['average_speed']):
            os.remove(file_list['average_speed'])
        # end time
        if os.path.exists(file_list['end_time']):
            os.remove(file_list['end_time'])
        
        # delete an order if one is in progress
        # delete any complete orders
        # delete an extra stop if one is in progress
        # delete any complete extra stops
    
    # completed delivery
    elif delivery.in_progress is False:
        # remove info file
        if os.path.exists(file_list['info']):
            os.remove(file_list['info'])
        
        # remove id from completed id's file
        delivery.remove_id_from_file()

        # delete any complete orders
        # delete any complete extra stops

def delete_order(order):
    '''    
        this function deletes the files for order
        the order is not removed from delivery order lists when this is called
    '''
    from objects import Order
    if not isinstance(order, Order):
        raise TypeError

    import os
    # get file paths
    file_list = order.file_list()

    # order in still being tracked
    if order.in_progress is True:
        # id
        if os.path.exists(file_list['id']):
            os.remove(file_list['id'])
        # tip
        if os.path.exists(file_list['tip']):
            os.remove(file_list['tip'])
        # distance
        if os.path.exists(file_list['distance']):
            os.remove(file_list['distance'])
        # end time
        if os.path.exists(file_list['end_time']):
            os.remove(file_list['end_time'])

    # order that has had all the data entered/was completed
    elif order.in_progress is False:
        # remove info file
        if os.path.exists(file_list['info']):
            os.remove(file_list['info'])
        
        # remove id from completed id's file
        order.remove_id_from_file()
