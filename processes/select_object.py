
def order(delivery):
    from objects.delivery import Delivery
    if not isinstance(delivery, Delivery):
        raise TypeError

    from utility.user_input import integer

    prompt = f'Delivery #{delivery.id} has orders:'
    for id in delivery.order_ids:
        prompt += f'\n{id}'
    prompt += f'\nPlease enter the I.D. of the order you want to revise.'

    user_choice = integer(prompt)
    while user_choice not in delivery.order_ids:
        user_choice = integer(prompt)
    else:
        # todo: update once order attribute selection is writen
        pass
