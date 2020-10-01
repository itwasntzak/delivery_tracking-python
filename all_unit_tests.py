import unittest
from menus_test import Test_Menus
from processes.consolidate_test import Test_Consolidate
from processes.load_test import Test_Load
from processes.select_test import Test_Select
from processes.track_test import Test_Track
from processes.view_test import Test_View
from objects_test import Test_Delivery, Test_Shift
from utility.file_test import Test_File
from utility.utility_test import Test_Utility
from utility.user_input_test import Test_User_Input

# todo: convience tests; load_shift_deliveries, load_shift_extra_stops, load_delivery_orders, 
#           load_delivery_extra_stops
# todo: none automated tests
# todoL write tests for objects in progress

# menus hasnt been looked at on how to unittest
# utility hasnt been looked at on how to unittest

# menus
Test_Menus()

# objects
Test_Delivery()
Test_Shift()

# processes
# consolidate
Test_Consolidate()

# load
Test_Load()

# select
Test_Select()
 
# track
Test_Track()

# view
Test_View()

# utilities
# file
Test_File()

# user input
Test_User_Input()

# utility
Test_Utility()