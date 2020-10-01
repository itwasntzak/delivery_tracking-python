import unittest

class Test_Utility(unittest.TestCase):
    def test_add_newlines(self):
        from utility.utility import add_newlines

        string = 'hello world'
        result = add_newlines(string)
        self.assertEqual(result, '\nhello world\n')

        string = '\nhello world'
        result = add_newlines(string)
        self.assertEqual(result, '\nhello world\n')

        string = 'hello world\n'
        result = add_newlines(string)
        self.assertEqual(result, '\nhello world\n')

    def test_prep_data_string(self):
        from utility.utility import prep_data_string

        data = 3.28
        result = prep_data_string(data, '$', ' card tip')
        self.assertEqual(result, '$3.28 card tip')

        data = 2.8
        result = prep_data_string(data, after=' miles traveled')
        self.assertEqual(result, '2.8 miles traveled')

        data = '07:50:16'
        result = prep_data_string(data, 'The time is ')
        self.assertEqual(result, 'The time is 07:50:16')

        with self.assertRaises(ValueError):
            prep_data_string(7.5)

    def test_to_datetime_from_date(self):
        from datetime import datetime
        from utility.utility import To_Datetime

        string = '2020-09-07'
        result = To_Datetime(string).from_date()
        self.assertIsInstance(result, datetime)

        string = '2020-01-30'
        result = To_Datetime(string).from_date()
        self.assertIsInstance(result, datetime)

        string = '2020-11-13'
        result = To_Datetime(string).from_date()
        self.assertIsInstance(result, datetime)

    def test_to_datetime_from_datetime(self):
        from utility.utility import To_Datetime
        from datetime import datetime

        string = '2020-09-07 09:13:27.73218'
        result = To_Datetime(string).from_datetime()
        self.assertIsInstance(result, datetime)

        string = '2020-09-07 09:13:27.000'
        result = To_Datetime(string).from_datetime()
        self.assertIsInstance(result, datetime)

        string = '2020-09-07 09:13:27'
        result = To_Datetime(string).from_datetime()
        self.assertIsInstance(result, datetime)

    def test_to_datetime_from_time(self):
        from utility.utility import To_Datetime
        from datetime import datetime

        string = '09:13:27.73218'
        result = To_Datetime(string).from_time()
        self.assertIsInstance(result, datetime)

        string = '09:13:27.000'
        result = To_Datetime(string).from_time()
        self.assertIsInstance(result, datetime)

        string = '09:13:27'
        result = To_Datetime(string).from_time()
        self.assertIsInstance(result, datetime)

    def test_to_money(self):
        from utility.utility import to_money

        value = 0
        result = to_money(value)
        self.assertEqual(result, '$0.00')

        value = 7
        result = to_money(value)
        self.assertEqual(result, '$7.00')

        value = 2.7
        result = to_money(value)
        self.assertEqual(result, '$2.70')

        value = 3.9831273
        result = to_money(value)
        self.assertEqual(result, '$3.98')
