__author__ = 'demathieu'

import Yacc
import unittest

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

class TestIntegerVarDeclarations(ParametrizedTestCase):

    def test_DeclareVariable(self):
        try:
            Yacc.forTesting('int test;')
        except SyntaxError:
            self.fail('ExpectedException not thrown')
        else:
            pass

    def test_VariableDeclarationNeedSemicolon(self):
        try:
            Yacc.forTesting('int test')
        except SyntaxError:
            pass
        else:
            self.fail('ExpectedException not thrown')

    def test_VariableDeclarationNeedsType(self):
        try:
            Yacc.forTesting('test;')
        except SyntaxError:
            pass
        else:
            self.fail('ExpectedException not thrown')

    def test_VariableDeclarationNeedsName(self):
        try:
            Yacc.forTesting('int ;')
        except SyntaxError:
            pass
        else:
            self.fail('ExpectedException not thrown')

    def test_DeclareMultipleVariables(self):
        try:
            Yacc.forTesting('int test; int test2;')
        except SyntaxError:
            self.fail('ExpectedException not thrown')
        else:
            pass

    def test_DeclareMultipleVariablesNeedsSemicolonInBetween(self):
        try:
            Yacc.forTesting('int test int test2;')
        except SyntaxError:
            pass
        else:
            self.fail('ExpectedException not thrown')

    def test_DeclareMultipleVariablesNeedsSemicolonAtTheEnd(self):
        try:
            Yacc.forTesting('int test ; int test2')
        except SyntaxError:
            pass
        else:
            self.fail('ExpectedException not thrown')

    def test_DeclareMultipleVariablesNeedsTwoTypes(self):
        try:
            Yacc.forTesting('int test ; int test2')
        except SyntaxError:
            pass
        else:
            self.fail('ExpectedException not thrown')

    def test_DeclareMultipleVariablesInMass(self):
        try:
            Yacc.forTesting('int test ; int test2; int test2;int test2;int test2;int test2; int test2; int test2;int test2; int test2;int test2;int test2;int test2;')
        except SyntaxError:
            self.fail('ExpectedException not thrown')
        else:
            pass

class TestCharVarDeclarations(ParametrizedTestCase):

    def test_DeclareVariable(self):
        try:
            Yacc.forTesting('char test;')
        except SyntaxError:
            self.fail('ExpectedException not thrown')
        else:
            pass

    def test_VariableDeclarationNeedSemicolon(self):
        try:
            Yacc.forTesting('char test')
        except SyntaxError:
            pass
        else:
            self.fail('ExpectedException not thrown')

    def test_VariableDeclarationNeedsType(self):
        try:
            Yacc.forTesting('test;')
        except SyntaxError:
            pass
        else:
            self.fail('ExpectedException not thrown')

    def test_VariableDeclarationNeedsName(self):
        try:
            Yacc.forTesting('char ;')
        except SyntaxError:
            pass
        else:
            self.fail('ExpectedException not thrown')

    def test_DeclareMultipleVariables(self):
        try:
            Yacc.forTesting('char test; char test2;')
        except SyntaxError:
            self.fail('ExpectedException not thrown')
        else:
            pass

    def test_DeclareMultipleVariablesNeedsSemicolonInBetween(self):
        try:
            Yacc.forTesting('char test char test2;')
        except SyntaxError:
            pass
        else:
            self.fail('ExpectedException not thrown')

    def test_DeclareMultipleVariablesNeedsSemicolonAtTheEnd(self):
        try:
            Yacc.forTesting('char test ; char test2')
        except SyntaxError:
            pass
        else:
            self.fail('ExpectedException not thrown')

    def test_DeclareMultipleVariablesNeedsTwoTypes(self):
        try:
            Yacc.forTesting('char test ; char test2')
        except SyntaxError:
            pass
        else:
            self.fail('ExpectedException not thrown')

    def test_DeclareMultipleVariablesInMass(self):
        try:
            Yacc.forTesting('char test ; char test2; char test2;char test2;char test2;char test2; char test2; char test2;char test2; char test2;char test2;char test2;char test2;')
        except SyntaxError:
            self.fail('ExpectedException not thrown')
        else:
            pass

class TestIntegerAndCharCombined(ParametrizedTestCase):

    def test_DeclareVariableFirstIntegerThenChar(self):
        try:
            Yacc.forTesting('int test; char test;')
        except SyntaxError:
            self.fail('ExpectedException not thrown')
        else:
            pass

    def test_DeclareVariableFirstCharThenInteger(self):
        try:
            Yacc.forTesting('char test; int test;')
        except SyntaxError:
            self.fail('ExpectedException not thrown')
        else:
            pass


    def test_DeclareMultipleVariablesNeedsSemicolonInBetween(self):
        try:
            Yacc.forTesting('int test char test2;')
        except SyntaxError:
            pass
        else:
            self.fail('ExpectedException not thrown')

    def test_DeclareMultipleVariablesNeedsSemicolonAtTheEnd(self):
        try:
            Yacc.forTesting('int test ; char test2')
        except SyntaxError:
            pass
        else:
            self.fail('ExpectedException not thrown')

    def test_DeclareMultipleVariablesNeedsTwoTypes(self):
        try:
            Yacc.forTesting(' test ; char test2')
        except SyntaxError:
            pass
        else:
            self.fail('ExpectedException not thrown')

    def test_DeclareMultipleVariablesInMass(self):
        try:
            Yacc.forTesting('char test ; int test2; char test2;char test2;char test2;int test2; char test2; char test2;int test2; char test2;char test2;char test2;char test2;')
        except SyntaxError:
            self.fail('ExpectedException not thrown')
        else:
            pass