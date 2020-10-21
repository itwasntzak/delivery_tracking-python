import unittest

class Test_Menus(unittest.TestCase):
    # def test_delivery_tracking_menu_match_check(self):
    #     from testing_tools import completed_shift
    #     from menus import Delivery_Tracking_Menu

    #     test = Delivery_Tracking_Menu(completed_shift().deliveries[0], test=True)

    #     # correct user choice
    #     test.user_choice = 'o'
    #     self.assertTrue(test.match_check())
    #     test.user_choice = 'O'
    #     self.assertTrue(test.match_check())
    #     test.user_choice = 'e'
    #     self.assertTrue(test.match_check())
    #     test.user_choice = 'E'
    #     self.assertTrue(test.match_check())
    #     test.user_choice = 'c'
    #     self.assertTrue(test.match_check())
    #     test.user_choice = 'C'
    #     self.assertTrue(test.match_check())
    #     test.user_choice = 'v'
    #     self.assertTrue(test.match_check())
    #     test.user_choice = 'V'
    #     self.assertTrue(test.match_check())
    #     test.user_choice = 'r'
    #     self.assertTrue(test.match_check())
    #     test.user_choice = 'R'
    #     self.assertTrue(test.match_check())
    #     test.user_choice = 'b'
    #     self.assertTrue(test.match_check())
    #     test.user_choice = 'B'
    #     self.assertTrue(test.match_check())

    #     # incorrect user choice
    #     test.user_choice = 'a'
    #     self.assertFalse(test.match_check())
    #     test.user_choice = 'A'
    #     self.assertFalse(test.match_check())
    #     test.user_choice = 'n'
    #     self.assertFalse(test.match_check())
    #     test.user_choice = 'N'
    #     self.assertFalse(test.match_check())
    #     test.user_choice = 'z'
    #     self.assertFalse(test.match_check())
    #     test.user_choice = 'Z'
    #     self.assertFalse(test.match_check())
    #     test.user_choice = '1'
    #     self.assertFalse(test.match_check())
    #     test.user_choice = '43.7'
    #     self.assertFalse(test.match_check())
    #     test.user_choice = 'hello'
    #     self.assertFalse(test.match_check())
    #     test.user_choice = 'oo'
    #     self.assertFalse(test.match_check())
    #     test.user_choice = 'oe'
    #     self.assertFalse(test.match_check())
    #     test.user_choice = 'oec'
    #     self.assertFalse(test.match_check())

    def test_delivery_tracking_menu_build_prompt(self):
        from menus import Delivery_Tracking_Menu
        from testing_tools import completed_shift
        from os import mkdir, rmdir, path

        shift = completed_shift()
        delivery = shift.deliveries[1]
        test = Delivery_Tracking_Menu(delivery, test=True)

        # directories dont exist
        expected =\
            '\n- Delivery Menu -\n'\
            'Please select an option:\n'\
            'O. Add new order\n'\
            'E. Take extra stop\n'\
            'C. Complete current delivery\n'\
            'V. View current delivery\n'\
            'R. Revise current delivery\n'\
            'B. Back a menu\n'
        test.build_prompt()
        self.assertEqual(test.prompt, expected)

        # make directories
        mkdir('data')
        mkdir(path.join('data', 'shifts'))
        mkdir(shift.file_list()['directory'])
        mkdir(delivery.file_list()['directory'])
        mkdir(delivery.orders[0].file_list()['directory'])
        mkdir(delivery.extra_stops[0].file_list()['directory'])

        # directories do exist
        expected =\
            '\n- Delivery Menu -\n'\
            'Please select an option:\n'\
            'O. Continue entering order\n'\
            'E. Continue extra stop\n'\
            'C. Complete current delivery\n'\
            'V. View current delivery\n'\
            'R. Revise current delivery\n'\
            'B. Back a menu\n'
        test.build_prompt()
        self.assertEqual(test.prompt, expected)

        # remove directories
        rmdir(delivery.extra_stops[0].file_list()['directory'])
        rmdir(delivery.orders[0].file_list()['directory'])
        rmdir(delivery.file_list()['directory'])
        rmdir(shift.file_list()['directory'])
        rmdir(path.join('data', 'shifts'))
        rmdir('data')

    def test_delivery_tracking_menu_build_confirmation_text(self):
        from menus import Delivery_Tracking_Menu
        from testing_tools import completed_shift
        from os import mkdir, rmdir, path

        shift = completed_shift()
        delivery = shift.deliveries[1]
        test = Delivery_Tracking_Menu(delivery, test=True)

        test.user_choice = 'o'
        expected = 'Add new order\n'
        test.build_confirmation_text()
        self.assertEqual(test.confirmation_text, expected)

        test.user_choice = 'e'
        expected = 'Take extra stop\n'
        test.build_confirmation_text()
        self.assertEqual(test.confirmation_text, expected)

        test.user_choice = 'c'
        expected = 'Complete current delivery\n'
        test.build_confirmation_text()
        self.assertEqual(test.confirmation_text, expected)

        test.user_choice = 'r'
        expected = 'Revise current delivery\n'
        test.build_confirmation_text()
        self.assertEqual(test.confirmation_text, expected)

        # make directories
        mkdir('data')
        mkdir(path.join('data', 'shifts'))
        mkdir(shift.file_list()['directory'])
        mkdir(delivery.file_list()['directory'])
        mkdir(delivery.orders[0].file_list()['directory'])
        mkdir(delivery.extra_stops[0].file_list()['directory'])

        test.user_choice = 'o'
        expected = 'Continue entering order\n'
        test.build_confirmation_text()
        self.assertEqual(test.confirmation_text, expected)

        test.user_choice = 'e'
        expected = 'Continue extra stop\n'
        test.build_confirmation_text()
        self.assertEqual(test.confirmation_text, expected)

        # remove directories
        rmdir(delivery.extra_stops[0].file_list()['directory'])
        rmdir(delivery.orders[0].file_list()['directory'])
        rmdir(delivery.file_list()['directory'])
        rmdir(shift.file_list()['directory'])
        rmdir(path.join('data', 'shifts'))
        rmdir('data')

    # def test_shift_tracking_menu_match_check(self):
    #     from testing_tools import completed_shift
    #     from menus import Shift_Tracking_Menu

    #     test = Shift_Tracking_Menu(completed_shift(), test=True)

    #     # correct user choice
    #     test.user_choice = 'd'
    #     self.assertTrue(test.match_check())
    #     test.user_choice = 'D'
    #     self.assertTrue(test.match_check())
    #     test.user_choice = 'e'
    #     self.assertTrue(test.match_check())
    #     test.user_choice = 'E'
    #     self.assertTrue(test.match_check())
    #     test.user_choice = 'c'
    #     self.assertTrue(test.match_check())
    #     test.user_choice = 'C'
    #     self.assertTrue(test.match_check())
    #     test.user_choice = 's'
    #     self.assertTrue(test.match_check())
    #     test.user_choice = 'S'
    #     self.assertTrue(test.match_check())
    #     test.user_choice = 'x'
    #     self.assertTrue(test.match_check())
    #     test.user_choice = 'X'
    #     self.assertTrue(test.match_check())
    #     test.user_choice = 'v'
    #     self.assertTrue(test.match_check())
    #     test.user_choice = 'V'
    #     self.assertTrue(test.match_check())
    #     test.user_choice = 'q'
    #     self.assertTrue(test.match_check())
    #     test.user_choice = 'Q'
    #     self.assertTrue(test.match_check())

    #     # incorrect user choice
    #     test.user_choice = 'a'
    #     self.assertFalse(test.match_check())
    #     test.user_choice = 'A'
    #     self.assertFalse(test.match_check())
    #     test.user_choice = 'n'
    #     self.assertFalse(test.match_check())
    #     test.user_choice = 'N'
    #     self.assertFalse(test.match_check())
    #     test.user_choice = 'z'
    #     self.assertFalse(test.match_check())
    #     test.user_choice = 'Z'
    #     self.assertFalse(test.match_check())
    #     test.user_choice = '1'
    #     self.assertFalse(test.match_check())
    #     test.user_choice = '43.7'
    #     self.assertFalse(test.match_check())
    #     test.user_choice = 'hello'
    #     self.assertFalse(test.match_check())
    #     test.user_choice = 'dd'
    #     self.assertFalse(test.match_check())
    #     test.user_choice = 'de'
    #     self.assertFalse(test.match_check())
    #     test.user_choice = 'dec'
    #     self.assertFalse(test.match_check())

    def test_shift_tracking_menu_build_prompt(self):
        from menus import Shift_Tracking_Menu
        from testing_tools import completed_shift
        from objects import Delivery
        from os import mkdir, rmdir, remove, path

        shift = completed_shift()
        delivery = Delivery(shift)
        test = Shift_Tracking_Menu(shift, test=True)

        # directories dont exist
        expected =\
            '\n- Shift Menu -\n'\
            'Please select an option:\n'\
            'D. Start delivery\n'\
            'E. Start extra stop\n'\
            'C. Enter carry out tip\n'\
            'S. Start split\n'\
            'X. End shift\n'\
            'V. View shift\n'\
            'Q. Quit program\n'
        test.build_prompt()
        self.assertEqual(test.prompt, expected)

        # make directories
        mkdir('data')
        mkdir(path.join('data', 'shifts'))
        mkdir(shift.file_list()['directory'])
        mkdir(delivery.file_list()['directory'])
        mkdir(shift.extra_stops[0].file_list()['directory'])
        mkdir(shift.split.file_list()['directory'])
        with open(shift.file_list()['end_time'], 'w') as file:
            file.write('')

        # directories do exist
        expected =\
            '\n- Shift Menu -\n'\
            'Please select an option:\n'\
            'D. Continue delivery\n'\
            'E. Continue extra stop\n'\
            'C. Enter carry out tip\n'\
            'S. End split\n'\
            'X. Continue ending shift\n'\
            'V. View shift\n'\
            'Q. Quit program\n'
        test.build_prompt()
        self.assertEqual(test.prompt, expected)

        # remove directories
        remove(shift.file_list()['end_time'])
        rmdir(shift.split.file_list()['directory'])
        rmdir(shift.extra_stops[0].file_list()['directory'])
        rmdir(delivery.file_list()['directory'])
        rmdir(shift.file_list()['directory'])
        rmdir(path.join('data', 'shifts'))
        rmdir('data')

    def test_shift_tracking_menu_build_confirmation_text(self):
        from menus import Shift_Tracking_Menu
        from testing_tools import completed_shift
        from objects import Delivery
        from os import mkdir, rmdir, remove, path

        shift = completed_shift()
        delivery = Delivery(shift)
        test = Shift_Tracking_Menu(shift, test=True)

        test.user_choice = 'd'
        expected = 'Start delivery\n'
        test.build_confirmation_text()
        self.assertEqual(test.confirmation_text, expected)

        test.user_choice = 'e'
        expected = 'Start extra stop\n'
        test.build_confirmation_text()
        self.assertEqual(test.confirmation_text, expected)

        test.user_choice = 'c'
        expected = 'Enter carry out tip\n'
        test.build_confirmation_text()
        self.assertEqual(test.confirmation_text, expected)

        test.user_choice = 's'
        expected = 'Start split\n'
        test.build_confirmation_text()
        self.assertEqual(test.confirmation_text, expected)

        test.user_choice = 'x'
        expected = 'End shift\n'
        test.build_confirmation_text()
        self.assertEqual(test.confirmation_text, expected)

        # make directories
        mkdir('data')
        mkdir(path.join('data', 'shifts'))
        mkdir(shift.file_list()['directory'])
        mkdir(delivery.file_list()['directory'])
        mkdir(shift.extra_stops[0].file_list()['directory'])
        mkdir(shift.split.file_list()['directory'])
        with open(shift.file_list()['end_time'], 'w') as file:
            file.write('')

        test.user_choice = 'd'
        expected = 'Continue delivery\n'
        test.build_confirmation_text()
        self.assertEqual(test.confirmation_text, expected)

        test.user_choice = 'e'
        expected = 'Continue extra stop\n'
        test.build_confirmation_text()
        self.assertEqual(test.confirmation_text, expected)

        test.user_choice = 's'
        expected = 'End split\n'
        test.build_confirmation_text()
        self.assertEqual(test.confirmation_text, expected)

        test.user_choice = 'x'
        expected = 'Continue ending shift\n'
        test.build_confirmation_text()
        self.assertEqual(test.confirmation_text, expected)

        # remove directories
        remove(shift.file_list()['end_time'])
        rmdir(shift.split.file_list()['directory'])
        rmdir(shift.extra_stops[0].file_list()['directory'])
        rmdir(delivery.file_list()['directory'])
        rmdir(shift.file_list()['directory'])
        rmdir(path.join('data', 'shifts'))
        rmdir('data')

    def test_completed_shift_overwrite_shift(self):
        # this test can be greately improved because right now its only testing
        #   against one file rather then an entire shift's files
        # this test is also poor because the completed ids file will only work for short time frame

        from menus import Completed_Shift
        from testing_tools import completed_shift
        from utility.utility import now
        from os import mkdir, path, remove, rmdir

        shift = completed_shift()

        # create directories and files
        mkdir('data')
        mkdir(path.join('data', 'shifts'))
        mkdir(shift.file_list()['directory'])
        with open(shift.file_list()['info'], 'w') as file:
            file.write(shift.csv())
        with open(shift.file_list()['completed_ids'], 'w') as file:
            file.write('2020-09-12,2020-09-14,2020-09-18,2020-09-19,2020-09-20')
        
        # run method
        test = Completed_Shift(shift, test=True).overwrite_shift()

        # check that method did what its supposed to
        self.assertFalse(path.exists(shift.file_list()['info']))
        self.assertTrue(path.exists(shift.file_list()['start_time']))
        self.assertNotEqual(test.shift.start_time, shift.start_time)

        # delete directories and files
        remove(shift.file_list()['start_time'])
        remove(shift.file_list()['completed_ids'])
        rmdir(shift.file_list()['directory'])
        rmdir(path.join('data', 'shifts'))
        rmdir('data')

    def test_completed_shift_resume_shift(self):
        # this test can be greately improved because right now its only testing
        #   against one file rather then an entire shift's files
        # this test is also poor because the completed ids file will only work for short time frame

        from menus import Completed_Shift
        from testing_tools import completed_shift
        from utility.utility import now
        from os import mkdir, path, remove, rmdir

        shift = completed_shift()

        # create directories and files
        mkdir('data')
        mkdir(path.join('data', 'shifts'))
        mkdir(shift.file_list()['directory'])
        with open(shift.file_list()['info'], 'w') as file:
            file.write(shift.csv())
        with open(shift.file_list()['completed_ids'], 'w') as file:
            file.write('2020-09-12,2020-09-14,2020-09-18,2020-09-19,2020-09-20')
        
        # run method
        test = Completed_Shift(shift, test=True).resume_shift()

        # check that method did what its supposed to
        self.assertFalse(path.exists(shift.file_list()['info']))
        self.assertTrue(path.exists(shift.file_list()['start_time']))
        self.assertEqual(test.shift.start_time, shift.start_time)

        # delete directories and files
        remove(shift.file_list()['start_time'])
        remove(shift.file_list()['completed_ids'])
        rmdir(shift.file_list()['directory'])
        rmdir(path.join('data', 'shifts'))
        rmdir('data')
