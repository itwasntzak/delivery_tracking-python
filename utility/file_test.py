import unittest

class Test_File(unittest.TestCase):
    def test_save(self):
        from os import path, remove
        from utility.file import save

        test_file = 'test_file.txt'
        self.assertFalse(path.exists(test_file))

        # test file doesnt exist with separator
        data = 0
        save(data, test_file, ',')
        self.assertTrue(path.exists(test_file))

        with open(test_file, 'r') as file:
            self.assertEqual(file.read(), '0')

        # test file exist with separator
        data = 27
        save(data, test_file, ',')

        with open(test_file, 'r') as file:
            self.assertEqual(file.read(), '0,27')

        # test file exist but no separator
        data = 42
        save(data, test_file)
        self.assertTrue(path.exists(test_file))

        with open(test_file, 'r') as file:
            self.assertEqual(file.read(), '42')

        remove(test_file)

    def test_read_integer(self):
        from os import remove
        from utility.file import Read

        test_file = 'test_file.txt'

        # test single item
        string = '35'

        with open(test_file, 'w') as file:
            file.write(string)
        
        expected = 35
        result = Read(test_file).integer()

        self.assertEqual(result, expected)

        # test multi items
        string = '0,1,2,3,4,5'

        with open(test_file, 'w') as file:
            file.write(string)
        
        expected = [0, 1, 2, 3, 4, 5]
        result = Read(test_file).integer()

        self.assertListEqual(result, expected)

        remove(test_file)

    def test_read_decimal(self):
        from os import remove
        from utility.file import Read

        test_file = 'test_file.txt'

        # test single item
        string = '3.5'

        with open(test_file, 'w') as file:
            file.write(string)
        
        expected = 3.5
        result = Read(test_file).decimal()

        self.assertEqual(result, expected)

        # test multi items
        string = '2.3,4.7,3.6,5.9'

        with open(test_file, 'w') as file:
            file.write(string)
        
        expected = [2.3, 4.7, 3.6, 5.9]
        result = Read(test_file).decimal()

        self.assertListEqual(result, expected)

        remove(test_file)
