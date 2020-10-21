
def completed_shift():
    import objects
    from utility.utility import To_Datetime
    from utility.utility import now

    # shift
    shift = objects.Shift(now().date())
    shift.miles_traveled = 12.3
    shift.fuel_economy = 21.2
    shift.vehicle_compensation = 13.07
    shift.device_compensation = .27
    shift.extra_tips_claimed = 3.0
    shift.total_hours = 9.7
    shift.start_time =\
        To_Datetime('2020-07-13 09:00:00.100').from_datetime()
    shift.end_time =\
        To_Datetime('2020-07-13 18:30:00.100').from_datetime()
    shift.carry_out_tips = [objects.Tip(card=3.11), objects.Tip(cash=2.71)]

    # delivery 1
    delivery_1 = objects.Delivery(shift, 0)
    delivery_1.start_time =\
        To_Datetime('2020-07-13 10:30:00.100').from_datetime()
    delivery_1.end_time =\
        To_Datetime('2020-07-13 10:55:00.100').from_datetime()
    delivery_1.miles_traveled = 3.7
    delivery_1.average_speed = 21
    # order
    order_1 = objects.Order(delivery_1, 7)
    order_1.end_time =\
        To_Datetime('2020-07-13 10:43:00.100').from_datetime()
    order_1.miles_traveled = 1.8
    order_1.tip = objects.Tip(cash=5)
    # add order to delivery
    delivery_1.order_ids.append(order_1.id)
    delivery_1.orders.append(order_1)
    # add delivery to shift
    shift.delivery_ids.append(delivery_1.id)
    shift.deliveries.append(delivery_1)

    # delivery 2
    delivery_2 = objects.Delivery(shift, 1)
    delivery_2.start_time =\
        To_Datetime('2020-07-13 11:20:00.100').from_datetime()
    delivery_2.end_time =\
        To_Datetime('2020-07-13 11:47:00.100').from_datetime()
    delivery_2.miles_traveled = .7
    delivery_2.average_speed = 14
    # order
    order_2 = objects.Order(delivery_2, 36)
    order_2.end_time =\
        To_Datetime('2020-07-13 11:31:00.100').from_datetime()
    order_2.miles_traveled = 3.1
    order_2.tip = objects.Tip()
    # add order to delivery
    delivery_2.order_ids.append(order_2.id)
    delivery_2.orders.append(order_2)
    # extra stop
    extra_stop_2 = objects.Extra_Stop(delivery_2, 1)
    extra_stop_2.location = 'mongolian grill'
    extra_stop_2.reason = 'trade food'
    extra_stop_2.miles_traveled = 4.1
    extra_stop_2.end_time =\
        To_Datetime('2020-08-25 13:27:57.100').from_datetime()
    delivery_2.extra_stop_ids.append(extra_stop_2.id)
    delivery_2.extra_stops.append(extra_stop_2)
    # add delivery to shift
    shift.delivery_ids.append(delivery_2.id)
    shift.deliveries.append(delivery_2)

    # delivery 3
    delivery_3 = objects.Delivery(shift, 2)
    delivery_3.start_time =\
        To_Datetime('2020-07-13 12:12:00.100').from_datetime()
    delivery_3.end_time =\
        To_Datetime('2020-07-13 12:41:00.100').from_datetime()
    delivery_3.miles_traveled = 6.7
    delivery_3.average_speed = 23
    # order 1
    order_3 = objects.Order(delivery_3, 47)
    order_3.end_time =\
        To_Datetime('2020-07-13 12:28:00.100').from_datetime()
    order_3.miles_traveled = 3.4
    order_3.tip = objects.Tip(card=2.78)
    # add order to delivery
    delivery_3.order_ids.append(order_3.id)
    delivery_3.orders.append(order_3)
    # order 2
    order_4 = objects.Order(delivery_3, 58)
    order_4.end_time =\
        To_Datetime('2020-07-13 12:28:00.100').from_datetime()
    order_4.miles_traveled = 3.4
    order_4.tip = objects.Tip(card=3.41, cash=3)
    # add order to delivery
    delivery_3.order_ids.append(order_4.id)
    delivery_3.orders.append(order_4)
    # add delivery to shift
    shift.delivery_ids.append(delivery_3.id)
    shift.deliveries.append(delivery_3)

    # extra stop 1
    extra_stop_1 = objects.Extra_Stop(shift, 0)
    extra_stop_1 = objects.Extra_Stop(shift)
    extra_stop_1.start_time =\
        To_Datetime('2020-08-25 10:05:33.100').from_datetime()
    extra_stop_1.location = 'bank'
    extra_stop_1.reason = 'change'
    extra_stop_1.miles_traveled = 3.6
    extra_stop_1.end_time =\
        To_Datetime('2020-08-25 10:15:33.100').from_datetime()
    # add extra stop to shift
    shift.extra_stop_ids.append(extra_stop_1.id)
    shift.extra_stops.append(extra_stop_1)

    # extra stop 2
    extra_stop_3 = objects.Extra_Stop(shift, 2)
    extra_stop_3 = objects.Extra_Stop(shift)
    extra_stop_3.start_time =\
        To_Datetime('2020-08-25 13:17:38.100').from_datetime()
    extra_stop_3.location = 'mongolian grill'
    extra_stop_3.reason = 'trade food'
    extra_stop_3.miles_traveled = 4.1
    extra_stop_3.end_time =\
        To_Datetime('2020-08-25 13:27:57.100').from_datetime()
    # add extra stop to shift
    shift.extra_stop_ids.append(extra_stop_3.id)
    shift.extra_stops.append(extra_stop_3)

    # split
    split = objects.Split(shift)
    split.start_time = To_Datetime('2020-08-25 14:03:57.100').from_datetime()
    split.miles_traveled = 3.1
    split.end_time = To_Datetime('2020-08-25 16:03:57.100').from_datetime()
    shift.split = split

    return shift


def get_tip(card=False, cash=False, both=False, unknown=False):
    import random
    from objects import Tip

    chance = random.randint(0, 3)

    # card tip
    if card is True or chance == 0:
        return Tip(random.uniform(.01, 20.0))
    # cash tip
    if cash is True or chance == 1:
        return Tip(cash=random.uniform(.01, 20.0))
    # card & cash tip
    if both is True or chance == 2:
        card_tip = random.uniform(.01, 20.0)
        cash_tip = random.uniform(.01, 20.0)
        return Tip(card_tip, cash_tip)
    # unknown
    if unknown is True or chance == 3:
        return Tip(unknown=random.uniform(.01, 20.0))
