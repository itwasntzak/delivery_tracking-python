from os import remove, rmdir

from utility.file import save, write


def shift(shift):
    from objects.shift import Shift
    if isinstance(shift, Shift):
        file_list = shift.file_list()
        # save data to one file
        write(shift.csv(), file_list.pop('info_file'))
        # remove file from list to not delete
        file_list.pop('carry_out_tips')
        completed_ids = file_list.pop('completed_ids')
        directory = file_list.pop('directory')
        # delete indavidual files
        for key in file_list:
            remove(file_list[key])
        rmdir(directory)
        # create/update completed ids file
        save(shift.id, completed_ids)

    else:
        raise TypeError


def delivery(delivery):
    from objects.delivery import Delivery
    if isinstance(delivery, Delivery):
        file_list = delivery.file_list()
        # save data to one file
        write(delivery.csv(), file_list.pop('info_file'))
        # remove file to not be deleted
        completed_ids = file_list.pop('completed_ids')
        directory = file_list.pop('directory')
        # delete individual data files
        for key in file_list:
            remove(file_list[key])
        rmdir(directory)
        # todo: after adding delivery subdir to file list, maybe need to rename it
        # create or update delivery ids file
        save(delivery.id, completed_ids, separator=',')

    else:
        # todo: need to write error message for this
        raise TypeError


def order(order):
    from objects.order import Order
    if isinstance(order, Order):
        file_list = order.file_list()
        # save data to one file
        write(order.csv(), order.info_file())
        # remove file from list to not delete
        completed_ids = file_list.pop('completed_ids')
        directory = file_list.pop('directory')
        # delete individual data files
        for key in file_list:
            remove(file_list[key])
        rmdir(directory)
        # create or update order ids file
        save(order.id, completed_ids, separator=',')

    else:
        from resources.error_messages import\
            consolidate__order__wrong_parameter as error_messages
        raise TypeError(f'{error_messages} {type(order)}')


def split(split):
    from objects.split import Split
    if isinstance(split, Split):
        # get list of files
        file_list = split.file_list()
        # save all split data to one file
        write(split.csv(), file_list.pop('info'))
        directory = file_list.pop('directory')
        # delete directory and individual files
        for key in file_list:
            remove(file_list[key])
        rmdir(directory)

    else:
        raise TypeError


def shift_extra_stop(extra_stop):
    # get list of files
    file_list = extra_stop.file_list()
    # save extra stop data to a single file
    write(extra_stop.nlsv(), file_list.pop('info'))
    # remove files from list to not be deleted
    file_list.pop('running_id')
    # files to not be deleted that will also be needed later
    completed_ids = file_list.pop('completed_ids')
    directory = file_list['directory']
    # delete indavidual data files
    for key in file_list:
        remove(file_list[key])
    # deleted directory after its empty
    rmdir(directory)
    # updated completed ids file
    save(extra_stop.id, completed_ids)
    # update running id number
    extra_stop.update_running_id()


def delivery_extra_stop(extra_stop):
    # get list of files
    file_list = extra_stop.file_list()
    # save extra stop data to a single file
    write(extra_stop.nlsv(), file_list.pop('info'))
    # remove files from list to not be deleted
    file_list.pop('running_id')
    file_list.pop('start_time') # this file wont exist when in a delivery
    # files to not be deleted that will also be needed later
    completed_ids = file_list.pop('completed_ids')
    directory = file_list['directory']
    # delete indavidual data files
    for key in file_list:
        remove(file_list[key])
    # deleted directory after its empty
    rmdir(directory)
    # updated completed ids file
    save(extra_stop.id, completed_ids)
    # update running id number
    extra_stop.update_running_id()
