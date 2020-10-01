import unittest

class Test_User_Input(unittest.TestCase):
    def test_check_confirm(self):
        from utility.user_input import check_confirm

        # true
        self.assertTrue(check_confirm('y'))
        self.assertTrue(check_confirm('Y'))
        # false
        self.assertFalse(check_confirm('n'))
        self.assertFalse(check_confirm('N'))
        # raise errors
        with self.assertRaises(TypeError):
            check_confirm(1.5)
            check_confirm(7)
            check_confirm([x for x in range(5)])
            check_confirm(None)
    
    def test_check_decimal(self):
        from utility.user_input import check_decimal

        # true
        self.assertTrue(check_decimal('7'))
        self.assertTrue(check_decimal('63'))
        self.assertTrue(check_decimal('294'))
        self.assertTrue(check_decimal('8.9'))
        self.assertTrue(check_decimal('37.4'))
        self.assertTrue(check_decimal('384.8'))

        # false
        self.assertFalse(check_decimal('hello world'))
        self.assertFalse(check_decimal('this is a test'))
        self.assertFalse(check_decimal('these should return false'))

        # raise type error
        with self.assertRaises(TypeError):
            check_decimal(63)
            check_decimal(37.4)
            check_decimal([x for x in range(5)])
            check_decimal(None)

    def test_check_integer(self):
        from utility.user_input import check_integer

        # true
        self.assertTrue(check_integer('7'))
        self.assertTrue(check_integer('63'))
        self.assertTrue(check_integer('294'))

        # false
        self.assertFalse(check_integer('8.9'))
        self.assertFalse(check_integer('37.4'))
        self.assertFalse(check_integer('384.8'))
        self.assertFalse(check_integer('hello world'))
        self.assertFalse(check_integer('this is a test'))
        self.assertFalse(check_integer('these should return false'))

        # raise type error
        with self.assertRaises(TypeError):
            check_integer(63)
            check_integer(37.4)
            check_integer([x for x in range(5)])
            check_integer(None)

    def test_check_text(self):
        from utility.user_input import check_text

        # true
        self.assertTrue(check_text('hello'))
        self.assertTrue(check_text('hello world', spaces=True))
        self.assertTrue(check_text('hello, world/earth & mars', spaces=True, symbols=',&/'))

        # false
        self.assertFalse(check_text('hello world'))
        self.assertFalse(check_text('hello, world/earth & mars'))
