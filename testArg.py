__author__ = 'demathieu'

import unittest
import LexTest as LexTest
import lex



def getToken(string):
    temp = string.split(',')
    temp2 = temp[0]
    return(temp2[9:])

def getString(string):
    temp = string.split(',')
    temp2 = temp[1]
    return temp2.replace("'", "")

class TestTokenName(unittest.TestCase):
    def test_NameCannotStartWithANumber(self):
    #A Name can't start with a number
            lex.giveInput('8test')
            stringedToken = str(lex.getToken())
            self.assertEqual(getToken(stringedToken), 'NUMBER')
            stringedToken = str(lex.getToken())
            self.assertEqual(getToken(stringedToken), 'NAME')

    def test_NameCannotStartWithASymbol(self):
        #A Name can't start with a Symbol
        if self.param != None:
            lex.giveInput('_test')
            stringedToken = str(lex.getToken())
            self.assertEqual(getToken(stringedToken), 'NAME')
            self.assertEqual(getString(stringedToken), 'te5st')

suite = unittest.TestSuite()
suite.addTest(LexTest.TestTokenName('test_NameCannotStartWithANumber','test_NameCannotStartWithASymbol'))
