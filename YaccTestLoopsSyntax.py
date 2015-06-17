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


class TestIfClauseWithoutElse(ParametrizedTestCase):

    def test_SimpleIF(self):
        try:
            Yacc.forTesting('int main(){if(1){} }')
        except SyntaxError:
            self.fail('ExpectedException not thrown')
        else:
            pass

    def test_SimpleIFExpEqualIntegerConstants(self):
        try:
            Yacc.forTesting('int main(){if(1 == 1){} }')
        except SyntaxError:
            self.fail('ExpectedException not thrown')
        else:
            pass

    def test_SimpleIFExpEqualIntegerVarConstant(self):
        try:
            Yacc.forTesting('int main(){if(1 == x){} }')
        except SyntaxError:
            self.fail('ExpectedException not thrown')
        else:
            pass

    def test_SimpleIFExpEqualIntegerVarConstantReverse(self):
        try:
            Yacc.forTesting('int main(){if(x == 1){} }')
        except SyntaxError:
            self.fail('ExpectedException not thrown')
        else:
            pass

    def test_SimpleIFExpGreaterIntegerConstantConstant(self):
        try:
            Yacc.forTesting('int main(){if(1 > 2){} }')
        except SyntaxError:
            self.fail('ExpectedException not thrown')
        else:
            pass
    def test_SimpleIFExpGreaterIntegerConstantVar(self):
        try:
            Yacc.forTesting('int main(){if(1 > x){} }')
        except SyntaxError:
            self.fail('ExpectedException not thrown')
        else:
            pass

    def test_SimpleIFExpGreaterIntegerConstantVarReverse(self):
        try:
            Yacc.forTesting('int main(){if(x > 1){} }')
        except SyntaxError:
            self.fail('ExpectedException not thrown')
        else:
            pass

    def test_SimpleIFExpGreaterIntegerConstantVarReverse(self):
        try:
            Yacc.forTesting('int main(){if(x > 1){} }')
        except SyntaxError:
            self.fail('ExpectedException not thrown')
        else:
            pass

    def test_SimpleIFExpGreaterIntegerVarVar(self):
        try:
            Yacc.forTesting('int main(){if(x > x){} }')
        except SyntaxError:
            self.fail('ExpectedException not thrown')
        else:
            pass
    def test_SimpleIFExpLessIntegerConstantConstant(self):
        try:
            Yacc.forTesting('int main(){if(1 < 2){} }')
        except SyntaxError:
            self.fail('ExpectedException not thrown')
        else:
            pass
    def test_SimpleIFExpLessIntegerConstantVar(self):
        try:
            Yacc.forTesting('int main(){if(1 < x){} }')
        except SyntaxError:
            self.fail('ExpectedException not thrown')
        else:
            pass

    def test_SimpleIFExpLessIntegerConstantVarReverse(self):
        try:
            Yacc.forTesting('int main(){if(x < 1){} }')
        except SyntaxError:
            self.fail('ExpectedException not thrown')
        else:
            pass

    def test_SimpleIFExpLessIntegerConstantVarReverse(self):
        try:
            Yacc.forTesting('int main(){if(x < 1){} }')
        except SyntaxError:
            self.fail('ExpectedException not thrown')
        else:
            pass

    def test_SimpleIFExpLessIntegerVarVar(self):
        try:
            Yacc.forTesting('int main(){if(x < x){} }')
        except SyntaxError:
            self.fail('ExpectedException not thrown')
        else:
            pass
    def test_SimpleIFExpNequalIntegerConstantConstant(self):
        try:
            Yacc.forTesting('int main(){if(1 != 2){} }')
        except SyntaxError:
            self.fail('ExpectedException not thrown')
        else:
            pass
    def test_SimpleIFExpNequalIntegerConstantVar(self):
        try:
            Yacc.forTesting('int main(){if(1 != x){} }')
        except SyntaxError:
            self.fail('ExpectedException not thrown')
        else:
            pass

    def test_SimpleIFExpNequalIntegerConstantVarReverse(self):
        try:
            Yacc.forTesting('int main(){if(x != 1){} }')
        except SyntaxError:
            self.fail('ExpectedException not thrown')
        else:
            pass

    def test_SimpleIFExpNequalIntegerConstantVarReverse(self):
        try:
            Yacc.forTesting('int main(){if(x != 1){} }')
        except SyntaxError:
            self.fail('ExpectedException not thrown')
        else:
            pass

    def test_SimpleIFExpNequalIntegerVarVar(self):
        try:
            Yacc.forTesting('int main(){if(x != x){} }')
        except SyntaxError:
            self.fail('ExpectedException not thrown')
        else:
            pass

    def test_SimpleIFExpCanBeFunctionCall(self):
        try:
            Yacc.forTesting('int main(){if(test(5)){} }')
        except SyntaxError:
            self.fail('ExpectedException not thrown')
        else:
            pass

    def test_SimpleIFExpNeedLPar(self):
        try:
            Yacc.forTesting('int main(){if 1){} }')
        except SyntaxError:
            pass
        else:
            self.fail('ExpectedException not thrown')

    def test_SimpleIFExpNeedRPar(self):
        try:
            Yacc.forTesting('int main(){if (1{} }')
        except SyntaxError:
            pass
        else:
            self.fail('ExpectedException not thrown')

    def test_SimpleIFExpNeedExpCantBeEmpty(self):
        try:
            Yacc.forTesting('int main(){if (){} }')
        except SyntaxError:
            pass
        else:
            self.fail('ExpectedException not thrown')

    def test_SimpleIFExpNeedExpNeedLBrace(self):
        try:
            Yacc.forTesting('int main(){if (1)} }')
        except SyntaxError:
            pass
        else:
            self.fail('ExpectedException not thrown')

    def test_SimpleIFExpNeedExpNeedRBrace(self):
        try:
            Yacc.forTesting('int main(){if (1){ }')
        except SyntaxError:
            pass
        else:
            self.fail('ExpectedException not thrown')

    def test_MultipleIf(self):
        try:
            Yacc.forTesting('int main(){if(1){}; if(1){} }')
        except SyntaxError:
            self.fail('ExpectedException not thrown')
        else:
            pass
    def test_MultipleIfMass(self):
        try:
            Yacc.forTesting('int main(){if(1){}; if(1){}; if(1){};if(1){};if(1){};if(1){};if(1){};}')
        except SyntaxError:
            self.fail('ExpectedException not thrown')
        else:
            pass

    def test_MultipleIfNeedsSemiColon(self):
        try:
            Yacc.forTesting('int main(){if(1){} if(1){} }')
        except SyntaxError:
            pass
        else:
            self.fail('ExpectedException not thrown')

    def test_MultipleIfCanBeSpacedByExp(self):
        try:
            Yacc.forTesting('int main(){if(1){}; x = 6; y = 7; if(1){}}')
        except SyntaxError:
            self.fail('ExpectedException not thrown')
        else:
            pass

