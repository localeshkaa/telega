import unittest


class Testing(unittest.TestCase):
    def test_string(self):
        a = 'some'
        b = 'some'
        if self.assertEqual(a, b):
            print("Yeah! It's all good 1")
        else:
            print("You died 1")
        return self.assertEqual(a, b)


    def test_boolean(self):
        a = True
        b = True
        self.assertEqual(a, b)
        if self.assertEqual(a, b):
            print("Yeah! It's all good 2")
        else:
            print("You died 2")
        return self.assertEqual(a, b)

if __name__ == '__main__':
    unittest.main()
