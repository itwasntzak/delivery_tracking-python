"""
resource legend:
    file/class_name__function/method_name__resource_occurrence
    file/class_name__resource_occurrence
"""

# directory names
parent_directory = 'delivery_tracking'
data_directory = 'data'
shifts_directory = 'shifts'
delivery_directory = 'delivery'
order_directory = 'order'
extra_stop_directory = 'extra_stop'
split_directory = 'split'

# list of shared file names
end_time = 'end_time.txt'
distance = 'distance.txt'
start_time = 'start_time.txt'

# shift files
Shift__completed_ids = 'shift_ids.txt'
Shift__completed_info = 'shift_info.txt'
Shift__carry_out_tips = 'carry_out_tips.txt'
Shift__device_compensation = 'device_compensation.txt'
Shift__extra_tips_claimed = 'extra_tips_claimed.txt'
Shift__fuel_economy = 'fuel_economy.txt'
Shift__hours = 'hours.txt'
Shift__vehicle_compensation = 'vehicle_compensation.txt'

# delivery files
Delivery__average_speed = 'average_speed.txt'
Delivery__completed_ids = 'delivery_ids.txt'
Delivery__info = 'delivery_info.txt'
Delivery__order_quantity = 'order_quantity.txt'

# order files
Order__completed_ids = 'order_ids.txt'
Order__id = 'order_id.txt'

# tip files
Tip__info = 'tip.txt'

# extra stop files
Extra_Stop__completed_ids = 'extra_stop_ids.txt'
Extra_Stop__info = '{}.txt'
Extra_Stop__location = 'location.txt'
Extra_Stop__reason = 'reason.txt'
Extra_Stop__running_id = 'extra_stop_id_number.txt'

# split
Split__info = 'split_info.txt'
