import unittest
from Simple_Calculator import Calculator

#A series of tests designed to see if the functions fail
class ArithTest (unittest.TestCase):
    def setUp(self) :
        self.cal = Calculator()

    def runTest (self):

        self.failUnless(self.cal.add(1, 2) == 3, msg='1+2 = 3 failed')

        self.failIf(self.cal.divide(10, 2) == 3, msg='10/2 = 3 fail test failed')






def suite():

    suite = unittest.TestSuite()

    suite.addTest (ArithTest())

    return suite





if __name__ == '__main__':

    runner = unittest.TextTestRunner()

    test_suite = suite()

    runner.run (test_suite)