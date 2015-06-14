__author__ = 'demathieu'

import lex
import unittest


def getToken(string):
    temp = string.split(',')
    temp2 = temp[0]
    return(temp2[9:])

def getString(string):
    temp = string.split(',')
    temp2 = temp[1]
    return temp2.replace("'", "")

class ParametrizedTestCase(unittest.TestCase):
    """ TestCase classes that want to be parametrized should
        inherit from this class.
    """
    def __init__(self, methodName='runTest', param=None):
        super(ParametrizedTestCase, self).__init__(methodName)
        self.param = param

    @staticmethod
    def parametrize(testcase_klass, param=None):
        """ Create a suite containing all tests taken from the given
            subclass, passing them the parameter 'param'.
        """
        testloader = unittest.TestLoader()
        testnames = testloader.getTestCaseNames(testcase_klass)
        suite = unittest.TestSuite()
        for name in testnames:
            suite.addTest(testcase_klass(name, param=param))
        return suite

class TestTokenDefault(ParametrizedTestCase):

  def test_CorrectTokenInputDefault(self):
    #the goal is this test is prove that an input returns the correct token.
    if self.param != None:
        lex.giveInput(self.param[1])
        stringedToken = str(lex.getToken())
        self.assertEqual(getString(stringedToken), self.param[1])
        self.assertEqual(getToken(stringedToken), self.param[0])

class TestTokenName(ParametrizedTestCase):
    def test_NameCannotStartWithANumber(self):
    #A Name can't start with a number
        #if self.param != None:
            lex.giveInput('8test')
            stringedToken = str(lex.getToken())
            self.assertEqual(getToken(stringedToken), 'NUMBER')
            stringedToken = str(lex.getToken())
            self.assertEqual(getToken(stringedToken), 'NAME')

    def test_NameCannotStartWithASymbol(self):
        #A Name can't start with a Symbol
        #if self.param != None:
            lex.giveInput('_test')
            stringedToken = str(lex.getToken())
            self.assertEqual(getToken(stringedToken), 'NAME')
            self.assertEqual(getString(stringedToken), 'test')

    def test_NameCanStartWithACapital(self):
            #A Name can't start with a Symbol
            #if self.param != None:
                lex.giveInput('Test')
                stringedToken = str(lex.getToken())
                self.assertEqual(getToken(stringedToken), 'NAME')
                self.assertEqual(getString(stringedToken), 'Test')

    def test_NameCanContainNumbers(self):
            #A Name can't start with a Symbol
            #if self.param != None:
                lex.giveInput('Te1st')
                stringedToken = str(lex.getToken())
                self.assertEqual(getToken(stringedToken), 'NAME')
                self.assertEqual(getString(stringedToken), 'Te1st')

    def test_NameCanContainNumbersAtTheEnd(self):
            #A Name can't start with a Symbol
            #if self.param != None:
                lex.giveInput('Test1')
                stringedToken = str(lex.getToken())
                self.assertEqual(getToken(stringedToken), 'NAME')
                self.assertEqual(getString(stringedToken), 'Test1')

    def test_NameCanContainMultipleNumbers(self):
            #A Name can't start with a Symbol
            #if self.param != None:
                lex.giveInput('Te12st12')
                stringedToken = str(lex.getToken())
                self.assertEqual(getToken(stringedToken), 'NAME')
                self.assertEqual(getString(stringedToken), 'Te12st12')

    def test_NameCanContainUnderscore(self):
            #A Name can't start with a Symbol
            #if self.param != None:
                lex.giveInput('Te_st')
                stringedToken = str(lex.getToken())
                self.assertEqual(getToken(stringedToken), 'NAME')
                self.assertEqual(getString(stringedToken), 'Te_st')

    def test_NameCanContainUnderscoreAtTheEnd(self):
            #A Name can't start with a Symbol
            #if self.param != None:
                lex.giveInput('Test_')
                stringedToken = str(lex.getToken())
                self.assertEqual(getToken(stringedToken), 'NAME')
                self.assertEqual(getString(stringedToken), 'Test_')

class TestTokenNumber(ParametrizedTestCase):
     def test_Number(self):
    #A Name can't start with a number
        if self.param != None:
            lex.giveInput('854')
            stringedToken = str(lex.getToken())
            self.assertEqual(getToken(stringedToken), 'NUMBER')

     def test_NumberCanNotStartWithALetter(self):
        #A Name can't start with a number
            if self.param != None:
                lex.giveInput('h854')
                stringedToken = str(lex.getToken())
                self.assertNotEqual(getToken(stringedToken), 'NUMBER')

      #def test_NumberCanNotStartWithASymbol(self):
      #todo

     def test_NumberCanNotContainALetter(self):
        #A Name can't start with a number
            if self.param != None:
                lex.giveInput('8h54')
                stringedToken = str(lex.getToken())
                #self.assertNotEqual(getToken(stringedToken), 'NUMBER')
                self.assertNotEqual(getString(stringedToken), '854')

     def test_NumberCanNotContainASymbol(self):
        #A Name can't start with a number
            if self.param != None:
                lex.giveInput('8$54')
                stringedToken = str(lex.getToken())
                self.assertNotEqual(getString(stringedToken), '854')

     def test_NumberCanBeNegative(self):
        #A Name can't start with a number
            if self.param != None:
                lex.giveInput('-854')
                stringedToken = str(lex.getToken())
                self.assertEqual(getToken(stringedToken), 'MINUS')
                stringedToken = str(lex.getToken())
                self.assertEqual(getString(stringedToken), '854')
                self.assertEqual(getToken(stringedToken), 'NUMBER')











