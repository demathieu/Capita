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

class TestSimpleFunctionNoParamsNoBody(ParametrizedTestCase):

    def test_SimpleFunctionWorks(self):
        try:
            Yacc.forTesting('int main(){}')
        except SyntaxError:
            self.fail('ExpectedException not thrown')
        else:
            pass

    def test_SimpleFunctionNeedsType(self):
        try:
            Yacc.forTesting('main(){}')
        except SyntaxError:
            pass
        else:
            self.fail('ExpectedException not thrown')

    def test_SimpleFunctionNeedsName(self):
        try:
            Yacc.forTesting('int (){}')
        except SyntaxError:
            pass
        else:
            self.fail('ExpectedException not thrown')

    def test_SimpleFunctionNeedsLPar(self):
        try:
            Yacc.forTesting('int main){}')
        except SyntaxError:
            pass
        else:
            self.fail('ExpectedException not thrown')

    def test_SimpleFunctionNeedsRPar(self):
        try:
            Yacc.forTesting('int main({}')
        except SyntaxError:
            pass
        else:
            self.fail('ExpectedException not thrown')

    def test_SimpleFunctionNeedsLBrace(self):
        try:
            Yacc.forTesting('int main()}')
        except SyntaxError:
            pass
        else:
            self.fail('ExpectedException not thrown')

    def test_SimpleFunctionNeedsRBrace(self):
        try:
            Yacc.forTesting('int main(){')
        except SyntaxError:
            pass
        else:
            self.fail('ExpectedException not thrown')

    def test_SimpleFunctionDoesNotNeedSemiColon(self):
        try:
            Yacc.forTesting('int main(){};')
        except SyntaxError:
            pass
        else:
            self.fail('ExpectedException not thrown')

class TestSimpleFunctionNoParamsWithSimpleBodyAndVarDeclaration(ParametrizedTestCase):
    def test_SimpleFunctionOneStatement(self):
        try:
            Yacc.forTesting('int main(){return 5;}')
        except SyntaxError:
            self.fail('ExpectedException not thrown')
        else:
            pass

    def test_SimpleFunctionMultipleStatements(self):
        try:
            Yacc.forTesting('int main(){return test;return test2;}')
        except SyntaxError:
            self.fail('ExpectedException not thrown')
        else:
            pass


    def test_SimpleFunctionVarDeclarationInteger(self):
        try:
            Yacc.forTesting('int main(){int test;}')
        except SyntaxError:
            self.fail('ExpectedException not thrown')
        else:
            pass

    def test_SimpleFunctionVarDeclarationChar(self):
        try:
            Yacc.forTesting('int main(){char test;}')
        except SyntaxError:
            self.fail('ExpectedException not thrown')
        else:
            pass

    def test_SimpleFunctionVarDeclarationIntegerMultiple(self):
        try:
            Yacc.forTesting('int main(){int test;int test;}')
        except SyntaxError:
            self.fail('ExpectedException not thrown')
        else:
            pass

    def test_SimpleFunctionVarDeclarationCharMultiple(self):
        try:
            Yacc.forTesting('int main(){char test;char test;}')
        except SyntaxError:
            self.fail('ExpectedException not thrown')
        else:
            pass

    def test_SimpleFunctionVarDeclarationMixed(self):
        try:
            Yacc.forTesting('int main(){int test;char test;}')
        except SyntaxError:
            self.fail('ExpectedException not thrown')
        else:
            pass

    def test_SimpleFunctionVarDeclarationMixedReverse(self):
        try:
            Yacc.forTesting('int main(){char test;int test;}')
        except SyntaxError:
            self.fail('ExpectedException not thrown')
        else:
            pass

    def test_SimpleFunctionVarDeclarationMassInteger(self):
        try:
            Yacc.forTesting('int main(){int test;int test;int test;int test;int test;int test;int test;int test;int test;}')
        except SyntaxError:
            self.fail('ExpectedException not thrown')
        else:
            pass

    def test_SimpleFunctionVarDeclarationMassChar(self):
        try:
            Yacc.forTesting('int main(){char test;char test;char test;char test;char test;char test;char test;char test;char test;}')
        except SyntaxError:
            self.fail('ExpectedException not thrown')
        else:
            pass

    def test_SimpleFunctionVarDeclarationMassMixed(self):
        try:
            Yacc.forTesting('int main(){int test;char test;int test;char test;char test;int test;char test;char test;int test;}')
        except SyntaxError:
            self.fail('ExpectedException not thrown')
        else:
            pass

class TestSimpleFunctionNoParamsWithVarInitialization(ParametrizedTestCase):
     def test_InitializeInteger(self):
        try:
            Yacc.forTesting('int main(){int test; test = 5;}')
        except SyntaxError:
            self.fail('ExpectedException not thrown')
        else:
            pass

     def test_InitializeIntegerNeedsAssignSymbol(self):
        try:
            Yacc.forTesting('int main(){int test; test 5;}')
        except SyntaxError:
            pass
        else:
            self.fail('ExpectedException not thrown')

     def test_InitializeChar(self):
        try:
            Yacc.forTesting('int main(){char test; test = haha;}')
        except SyntaxError:
            self.fail('ExpectedException not thrown')
        else:
            pass
     def test_InitializeIntegerMultipleSameVar(self):
        try:
            Yacc.forTesting('int main(){int test;test = 5; test = 6; test = 7;}')
        except SyntaxError:
            self.fail('ExpectedException not thrown')
        else:
            pass

     def test_InitializeIntegerMultipleDifferentVar(self):
        try:
            Yacc.forTesting('int main(){int test;test = 5; test2 = 6; test3 = 7;}')
        except SyntaxError:
            self.fail('ExpectedException not thrown')
        else:
            pass

     def test_InitializeCharMultipleDifferentVar(self):
        try:
            Yacc.forTesting('int main(){char test;test = haha; test2 = haha; test3 = haha;}')
        except SyntaxError:
            self.fail('ExpectedException not thrown')
        else:
            pass

     def test_InitializeCharMultipleSameVar(self):
        try:
            Yacc.forTesting('int main(){char test;test = haha; test = haha; test = haha;}')
        except SyntaxError:
            self.fail('ExpectedException not thrown')
        else:
            pass

     def test_InitializeIntegerAndChar(self):
        try:
            Yacc.forTesting('int main(){int test;char test2;test = 5; test2 = haha;}')
        except SyntaxError:
            self.fail('ExpectedException not thrown')
        else:
            pass