class TestIfClauseWitElseButNotUsed(ParametrizedTestCase):

    def test_SimpleIF(self):
        try:
            Yacc.forTesting('int main(){if(1){}else{} }')
        except SyntaxError:
            self.fail('ExpectedException not thrown')
        else:
            pass

    def test_SimpleIFExpEqualIntegerConstants(self):
        try:
            Yacc.forTesting('int main(){if(1 == 1){}else{} }')
        except SyntaxError:
            self.fail('ExpectedException not thrown')
        else:
            pass

    def test_SimpleIFExpEqualIntegerVarConstant(self):
        try:
            Yacc.forTesting('int main(){if(1 == x){}else{} }')
        except SyntaxError:
            self.fail('ExpectedException not thrown')
        else:
            pass

    def test_SimpleIFExpEqualIntegerVarConstantReverse(self):
        try:
            Yacc.forTesting('int main(){if(x == 1){}else{} }')
        except SyntaxError:
            self.fail('ExpectedException not thrown')
        else:
            pass

    def test_SimpleIFExpGreaterIntegerConstantConstant(self):
        try:
            Yacc.forTesting('int main(){if(1 > 2){}else{} }')
        except SyntaxError:
            self.fail('ExpectedException not thrown')
        else:
            pass
    def test_SimpleIFExpGreaterIntegerConstantVar(self):
        try:
            Yacc.forTesting('int main(){if(1 > x){}else{} }')
        except SyntaxError:
            self.fail('ExpectedException not thrown')
        else:
            pass

    def test_SimpleIFExpGreaterIntegerConstantVarReverse(self):
        try:
            Yacc.forTesting('int main(){if(x > 1){}else{} }')
        except SyntaxError:
            self.fail('ExpectedException not thrown')
        else:
            pass

    def test_SimpleIFExpGreaterIntegerConstantVarReverse(self):
        try:
            Yacc.forTesting('int main(){if(x > 1){}else{} }')
        except SyntaxError:
            self.fail('ExpectedException not thrown')
        else:
            pass

    def test_SimpleIFExpGreaterIntegerVarVar(self):
        try:
            Yacc.forTesting('int main(){if(x > x){}else{} }')
        except SyntaxError:
            self.fail('ExpectedException not thrown')
        else:
            pass
    def test_SimpleIFExpLessIntegerConstantConstant(self):
        try:
            Yacc.forTesting('int main(){if(1 < 2){}else{} }')
        except SyntaxError:
            self.fail('ExpectedException not thrown')
        else:
            pass
    def test_SimpleIFExpLessIntegerConstantVar(self):
        try:
            Yacc.forTesting('int main(){if(1 < x){}else{} }')
        except SyntaxError:
            self.fail('ExpectedException not thrown')
        else:
            pass

    def test_SimpleIFExpLessIntegerConstantVarReverse(self):
        try:
            Yacc.forTesting('int main(){if(x < 1){}else{} }')
        except SyntaxError:
            self.fail('ExpectedException not thrown')
        else:
            pass

    def test_SimpleIFExpLessIntegerConstantVarReverse(self):
        try:
            Yacc.forTesting('int main(){if(x < 1){}else{} }')
        except SyntaxError:
            self.fail('ExpectedException not thrown')
        else:
            pass

    def test_SimpleIFExpLessIntegerVarVar(self):
        try:
            Yacc.forTesting('int main(){if(x < x){}else{} }')
        except SyntaxError:
            self.fail('ExpectedException not thrown')
        else:
            pass
    def test_SimpleIFExpNequalIntegerConstantConstant(self):
        try:
            Yacc.forTesting('int main(){if(1 != 2){}else{} }')
        except SyntaxError:
            self.fail('ExpectedException not thrown')
        else:
            pass
    def test_SimpleIFExpNequalIntegerConstantVar(self):
        try:
            Yacc.forTesting('int main(){if(1 != x){}else{} }')
        except SyntaxError:
            self.fail('ExpectedException not thrown')
        else:
            pass

    def test_SimpleIFExpNequalIntegerConstantVarReverse(self):
        try:
            Yacc.forTesting('int main(){if(x != 1){}else{} }')
        except SyntaxError:
            self.fail('ExpectedException not thrown')
        else:
            pass

    def test_SimpleIFExpNequalIntegerConstantVarReverse(self):
        try:
            Yacc.forTesting('int main(){if(x != 1){}else{} }')
        except SyntaxError:
            self.fail('ExpectedException not thrown')
        else:
            pass

    def test_SimpleIFExpNequalIntegerVarVar(self):
        try:
            Yacc.forTesting('int main(){if(x != x){}else{} }')
        except SyntaxError:
            self.fail('ExpectedException not thrown')
        else:
            pass

    def test_SimpleIFExpCanBeFunctionCall(self):
        try:
            Yacc.forTesting('int main(){if(test(5)){}else{} }')
        except SyntaxError:
            self.fail('ExpectedException not thrown')
        else:
            pass

    def test_SimpleIFExpNeedLPar(self):
        try:
            Yacc.forTesting('int main(){if 1){}else{} }')
        except SyntaxError:
            pass
        else:
            self.fail('ExpectedException not thrown')

    def test_SimpleIFExpNeedRPar(self):
        try:
            Yacc.forTesting('int main(){if (1{}else{} }')
        except SyntaxError:
            pass
        else:
            self.fail('ExpectedException not thrown')

    def test_SimpleIFExpNeedExpCantBeEmpty(self):
        try:
            Yacc.forTesting('int main(){if (){}else{} }')
        except SyntaxError:
            pass
        else:
            self.fail('ExpectedException not thrown')

    def test_SimpleIFExpNeedExpNeedLBrace(self):
        try:
            Yacc.forTesting('int main(){if (1)}else{} }')
        except SyntaxError:
            pass
        else:
            self.fail('ExpectedException not thrown')

    def test_SimpleIFExpNeedExpNeedRBrace(self):
        try:
            Yacc.forTesting('int main(){if (1){ }else{}')
        except SyntaxError:
            pass
        else:
            self.fail('ExpectedException not thrown')

    def test_MultipleIf(self):
        try:
            Yacc.forTesting('int main(){if(1){}else{}; if(1){}else{} }')
        except SyntaxError:
            self.fail('ExpectedException not thrown')
        else:
            pass
    def test_MultipleIfMass(self):
        try:
            Yacc.forTesting('int main(){if(1){}else{}; if(1){}else{}; if(1){}else{};if(1){}else{};if(1){};if(1){};if(1){};}')
        except SyntaxError:
            self.fail('ExpectedException not thrown')
        else:
            pass

    def test_MultipleIfNeedsSemiColon(self):
        try:
            Yacc.forTesting('int main(){if(1){}else{} if(1){}else{} }')
        except SyntaxError:
            pass
        else:
            self.fail('ExpectedException not thrown')

    def test_MultipleIfCanBeSpacedByExp(self):
        try:
            Yacc.forTesting('int main(){if(1){}else{}; x = 6; y = 7; if(1){}else{}}')
        except SyntaxError:
            self.fail('ExpectedException not thrown')
        else:
            pass

