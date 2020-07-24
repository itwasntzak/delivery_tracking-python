"""
resource legend:
    file/class_name__function/method_name__resource_occurrence
    file/class_name__resource_occurrence
"""

# delivery tracking
#   user error messages
#       shift

#       delivery

#       Order
Order__load__file_not_found = 'the file was not found, or does not exist'

#       tip

#       extra stop

#       split

#   python error messages
#       shift

#       delivery

#       Order
Order__class__wrong_id_type = "order id is of type '{}', must be an integer"
Order__class__wrong_parent_type = "parent of Order must be Delivery not '{}'"
Order__directory__no_parent = 'this Order does not have an assigned delivery'
Order__info_file__missing_id = 'this Order does not have an assigned id'

#       tip
# not used - Tip__input_data__wrong_parameter = 'parameter for input_data.tip must be of type Tip'

#       extra stop

#       split

# other files
#   user error messages

#   python error messages
consolidate__order__wrong_parameter = 'consolidate.order parameter must be of type Order, not '

load__order__wrong_parameter = 'load.order parameter must be of type Order'
