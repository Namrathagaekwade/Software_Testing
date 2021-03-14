import unittest
from Simple_Calculator import Calculator

#A series of tests designed to see if the functions fail
class ArithTest_integration (unittest.TestCase):
    def setUp(self):
        self.cal = Calculator()

    def runTest (self):


        self.assertEqual(self.cal.add(self.cal.multiply(1,1), self.cal.subtract(3,1)) , 3)

        self.assertEqual(self.cal.divide(self.cal.multiply(2,5), self.cal.add(1,1)) , 5)

        self.assertEqual(self.cal.multiply(self.cal.subtract(4,2), self.cal.divide(4,2)), 4)

        self.assertEqual(self.cal.subtract(self.cal.add(6,7), self.cal.divide(self.cal.multiply(6,2),2)) , 7)


def suite():

    suite = unittest.TestSuite()

    suite.addTest (ArithTest_integration())

    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()

    test_suite = suite()

    runner.run (test_suite)