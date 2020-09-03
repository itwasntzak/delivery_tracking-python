import unittest
from processes.consolidate_test import Test_Consolidate
from processes.load_test import Test_Load
from processes.select_test import Test_Select
from processes.track_test import Test_Track
from processes.view_test import Test_View
from objects_test import Test_Delivery, Test_Shift

# todo: convience tests; load_shift_deliveries, load_shift_extra_stops, load_delivery_orders, 
#           load_delivery_extra_stops
# todo: none automated tests
# todoL write tests for objects in progress

# menus hasnt been looked at on how to unittest
# utility hasnt been looked at on how to unittest

# objects
Test_Delivery()
Test_Shift()

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
