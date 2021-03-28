import unittest
from Simple_Calculator import Calculator

#A series of tests designed to see if the functions fail
class ArithTest (unittest.TestCase):
    def setUp(self) :
        self.cal = Calculator()

    def runTest (self):

        self.assertEqual(self.cal.add(1, 1), 3, msg='1+2 = 3 failed')
        self.failIf(self.cal.divide(10, 2) == 3, msg='10/2 = 3 fail test failed')
        self.failUnlessEqual(self.cal.multiply(2, 2), 4, msg='2 * 2 failed')
        self.assertTrue(self.cal.subtract(13, 5) == 7, msg='13 - 6 failed')
        self.assertTrue(self.cal.multiply(5, 4) == 25, msg='5 * 5 failed')
        self.assertEqual(self.cal.add(10, 10), 25, msg='10 + 15 = 25 failed')
        self.assertEqual(self.cal.divide(50, 15), 5, msg='50 / 10 failed')
        self.assertFalse(self.cal.subtract(20, 5) == 14, msg='20 - 5 = 14 fail test failed')
        self.assertEqual(self.cal.divide(5,1), 1)

def suite():

    suite = unittest.TestSuite()

    suite.addTest (ArithTest())

    return suite





if __name__ == '__main__':

    runner = unittest.TextTestRunner()

    test_suite = suite()

    runner.run (test_suite)