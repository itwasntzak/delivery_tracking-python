import unittest

class Test_Select(unittest.TestCase):
    # code is written so that build prompt, get index and match check can be
    #   tested automaticly with unittests

    def setUp(self):
        from testing_tools import completed_shift

        self.shift = completed_shift()

    def test_select_delivery(self):
        from processes.select import Select_Delivery

        select_delivery = Select_Delivery(self.shift, test=True)

        # test build_prompt
        select_delivery.build_prompt()
        expected =\
            'There are 3 number of deliveries\n'\
            'Delivery #1\n'\
            '\t7\n'\
            'Delivery #2\n'\
            '\t36\n'\
            'Delivery #3\n'\
            '\t47, 58\n'\
            'Enter the ID of the delivery you want to select:\n'\
            '(B to go back)\n'

        self.assertEqual(select_delivery.prompt, expected)        

        # do match
        select_delivery.user_choice = 1
        self.assertTrue(select_delivery.match_check())
        self.assertEqual(select_delivery.get_index(), 0)

        select_delivery.user_choice = 2
        self.assertTrue(select_delivery.match_check())
        self.assertEqual(select_delivery.get_index(), 1)

        select_delivery.user_choice = 3
        self.assertTrue(select_delivery.match_check())
        self.assertEqual(select_delivery.get_index(), 2)

        select_delivery.user_choice = 'b'
        self.assertTrue(select_delivery.match_check())

        select_delivery.user_choice = 'B'
        self.assertTrue(select_delivery.match_check())

        # doesn't match
        select_delivery.user_choice = 0
        self.assertFalse(select_delivery.match_check())

        select_delivery.user_choice = 4
        self.assertFalse(select_delivery.match_check())

        select_delivery.user_choice = 5
        self.assertFalse(select_delivery.match_check())

        select_delivery.user_choice = 6
        self.assertFalse(select_delivery.match_check())

        select_delivery.user_choice = 'a'
        self.assertFalse(select_delivery.match_check())

        select_delivery.user_choice = 'A'
        self.assertFalse(select_delivery.match_check())

        select_delivery.user_choice = 'n'
        self.assertFalse(select_delivery.match_check())

        select_delivery.user_choice = 'N'
        self.assertFalse(select_delivery.match_check())

        select_delivery.user_choice = 'z'
        self.assertFalse(select_delivery.match_check())

        select_delivery.user_choice = 'Z'
        self.assertFalse(select_delivery.match_check())

    def test_select_order(self):
        from processes.select import Select_Order

        # delivery 1
        select_order = Select_Order(self.shift.deliveries[0], test=True)

        # check build_prompt
        select_order.build_prompt()
        expected =\
            'Order IDs:\n'\
            '7\n'\
            'Enter an above ID to select an order:\n'\
            '(B to go back)\n'
        
        self.assertEqual(select_order.prompt, expected)

        # do match
        select_order.user_choice = 7
        self.assertTrue(select_order.match_check())
        self.assertEqual(select_order.get_index(), 0)
        select_order.user_choice = 'b'
        self.assertTrue(select_order.match_check())
        select_order.user_choice = 'B'
        self.assertTrue(select_order.match_check())

        # doen't match
        select_order.user_choice = 3
        self.assertFalse(select_order.match_check())
        select_order.user_choice = 113
        self.assertFalse(select_order.match_check())
        select_order.user_choice = 'a'
        self.assertFalse(select_order.match_check())
        select_order.user_choice = 'A'
        self.assertFalse(select_order.match_check())
        select_order.user_choice = 'n'
        self.assertFalse(select_order.match_check())
        select_order.user_choice = 'N'
        self.assertFalse(select_order.match_check())
        select_order.user_choice = 'z'
        self.assertFalse(select_order.match_check())
        select_order.user_choice = 'Z'
        self.assertFalse(select_order.match_check())

        # delivery 2
        select_order = Select_Order(self.shift.deliveries[1], test=True)

        # check build_prompt
        select_order.build_prompt()
        expected =\
            'Order IDs:\n'\
            '36\n'\
            'Enter an above ID to select an order:\n'\
            '(B to go back)\n'
        
        self.assertEqual(select_order.prompt, expected)

        # do match
        select_order.user_choice = 36
        self.assertTrue(select_order.match_check())
        self.assertEqual(select_order.get_index(), 0)
        select_order.user_choice = 'b'
        self.assertTrue(select_order.match_check())
        select_order.user_choice = 'B'
        self.assertTrue(select_order.match_check())

        # doen't match
        select_order.user_choice = 3
        self.assertFalse(select_order.match_check())
        select_order.user_choice = 113
        self.assertFalse(select_order.match_check())
        select_order.user_choice = 'a'
        self.assertFalse(select_order.match_check())
        select_order.user_choice = 'A'
        self.assertFalse(select_order.match_check())
        select_order.user_choice = 'n'
        self.assertFalse(select_order.match_check())
        select_order.user_choice = 'N'
        self.assertFalse(select_order.match_check())
        select_order.user_choice = 'z'
        self.assertFalse(select_order.match_check())
        select_order.user_choice = 'Z'
        self.assertFalse(select_order.match_check())

        # delivery 3
        select_order = Select_Order(self.shift.deliveries[2], test=True)

        # check build_prompt
        select_order.build_prompt()
        expected =\
            'Order IDs:\n'\
            '47\n'\
            '58\n'\
            'Enter an above ID to select an order:\n'\
            '(B to go back)\n'
        
        self.assertEqual(select_order.prompt, expected)

        # do match
        select_order.user_choice = 47
        self.assertTrue(select_order.match_check())
        self.assertEqual(select_order.get_index(), 0)
        select_order.user_choice = 58
        self.assertTrue(select_order.match_check())
        self.assertEqual(select_order.get_index(), 1)
        select_order.user_choice = 'b'
        self.assertTrue(select_order.match_check())
        select_order.user_choice = 'B'
        self.assertTrue(select_order.match_check())

        # doen't match
        select_order.user_choice = 3
        self.assertFalse(select_order.match_check())
        select_order.user_choice = 113
        self.assertFalse(select_order.match_check())
        select_order.user_choice = 'a'
        self.assertFalse(select_order.match_check())
        select_order.user_choice = 'A'
        self.assertFalse(select_order.match_check())
        select_order.user_choice = 'n'
        self.assertFalse(select_order.match_check())
        select_order.user_choice = 'N'
        self.assertFalse(select_order.match_check())
        select_order.user_choice = 'z'
        self.assertFalse(select_order.match_check())
        select_order.user_choice = 'Z'
        self.assertFalse(select_order.match_check())

    def test_quick_select_order(self):
        from processes.select import Quick_Select_Order

        select_order = Quick_Select_Order(self.shift, test=True)

        # does match
        select_order.user_choice = 7
        self.assertTrue(select_order.match_check())
        self.assertEqual(select_order.get_delivery_id(), 0)
        self.assertEqual(select_order.get_order_index(), 0)
        select_order.user_choice = 36
        self.assertTrue(select_order.match_check())
        self.assertEqual(select_order.get_delivery_id(), 1)
        self.assertEqual(select_order.get_order_index(), 0)
        select_order.user_choice = 47
        self.assertTrue(select_order.match_check())
        self.assertEqual(select_order.get_delivery_id(), 2)
        self.assertEqual(select_order.get_order_index(), 0)
        select_order.user_choice = 58
        self.assertTrue(select_order.match_check())
        self.assertEqual(select_order.get_delivery_id(), 2)
        self.assertEqual(select_order.get_order_index(), 1)
        select_order.user_choice = 'b'
        self.assertTrue(select_order.match_check())
        select_order.user_choice = 'B'
        self.assertTrue(select_order.match_check())

        # doesn't match
        select_order.user_choice = 3
        self.assertFalse(select_order.match_check())
        select_order.user_choice = 39
        self.assertFalse(select_order.match_check())
        select_order.user_choice = 113
        self.assertFalse(select_order.match_check())
        select_order.user_choice = 'a'
        self.assertFalse(select_order.match_check())
        select_order.user_choice = 'A'
        self.assertFalse(select_order.match_check())
        select_order.user_choice = 'n'
        self.assertFalse(select_order.match_check())
        select_order.user_choice = 'N'
        self.assertFalse(select_order.match_check())
        select_order.user_choice = 'z'
        self.assertFalse(select_order.match_check())
        select_order.user_choice = 'Z'
        self.assertFalse(select_order.match_check())

    def test_select_carry_out_tip(self):
        from processes.select import Select_Carry_Out_Tip

        select_carry_out_tip = Select_Carry_Out_Tip(self.shift, test=True)

        # check build_prompt
        select_carry_out_tip.build_prompt()
        expected =\
            'Carry out tips:\n'\
            '\t1. Card: $3.11\n'\
            '\t2. Cash: $2.71\n'\
            'Enter a number to select a tip:\n'\
            '(B to go back)\n'
        self.assertEqual(select_carry_out_tip.prompt, expected)

        # does match
        select_carry_out_tip.user_choice = 1
        self.assertTrue(select_carry_out_tip.match_check())
        self.assertEqual(select_carry_out_tip.get_index(), 0)
        select_carry_out_tip.user_choice = 2
        self.assertTrue(select_carry_out_tip.match_check())
        self.assertEqual(select_carry_out_tip.get_index(), 1)
        select_carry_out_tip.user_choice = 'b'
        self.assertTrue(select_carry_out_tip.match_check())
        select_carry_out_tip.user_choice = 'B'
        self.assertTrue(select_carry_out_tip.match_check())

        # doesn't match
        select_carry_out_tip.user_choice = 0
        self.assertFalse(select_carry_out_tip.match_check())
        select_carry_out_tip.user_choice = 3
        self.assertFalse(select_carry_out_tip.match_check())
        select_carry_out_tip.user_choice = 4
        self.assertFalse(select_carry_out_tip.match_check())
        select_carry_out_tip.user_choice = 'a'
        self.assertFalse(select_carry_out_tip.match_check())
        select_carry_out_tip.user_choice = 'A'
        self.assertFalse(select_carry_out_tip.match_check())
        select_carry_out_tip.user_choice = 'n'
        self.assertFalse(select_carry_out_tip.match_check())
        select_carry_out_tip.user_choice = 'N'
        self.assertFalse(select_carry_out_tip.match_check())
        select_carry_out_tip.user_choice = 'z'
        self.assertFalse(select_carry_out_tip.match_check())
        select_carry_out_tip.user_choice = 'Z'
        self.assertFalse(select_carry_out_tip.match_check())

    def test_select_extra_stop_shift(self):
        from processes.select import Select_Extra_Stop

        select_extra_stop = Select_Extra_Stop(self.shift, test=True)

        # check build_prompt
        select_extra_stop.build_prompt()
        expected =\
            'Extra Stops:\n'\
            f'Extra stop #1, Location: bank\n'\
            f'Extra stop #2, Location: mongolian grill\n'\
            'Enter an ID number to select an extra stop:\n'\
            '(B to go back)\n'
        self.assertEqual(select_extra_stop.prompt, expected)

        # does match
        select_extra_stop.user_choice = 1
        self.assertTrue(select_extra_stop.match_check())
        self.assertEqual(select_extra_stop.get_index(), 0)
        select_extra_stop.user_choice = 2
        self.assertTrue(select_extra_stop.match_check())
        self.assertEqual(select_extra_stop.get_index(), 1)
        select_extra_stop.user_choice = 'b'
        self.assertTrue(select_extra_stop.match_check())
        select_extra_stop.user_choice = 'B'
        self.assertTrue(select_extra_stop.match_check())


        # doesn't match
        select_extra_stop.user_choice = 0
        self.assertFalse(select_extra_stop.match_check())
        select_extra_stop.user_choice = 3
        self.assertFalse(select_extra_stop.match_check())
        select_extra_stop.user_choice = 4
        self.assertFalse(select_extra_stop.match_check())
        select_extra_stop.user_choice = 'a'
        self.assertFalse(select_extra_stop.match_check())
        select_extra_stop.user_choice = 'A'
        self.assertFalse(select_extra_stop.match_check())
        select_extra_stop.user_choice = 'n'
        self.assertFalse(select_extra_stop.match_check())
        select_extra_stop.user_choice = 'N'
        self.assertFalse(select_extra_stop.match_check())
        select_extra_stop.user_choice = 'z'
        self.assertFalse(select_extra_stop.match_check())
        select_extra_stop.user_choice = 'Z'
        self.assertFalse(select_extra_stop.match_check())

    def test_select_extra_stop_delivery(self):
        from processes.select import Select_Extra_Stop

        select_extra_stop = Select_Extra_Stop(self.shift.deliveries[1], test=True)

        # check build_prompt
        select_extra_stop.build_prompt()
        expected =\
            'Extra Stops:\n'\
            f'Extra stop #1, Location: mongolian grill\n'\
            'Enter an ID number to select an extra stop:\n'\
            '(B to go back)\n'
        self.assertEqual(select_extra_stop.prompt, expected)

        # does match
        select_extra_stop.user_choice = 1
        self.assertTrue(select_extra_stop.match_check())
        self.assertEqual(select_extra_stop.get_index(), 0)
        select_extra_stop.user_choice = 'b'
        self.assertTrue(select_extra_stop.match_check())
        select_extra_stop.user_choice = 'B'
        self.assertTrue(select_extra_stop.match_check())

        # doesn't match
        select_extra_stop.user_choice = 0
        self.assertFalse(select_extra_stop.match_check())
        select_extra_stop.user_choice = 3
        self.assertFalse(select_extra_stop.match_check())
        select_extra_stop.user_choice = 4
        self.assertFalse(select_extra_stop.match_check())
        select_extra_stop.user_choice = 'a'
        self.assertFalse(select_extra_stop.match_check())
        select_extra_stop.user_choice = 'A'
        self.assertFalse(select_extra_stop.match_check())
        select_extra_stop.user_choice = 'n'
        self.assertFalse(select_extra_stop.match_check())
        select_extra_stop.user_choice = 'N'
        self.assertFalse(select_extra_stop.match_check())
        select_extra_stop.user_choice = 'z'
        self.assertFalse(select_extra_stop.match_check())
        select_extra_stop.user_choice = 'Z'
        self.assertFalse(select_extra_stop.match_check())