class TestIfClauseBody(ParametrizedTestCase):

    def test_SimpleIFReturnNumber(self):
        try:
            Yacc.forTesting('int main(){if(1){return 5;}else{} }')
        except SyntaxError:
            self.fail('ExpectedException not thrown')
        else:
            pass

    def test_SimpleIFReturnConstantInteger(self):
        try:
            Yacc.forTesting('int main(){if(1){int x; return x;}else{} }')
        except SyntaxError:
            self.fail('ExpectedException not thrown')
        else:
            pass

    def test_SimpleIFReturnConstantChar(self):
        try:
            Yacc.forTesting('int main(){if(1){char x; return x;}else{} }')
        except SyntaxError:
            self.fail('ExpectedException not thrown')
        else:
            pass

    def test_SimpleIFReturnNumberInElse(self):
        try:
            Yacc.forTesting('int main(){if(1){}else{return 5;} }')
        except SyntaxError:
            self.fail('ExpectedException not thrown')
        else:
            pass

    def test_SimpleIFReturnConstantIntegerInElse(self):
        try:
            Yacc.forTesting('int main(){if(1){}else{int x; return x;} }')
        except SyntaxError:
            self.fail('ExpectedException not thrown')
        else:
            pass

    def test_SimpleIFReturnConstantChar(self):
        try:
            Yacc.forTesting('int main(){if(1){}else{char x; return x;} }')
        except SyntaxError:
            self.fail('ExpectedException not thrown')
        else:
            pass

class TestWhileLoop(ParametrizedTestCase):

    def test_SimpleWhile(self):
        try:
            Yacc.forTesting('int main(){int x; while(x == 4){return 5;} }')
        except SyntaxError:
            self.fail('ExpectedException not thrown')
        else:
            pass