import datetime
import os

import extra_stop
import input_data
import order
import process_data
import utility_function


def on_delivery(prompt):
    # creating file so code knows while on delivery, and can continue
    utility_function.write_data(
        path='delivery',
        file='on_delivery',
        data=None
    )

    while True:
        wait_for_user = input_data.get_input(
            prompt=prompt + '\n1 after returning | 2 for extra stop\n',
            kind=int
        )
        if wait_for_user == 1:
            # remove on_delivery file so code can know a delivery has ended
            os.remove(os.path.join(
                'delivery', 'on_delivery')
            )
            break
        elif wait_for_user == 2:
            # extra stop option
            extra_stop.extra_stop()
            continue
        else:
            print('\nInvalid input...')


def number_of_orders():
    return utility_function.write_data(
        path='delivery',
        file='number_of_orders.txt',
        data=input_data.input_data(
            prompt1='\nNumber of orders?\n',
            input_type1=int,
            prompt2='\nIs this correct? [y/n]\n',
            input_type2=str,
            option_yes='y',
            option_no='n'
        )
    )


def order_numbers_file():
    if os.path.exists(os.path.join(
        'delivery', 'order_numbers.txt'
        )
    ):
        utility_function.append_data(
            path='delivery',
            file='order_numbers.txt',
            data=',' + utility_function.read_data(
                path='deliver',
                file='order_number.txt'
            )
        )
    else:
        utility_function.write_data(
            path='delivery',
            file='order_numbers.txt',
            data=utility_function.read_data(
                path='delivery',
                file='order_number.txt'
            )
        )


def delivery():
    os.mkdir('delivery')
    utility_function.write_data(
        path='delivery',
        file='delivery_start_time.txt',
        data=utility_function.now()
    )
    numbr_of_orders = number_of_orders()

    if numbr_of_orders == 1:
        on_delivery(prompt='\nDriving to address...')
        order.order_number()
        order.tip()
        tip_data = utility_function.read_data(
            path='delivery',
            file='tip.txt'
        )
        if tip_data == 'n/a':
            utility_function.write_data(
                path='delivery',
                file='tip_type.txt',
                data='n/a'
            )
        else:
            order.tip_type()
        utility_function.miles_traveled(prompt='Miles traveled:    #.#')
    # save current time for end of order
        utility_function.write_data(
            path='delivery',
            file='order_end_time.txt',
            data=utility_function.now(),
        )
        order_numbers_file()
        order_number = process_data.consolidate_order()
        delivery_start_time = utility_function.read_data(
            path='delivery',
            file='delivery_start_time.txt'
        )
        order_end_time = order.get_order_data(
            path='delivery',
            file=order_number + '.txt'
        )
        utility_function.time_took(
            start_time=datetime.datetime.strptime(
                delivery_start_time, '%Y-%m-%d %H:%M:%S.%f'
            ),
            end_time=datetime.datetime.strptime(
                order_end_time[3], '%Y-%m-%d %H:%M:%S.%f'
            ),
            var_word='Order'
        )

    elif numbr_of_orders > 1:
        for value in range(numbr_of_orders):
            on_delivery(prompt='\nDriving to address...')
            order.order_number()
            order.tip()
            tip_data = utility_function.read_data(
                path='delivery',
                file='tip.txt'
            )
            if tip_data == 'n/a':
                utility_function.write_data(
                    path='delivery',
                    file='tip_type.txt',
                    data='n/a'
                )
            else:
                order.tip_type()
            utility_function.miles_traveled(prompt='Miles traveled:    #.#')
            utility_function.write_data(
                path='delivery',
                file='order_end_time.txt',
                data=utility_function.now()
            )
            order_numbers_file()
            order_number = process_data.consolidate_order()
            delivery_start_time = utility_function.read_data(
                path='delivery',
                file='delivery_start_time.txt'
            )
            order_end_time = order.get_order_data(
                path='delivery',
                file=order_number + '.txt'
            )
            utility_function.time_took(
                start_time=datetime.datetime.strptime(
                    delivery_start_time, '%Y-%m-%d %H:%M:%S.%f'
                ),
                end_time=datetime.datetime.strptime(
                    order_end_time[3], '%Y-%m-%d %H:%M:%S.%f'
                ),
                var_word='Order'
            )

    on_delivery(prompt='Driving back to store...')
    utility_function.miles_traveled(prompt='Total miles traveled:    #.#')
    delivery_start_time = utility_function.read_data(
        path='delivery',
        file='delivery_start_time.txt'
    )
    delivery_end_time = utility_function.write_data(
        path='delivery',
        file='delivery_end_time.txt',
        data=utility_function.now()
    )
    utility_function.time_took(
        start_time=datetime.datetime.strptime(
            str(delivery_start_time), '%Y-%m-%d %H:%M:%S.%f'
        ),
        end_time=delivery_end_time,
        var_word='Delivery'
    )
    process_data.consolidate_delivery()
    utility_function.write_data(
        path='shift',
        file='number_of_deliveries.txt',
        data=int(utility_function.delivery_number('number')) + 1
    )
