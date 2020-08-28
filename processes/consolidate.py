
def consolidate_shift(shift):
    from objects import Shift
    if not isinstance(shift, Shift):
        raise TypeError

    from os import remove
    from utility.file import save, write

    file_list = shift.file_list()
    # save data to one file
    write(shift.csv(), file_list.pop('info'))
    # remove file from dict to not delete
    file_list.pop('tips')
    file_list.pop('directory')
    completed_ids = file_list.pop('completed_ids')
    # delete indavidual files
    for key in file_list:
        remove(file_list[key])
    # create/update completed ids file
    save(shift.id, completed_ids, separator=',')


def consolidate_delivery(delivery):
    from objects import Delivery
    if not isinstance(delivery, Delivery):
        # todo: need to write error message for this
        raise TypeError

    from os import remove
    from utility.file import save, write

    file_list = delivery.file_list()
    # save data to one file
    write(delivery.csv(), file_list.pop('info'))
    # remove file/directory to not be deleted
    directory = file_list.pop('directory')
    completed_ids = file_list.pop('completed_ids')
    # delete individual data files
    for key in file_list:
        remove(file_list[key])
    # create or update delivery ids file
    save(delivery.id, completed_ids, separator=',')


def consolidate_order(order):
    from objects import Order
    if not isinstance(order, Order):
        from resources.error_messages import\
            consolidate__order__wrong_parameter as error_messages
        raise TypeError(f'{error_messages} {type(order)}')

    from os import remove, rmdir
    from utility.file import save, write

    file_list = order.file_list()
    # save data to one file
    write(order.csv(), file_list.pop('info'))
    # remove file from list to not delete
    completed_ids = file_list.pop('completed_ids')
    directory = file_list.pop('directory')
    # delete individual data files
    for key in file_list:
        remove(file_list[key])
    rmdir(directory)
    # create or update order ids file
    save(order.id, completed_ids, separator=',')


def consolidate_split(split):
    from objects import Split
    if not isinstance(split, Split):
        raise TypeError

    from os import remove, rmdir
    from utility.file import write

    # get list of files
    file_list = split.file_list()
    # save all split data to one file
    write(split.csv(), file_list.pop('info'))
    directory = file_list.pop('directory')
    # delete directory and individual files
    for key in file_list:
        remove(file_list[key])
    rmdir(directory)


def consolidate_extra_stop(extra_stop):
    from objects import Extra_Stop, Shift
    if not isinstance(extra_stop, Extra_Stop):
        raise TypeError

    from os import remove, rmdir
    from utility.file import write, save

    # get list of files
    file_list = extra_stop.file_list()
    # save extra stop data to a single file
    write(extra_stop.nlsv(), file_list.pop('info'))
    # this file wont exist if the extra stop is delivery
    start_time_file = file_list.pop('start_time')
    # files to not be deleted that will be needed later
    completed_ids = file_list.pop('completed_ids')
    directory = file_list.pop('directory')
    running_id = file_list.pop('running_id')
    # delete indavidual data files
    for key in file_list:
        remove(file_list[key])
    if isinstance(extra_stop.parent, Shift):
        remove(start_time_file)
    # deleted directory after its empty
    rmdir(directory)
    # updated completed ids file
    save(extra_stop.id, completed_ids, separator=',')
    # update running id number
    write(extra_stop.id + 1, running_id)
