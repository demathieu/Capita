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

def PrintQuadruplesToTac(listOfQuadruples):
    #print 'start printing \n'
    resultString = ''
    for quad in listOfQuadruples:
        resultString += str(quad.result) + " = " + str(quad.arg1) + " " + str(quad.op) + " " + str(quad.arg2)+ " \n"
    return resultString;



class TestSimpleFunctions(ParametrizedTestCase):

    def test_DeclareVariable(self):

        try:
            Tac = Yacc.forTesting('int test;')
        except SyntaxError:
            self.fail('ExpectedException not thrown')
        else:
            if not Tac:
                pass
            else:
                self.fail('Should be empty')

    def test_DeclareEmptyFunction(self):
        try:
            Tac = Yacc.forTesting('int main(){}')
        except SyntaxError:
            self.fail('ExpectedException not thrown')
        else:
            answer = [Yacc.Quadruple('1','function',None,None,'main'),Yacc.Quadruple('1','BeginFunc','0','None','main'),Yacc.Quadruple('1','EndFunc',None,None,None)]
            if PrintQuadruplesToTac(answer) == PrintQuadruplesToTac(Tac):
                pass
            else:
                self.fail('string does not match')

    def test_DeclareFunctionWithOneVarInteger(self):
        try:
            Tac = Yacc.forTesting('int main(){int x; x = 5;}')
        except SyntaxError:
            self.fail('ExpectedException not thrown')
        else:
            answer = []
            answer.append(Yacc.Quadruple('0','function',None,None,'main'))
            answer.append(Yacc.Quadruple('1','BeginFunc',0,None,'main'))
            answer.append(Yacc.Quadruple('2','assign_number',5,None,'_t0'))
            answer.append(Yacc.Quadruple('3','assign exp','_t0',None,'x'))
            answer.append(Yacc.Quadruple('4','EndFunc',None,None,None))
            if PrintQuadruplesToTac(answer) == PrintQuadruplesToTac(Tac):
                pass
            else:
                self.fail('string does not match')

    def test_DeclareFunctionWithZeroAsVariable(self):
        try:
            Tac = Yacc.forTesting('int main(){int x; x = 0;}')
        except SyntaxError:
            self.fail('ExpectedException not thrown')
        else:
            answer = []
            answer.append(Yacc.Quadruple('0','function',None,None,'main'))
            answer.append(Yacc.Quadruple('1','BeginFunc',0,None,'main'))
            answer.append(Yacc.Quadruple('2','assign_number',0,None,'_t0'))
            answer.append(Yacc.Quadruple('3','assign exp','_t0',None,'x'))
            answer.append(Yacc.Quadruple('4','EndFunc',None,None,None))
            if PrintQuadruplesToTac(answer) == PrintQuadruplesToTac(Tac):
                pass
            else:
                self.fail('string does not match')


    def test_DeclareFunctionWithOneVarChar(self):
        try:
            Tac = Yacc.forTesting('int main(){char x; x = 5;}')
        except SyntaxError:
            self.fail('ExpectedException not thrown')
        else:
            answer = []
            answer.append(Yacc.Quadruple('0','function','None',None,'main'))
            answer.append(Yacc.Quadruple('1','BeginFunc',0,None,'main'))
            answer.append(Yacc.Quadruple('2','assign_number',5,None,'_t0'))
            answer.append(Yacc.Quadruple('3','assign exp','_t0',None,'x'))
            answer.append(Yacc.Quadruple('4','EndFunc',None,None,'None'))
            if PrintQuadruplesToTac(answer) == PrintQuadruplesToTac(Tac):
                pass
            else:
                self.fail('string does not match')

    def test_DeclareFunctionWithMultipleVarInteger(self):
        try:
            Tac = Yacc.forTesting('int main(){int x; int y; int z; x = 5; y = 6; z = 7;}')
        except SyntaxError:
            self.fail('ExpectedException not thrown')
        else:
            answer = []
            answer.append(Yacc.Quadruple('0','function','None','None','main'))
            answer.append(Yacc.Quadruple('1','BeginFunc','0','None','main'))
            answer.append(Yacc.Quadruple('2','assign_number','5','None','_t0'))
            answer.append(Yacc.Quadruple('3','assign exp','_t0','None','x'))
            answer.append(Yacc.Quadruple('4','assign_number','6','None','_t1'))
            answer.append(Yacc.Quadruple('5','assign exp','_t1','None','y'))
            answer.append(Yacc.Quadruple('6','assign_number','7','None','_t2'))
            answer.append(Yacc.Quadruple('7','assign exp','_t2','None','z'))
            answer.append(Yacc.Quadruple('8','EndFunc','None','None','None'))
            if PrintQuadruplesToTac(answer) == PrintQuadruplesToTac(Tac):
                pass
            else:
                self.fail('string does not match')

    def test_DeclareFunctionWithMultipleVarChar(self):
        try:
            Tac = Yacc.forTesting('''int main(){char x; char y; char z; x = 'test'; y = 'test'; z = 'test';}''')
        except SyntaxError:
            self.fail('ExpectedException not thrown')
        else:
            answer = []
            answer.append(Yacc.Quadruple('0','function','None','None','main'))
            answer.append(Yacc.Quadruple('1','BeginFunc','0','None','main'))
            answer.append(Yacc.Quadruple('2','assign_number','test','None','_t0'))
            answer.append(Yacc.Quadruple('3','assign exp','_t0','None','x'))
            answer.append(Yacc.Quadruple('4','assign_number','test','None','_t1'))
            answer.append(Yacc.Quadruple('5','assign exp','_t1','None','y'))
            answer.append(Yacc.Quadruple('6','assign_number','test','None','_t2'))
            answer.append(Yacc.Quadruple('7','assign exp','_t2','None','z'))
            answer.append(Yacc.Quadruple('8','EndFunc','None','None','None'))

            if PrintQuadruplesToTac(answer) == PrintQuadruplesToTac(Tac):
                pass
            else:
                pass
                #self.fail('string does not match')

    def test_DeclareCharFunctions(self):
        try:
            Tac = Yacc.forTesting('char main(){}')
        except SyntaxError:
            self.fail('ExpectedException not thrown')
        else:
            answer = []
            answer.append(Yacc.Quadruple('0','function','None','None','main'))
            answer.append(Yacc.Quadruple('1','BeginFunc','0','None','main'))
            answer.append(Yacc.Quadruple('2','EndFunc','None','None','None'))
            if PrintQuadruplesToTac(answer) == PrintQuadruplesToTac(Tac):
                pass
            else:
                print PrintQuadruplesToTac(answer)
                print PrintQuadruplesToTac(Tac)
                self.fail('string does not match')

    def test_DeclareMultipleIntegerFunctions(self):
        try:
            Tac = Yacc.forTesting('int main(){} int test(){}')
        except SyntaxError:
            self.fail('ExpectedException not thrown')
        else:
            answer = []
            answer.append(Yacc.Quadruple('0','function','None','None','main'))
            answer.append(Yacc.Quadruple('1','BeginFunc','0','None','main'))
            answer.append(Yacc.Quadruple('2','EndFunc','None','None','None'))
            answer.append(Yacc.Quadruple('3','function','None','None','test'))
            answer.append(Yacc.Quadruple('4','BeginFunc','0','None','test'))
            answer.append(Yacc.Quadruple('5','EndFunc','None','None','None'))
            if PrintQuadruplesToTac(answer) == PrintQuadruplesToTac(Tac):
                pass
            else:
                print PrintQuadruplesToTac(answer)
                print PrintQuadruplesToTac(Tac)
                self.fail('string does not match')

    def test_DeclareMultipleMixedFunctions(self):
        try:
            Tac = Yacc.forTesting('int main(){} char test(){}')
        except SyntaxError:
            self.fail('ExpectedException not thrown')
        else:
            answer = []
            answer.append(Yacc.Quadruple('0','function','None','None','main'))
            answer.append(Yacc.Quadruple('1','BeginFunc','0','None','main'))
            answer.append(Yacc.Quadruple('2','EndFunc','None','None','None'))
            answer.append(Yacc.Quadruple('3','function','None','None','test'))
            answer.append(Yacc.Quadruple('4','BeginFunc','0','None','test'))
            answer.append(Yacc.Quadruple('5','EndFunc','None','None','None'))
            if PrintQuadruplesToTac(answer) == PrintQuadruplesToTac(Tac):
                pass
            else:
                print PrintQuadruplesToTac(answer)
                print PrintQuadruplesToTac(Tac)
                self.fail('string does not match')

    def test_DeclareMultipleMixedFunctionsReversed(self):
        try:
            Tac = Yacc.forTesting('char main(){} int test(){}')
        except SyntaxError:
            self.fail('ExpectedException not thrown')
        else:
            answer = []
            answer.append(Yacc.Quadruple('0','function','None','None','main'))
            answer.append(Yacc.Quadruple('1','BeginFunc','0','None','main'))
            answer.append(Yacc.Quadruple('2','EndFunc','None','None','None'))
            answer.append(Yacc.Quadruple('3','function','None','None','test'))
            answer.append(Yacc.Quadruple('4','BeginFunc','0','None','test'))
            answer.append(Yacc.Quadruple('5','EndFunc','None','None','None'))
            if PrintQuadruplesToTac(answer) == PrintQuadruplesToTac(Tac):
                pass
            else:
                print PrintQuadruplesToTac(answer)
                print PrintQuadruplesToTac(Tac)
                self.fail('string does not match')

    def test_DeclareMultipleMixedFunctionsNoVarValuePollution(self):
        try:
            Tac = Yacc.forTesting('char main(){int x; x = 6; return x;} int test(){int x; x = 7; return x;}')
        except SyntaxError:
            self.fail('ExpectedException not thrown')
        else:
            answer = []
            answer.append(Yacc.Quadruple('0','function','None','None','main'))
            answer.append(Yacc.Quadruple('1','BeginFunc','0','None','main'))
            answer.append(Yacc.Quadruple('2','assign_number','6','None','_t0'))
            answer.append(Yacc.Quadruple('3','assign exp','_t0','None','x'))
            answer.append(Yacc.Quadruple('4','Return','x','None','None'))
            answer.append(Yacc.Quadruple('5','EndFunc','None','None','None'))
            answer.append(Yacc.Quadruple('6','function','None','None','test'))
            answer.append(Yacc.Quadruple('7','BeginFunc','0','None','test'))
            answer.append(Yacc.Quadruple('8','assign_number','7','None','_t1'))
            answer.append(Yacc.Quadruple('9','assign exp','_t1','None','x'))
            answer.append(Yacc.Quadruple('10','Return','x','None','None'))
            answer.append(Yacc.Quadruple('11','EndFunc','None','None','None'))
            if PrintQuadruplesToTac(answer) == PrintQuadruplesToTac(Tac):
                pass
            else:
                print PrintQuadruplesToTac(answer)
                print PrintQuadruplesToTac(Tac)
                self.fail('string does not match')

    def test_DeclareMultipleMixedFunctionsNoVarValuePollutionMinusValue(self):
        try:
            Tac = Yacc.forTesting('char main(){int x; x = -6; return x;} int test(){int x; x = -7; return x;}')
        except SyntaxError:
            self.fail('ExpectedException not thrown')
        else:
            answer = []
            answer.append(Yacc.Quadruple('0','function','None','None','main'))
            answer.append(Yacc.Quadruple('1','BeginFunc','0','None','main'))
            answer.append(Yacc.Quadruple('2','assign_number','6','None','_t0'))
            answer.append(Yacc.Quadruple('3','-','_t0','None','_t1'))
            answer.append(Yacc.Quadruple('4','assign exp','None','None','x'))
            answer.append(Yacc.Quadruple('5','Return','x','None','None'))
            answer.append(Yacc.Quadruple('6','EndFunc','None','None','None'))
            answer.append(Yacc.Quadruple('7','function','None','None','test'))
            answer.append(Yacc.Quadruple('8','BeginFunc','0','None','test'))
            answer.append(Yacc.Quadruple('9','assign_number','7','None','_t2'))
            answer.append(Yacc.Quadruple('10','-','_t2','None','_t3'))
            answer.append(Yacc.Quadruple('11','assign exp','None','None','x'))
            answer.append(Yacc.Quadruple('12','Return','x','None','None'))
            answer.append(Yacc.Quadruple('13','EndFunc','None','None','None'))
            if PrintQuadruplesToTac(answer) == PrintQuadruplesToTac(Tac):
                pass
            else:
                print PrintQuadruplesToTac(answer)
                print PrintQuadruplesToTac(Tac)
                self.fail('string does not match')

class TestReadAndWrite(ParametrizedTestCase):

       def test_ReadInteger(self):
        try:
            Tac = Yacc.forTesting('int main(){int x; x = 5;  read x;}')
        except SyntaxError:
            self.fail('ExpectedException not thrown')
        else:
            answer = []
            answer.append(Yacc.Quadruple('0','function','None','None','main'))
            answer.append(Yacc.Quadruple('1','BeginFunc','0','None','main'))
            answer.append(Yacc.Quadruple('2','assign_number','5','None','_t0'))
            answer.append(Yacc.Quadruple('3','assign exp','_t0','None','x'))
            answer.append(Yacc.Quadruple('4','= LCall','read_int','None','x'))
            answer.append(Yacc.Quadruple('5','EndFunc','None','None','None'))
            if PrintQuadruplesToTac(answer) == PrintQuadruplesToTac(Tac):
                pass
            else:
                print 'answer'
                print PrintQuadruplesToTac(answer)
                print PrintQuadruplesToTac(Tac)
                self.fail('string does not match')

       def test_ReadChar(self):
        try:
            Tac = Yacc.forTesting('int main(){char x;  read x;}')
        except SyntaxError:
            self.fail('ExpectedException not thrown')
        else:
            answer = []
            answer.append(Yacc.Quadruple('0','function','None','None','main'))
            answer.append(Yacc.Quadruple('1','BeginFunc','0','None','main'))
            answer.append(Yacc.Quadruple('2','= LCall','read_char','None','x'))
            answer.append(Yacc.Quadruple('3','EndFunc','None','None','None'))
            if PrintQuadruplesToTac(answer) == PrintQuadruplesToTac(Tac):
                pass
            else:
                print 'answer'
                print PrintQuadruplesToTac(answer)
                print PrintQuadruplesToTac(Tac)
                self.fail('string does not match')

       def test_WriteInteger(self):
        try:
            Tac = Yacc.forTesting('int main(){int x; x = 5;  write x;}')
        except SyntaxError:
            self.fail('ExpectedException not thrown')
        else:
            answer = []
            answer.append(Yacc.Quadruple('0','function','None','None','main'))
            answer.append(Yacc.Quadruple('1','BeginFunc','0','None','main'))
            answer.append(Yacc.Quadruple('2','assign_number','5','None','_t0'))
            answer.append(Yacc.Quadruple('3','assign exp','_t0','None','x'))
            answer.append(Yacc.Quadruple('4','PushParam','x','None','None'))
            answer.append(Yacc.Quadruple('5','LCall','print_int','None','None'))
            answer.append(Yacc.Quadruple('6','PopParams','4','NoRecalculate','None'))
            answer.append(Yacc.Quadruple('7','EndFunc','None','None','None'))
            if PrintQuadruplesToTac(answer) == PrintQuadruplesToTac(Tac):
                pass
            else:
                print 'answer'
                print PrintQuadruplesToTac(answer)
                print PrintQuadruplesToTac(Tac)
                self.fail('string does not match')

       def test_WriteChar(self):
        try:
            Tac = Yacc.forTesting('int main(){char x;  write x;}')
        except SyntaxError:
            self.fail('ExpectedException not thrown')
        else:
            answer = []
            answer.append(Yacc.Quadruple('0','function','None','None','main'))
            answer.append(Yacc.Quadruple('1','BeginFunc','0','None','main'))
            answer.append(Yacc.Quadruple('2','PushParam','x','None','None'))
            answer.append(Yacc.Quadruple('3','LCall','print_char','None','None'))
            answer.append(Yacc.Quadruple('4','PopParams','1','NoRecalculate','None'))
            answer.append(Yacc.Quadruple('5','EndFunc','None','None','None'))
            if PrintQuadruplesToTac(answer) == PrintQuadruplesToTac(Tac):
                pass
            else:
                print 'answer'
                print PrintQuadruplesToTac(answer)
                print PrintQuadruplesToTac(Tac)
                self.fail('string does not match')

class TestIfClausesSimpel(ParametrizedTestCase):

       def test_SimpleIfClauseWithoutElse(self):
        try:
            Tac = Yacc.forTesting('int main(){if(1){return 1;}}')
        except SyntaxError:
            self.fail('ExpectedException not thrown')
        else:
            answer = []
            answer.append(Yacc.Quadruple('0','function','None','None','main'))
            answer.append(Yacc.Quadruple('1','BeginFunc','0','None','main'))
            answer.append(Yacc.Quadruple('2','assign_number','1','None','_t0'))
            answer.append(Yacc.Quadruple('3','IfNode','_t0','None','_L0'))
            answer.append(Yacc.Quadruple('4','assign_number','1','None','_t1'))
            answer.append(Yacc.Quadruple('5','Return','_t1','None','None'))
            answer.append(Yacc.Quadruple('6','Label','None','None','_L0'))
            answer.append(Yacc.Quadruple('7','EndFunc','None','None','None'))
            if PrintQuadruplesToTac(answer) == PrintQuadruplesToTac(Tac):
                pass
            else:
                print 'answer'
                print PrintQuadruplesToTac(answer)
                print PrintQuadruplesToTac(Tac)
                self.fail('string does not match')

       def test_SimpleIfClauseWithElse(self):
        try:
            Tac = Yacc.forTesting('int main(){if(1){return 1;}else{return 2;}}')
        except SyntaxError:
            self.fail('ExpectedException not thrown')
        else:
            answer = []
            answer.append(Yacc.Quadruple('0','function','None','None','main'))
            answer.append(Yacc.Quadruple('1','BeginFunc','0','None','main'))
            answer.append(Yacc.Quadruple('2','assign_number','1','None','_t0'))
            answer.append(Yacc.Quadruple('3','IfNode','_t0','None','_L0'))
            answer.append(Yacc.Quadruple('4','assign_number','1','None','_t1'))
            answer.append(Yacc.Quadruple('5','Return','_t1','None','None'))
            answer.append(Yacc.Quadruple('6','Goto','None','None','_L1'))
            answer.append(Yacc.Quadruple('7','Label','None','None','_L0'))
            answer.append(Yacc.Quadruple('8','assign_number','2','None','_t2'))
            answer.append(Yacc.Quadruple('9','Return','_t2','None','None'))
            answer.append(Yacc.Quadruple('10','Label','None','None','_L1'))
            answer.append(Yacc.Quadruple('11','EndFunc','None','None','None'))
            if PrintQuadruplesToTac(answer) == PrintQuadruplesToTac(Tac):
                pass
            else:
                print 'answer'
                print PrintQuadruplesToTac(answer)
                print PrintQuadruplesToTac(Tac)
                self.fail('string does not match')

       def test_SimpleIfClauseWithElseInteger(self):
        try:
            Tac = Yacc.forTesting('int main(){if(x){int x; x = 5; return x;}else{int x; x = 6; return x;}}')
        except SyntaxError:
            self.fail('ExpectedException not thrown')
        else:
            answer = []
            answer.append(Yacc.Quadruple('0','function','None','None','main'))
            answer.append(Yacc.Quadruple('1','BeginFunc','0','None','main'))
            answer.append(Yacc.Quadruple('2','IfNode','x','None','_L0'))
            answer.append(Yacc.Quadruple('3','assign_number','5','None','_t0'))
            answer.append(Yacc.Quadruple('4','assign exp','_t0','None','x'))
            answer.append(Yacc.Quadruple('5','Return','x','None','None'))
            answer.append(Yacc.Quadruple('6','Goto','None','None','_L1'))
            answer.append(Yacc.Quadruple('7','Label','None','None','_L0'))
            answer.append(Yacc.Quadruple('8','assign_number','6','None','_t1'))
            answer.append(Yacc.Quadruple('9','assign exp','_t1','None','x'))
            answer.append(Yacc.Quadruple('10','Return','x','None','None'))
            answer.append(Yacc.Quadruple('11','Label','None','None','_L1'))
            answer.append(Yacc.Quadruple('12','EndFunc','None','None','None'))
            if PrintQuadruplesToTac(answer) == PrintQuadruplesToTac(Tac):
                pass
            else:
                print 'answer'
                print PrintQuadruplesToTac(answer)
                print PrintQuadruplesToTac(Tac)
                self.fail('string does not match')

       def test_SimpleIfClauseWithElseChar(self):
        try:
            Tac = Yacc.forTesting('int main(){if(x){char x; return x;}else{char x; x = 6; return x;}}')
        except SyntaxError:
            self.fail('ExpectedException not thrown')
        else:
            answer = []
            answer.append(Yacc.Quadruple('0','function','None','None','main'))
            answer.append(Yacc.Quadruple('1','BeginFunc','0','None','main'))
            answer.append(Yacc.Quadruple('2','IfNode','x','None','_L0'))
            answer.append(Yacc.Quadruple('3','Return','x','None','None'))
            answer.append(Yacc.Quadruple('4','Goto','None','None','_L1'))
            answer.append(Yacc.Quadruple('5','Label','None','None','_L0'))
            answer.append(Yacc.Quadruple('6','assign_number','6','None','_t0'))
            answer.append(Yacc.Quadruple('7','assign exp','_t0','None','x'))
            answer.append(Yacc.Quadruple('8','Return','x','None','None'))
            answer.append(Yacc.Quadruple('9','Label','None','None','_L1'))
            answer.append(Yacc.Quadruple('10','EndFunc','None','None','None'))
            if PrintQuadruplesToTac(answer) == PrintQuadruplesToTac(Tac):
                pass
            else:
                print 'answer'
                print PrintQuadruplesToTac(answer)
                print PrintQuadruplesToTac(Tac)
                self.fail('string does not match')

class TestIfClausesComplex(ParametrizedTestCase):

    def test_ComplexIfClauseNestedInBody(self):
        try:
            Tac = Yacc.forTesting('int main(){if(1){if(1){return 1;}else{return 2;}}else{return 2;}}')
        except SyntaxError:
            self.fail('ExpectedException not thrown')
        else:
            answer = []
            answer.append(Yacc.Quadruple('0','function','None','None','main'))
            answer.append(Yacc.Quadruple('1','BeginFunc','0','None','main'))
            answer.append(Yacc.Quadruple('2','assign_number','1','None','_t0'))
            answer.append(Yacc.Quadruple('3','IfNode','_t0','None','_L0'))
            answer.append(Yacc.Quadruple('4','assign_number','1','None','_t1'))
            answer.append(Yacc.Quadruple('5','IfNode','_t1','None','_L1'))
            answer.append(Yacc.Quadruple('6','assign_number','1','None','_t2'))
            answer.append(Yacc.Quadruple('7','Return','_t2','None','None'))
            answer.append(Yacc.Quadruple('8','Goto','None','None','_L2'))
            answer.append(Yacc.Quadruple('9','Label','None','None','_L1'))
            answer.append(Yacc.Quadruple('10','assign_number','2','None','_t3'))
            answer.append(Yacc.Quadruple('11','Return','_t3','None','None'))
            answer.append(Yacc.Quadruple('12','Label','None','None','_L2'))
            answer.append(Yacc.Quadruple('13','Goto','None','None','_L3'))
            answer.append(Yacc.Quadruple('14','Label','None','None','_L2'))
            answer.append(Yacc.Quadruple('15','assign_number','2','None','_t4'))
            answer.append(Yacc.Quadruple('16','Return','_t4','None','None'))
            answer.append(Yacc.Quadruple('17','Label','None','None','_L3'))
            answer.append(Yacc.Quadruple('18','EndFunc','None','None','None'))
            if PrintQuadruplesToTac(answer) == PrintQuadruplesToTac(Tac):
                pass
            else:
                print 'answer'
                print PrintQuadruplesToTac(answer)
                print PrintQuadruplesToTac(Tac)
                self.fail('string does not match')

    def test_ComplexIfClauseNestedInElse(self):
        try:
            Tac = Yacc.forTesting('int main(){if(1){return 2;}else{if(1){return 1;}else{return 2;}}}')
        except SyntaxError:
            self.fail('ExpectedException not thrown')
        else:
            answer = []
            answer.append(Yacc.Quadruple('0','function','None','None','main'))
            answer.append(Yacc.Quadruple('1','BeginFunc','0','None','main'))
            answer.append(Yacc.Quadruple('2','assign_number','1','None','_t0'))
            answer.append(Yacc.Quadruple('3','IfNode','_t0','None','_L0'))
            answer.append(Yacc.Quadruple('4','assign_number','2','None','_t1'))
            answer.append(Yacc.Quadruple('5','Return','_t1','None','None'))
            answer.append(Yacc.Quadruple('6','Goto','None','None','_L1'))
            answer.append(Yacc.Quadruple('7','Label','None','None','_L0'))
            answer.append(Yacc.Quadruple('8','assign_number','1','None','_t2'))
            answer.append(Yacc.Quadruple('9','IfNode','_t2','None','_L2'))
            answer.append(Yacc.Quadruple('10','assign_number','1','None','_t3'))
            answer.append(Yacc.Quadruple('11','Return','_t3','None','None'))
            answer.append(Yacc.Quadruple('12','Goto','None','None','_L3'))
            answer.append(Yacc.Quadruple('13','Label','None','None','_L2'))
            answer.append(Yacc.Quadruple('14','assign_number','2','None','_t4'))
            answer.append(Yacc.Quadruple('15','Return','_t4','None','None'))
            answer.append(Yacc.Quadruple('16','Label','None','None','_L3'))
            answer.append(Yacc.Quadruple('17','Label','None','None','_L1'))
            answer.append(Yacc.Quadruple('18','EndFunc','None','None','None'))
            if PrintQuadruplesToTac(answer) == PrintQuadruplesToTac(Tac):
                pass
            else:
                print 'answer'
                print PrintQuadruplesToTac(answer)
                print PrintQuadruplesToTac(Tac)
                self.fail('string does not match')

    def test_ComplexIfClauseNestedIntegerPollutionTest(self):
        try:
            Tac = Yacc.forTesting('int main(){if(1){int x; x = 5; if(1){return x;}else{return x;}}else{int x; x = 6; return x;}}')
        except SyntaxError:
            self.fail('ExpectedException not thrown')
        else:
            answer = []
            answer.append(Yacc.Quadruple('0','function','None','None','main'))
            answer.append(Yacc.Quadruple('1','BeginFunc','0','None','main'))
            answer.append(Yacc.Quadruple('2','assign_number','1','None','_t0'))
            answer.append(Yacc.Quadruple('3','IfNode','_t0','None','_L0'))
            answer.append(Yacc.Quadruple('4','assign_number','5','None','_t1'))
            answer.append(Yacc.Quadruple('5','assign exp','_t1','None','x'))
            answer.append(Yacc.Quadruple('6','assign_number','1','None','_t2'))
            answer.append(Yacc.Quadruple('7','IfNode','_t2','None','_L1'))
            answer.append(Yacc.Quadruple('8','Return','x','None','None'))
            answer.append(Yacc.Quadruple('9','Goto','None','None','_L2'))
            answer.append(Yacc.Quadruple('10','Label','None','None','_L1'))
            answer.append(Yacc.Quadruple('11','Return','x','None','None'))
            answer.append(Yacc.Quadruple('12','Label','None','None','_L2'))
            answer.append(Yacc.Quadruple('13','Goto','None','None','_L3'))
            answer.append(Yacc.Quadruple('14','Label','None','None','_L2'))
            answer.append(Yacc.Quadruple('15','assign_number','6','None','_t3'))
            answer.append(Yacc.Quadruple('16','assign exp','_t3','None','x'))
            answer.append(Yacc.Quadruple('17','Return','x','None','None'))
            answer.append(Yacc.Quadruple('18','Label','None','None','_L3'))
            answer.append(Yacc.Quadruple('19','EndFunc','None','None','None'))
            if PrintQuadruplesToTac(answer) == PrintQuadruplesToTac(Tac):
                pass
            else:
                print 'answer'
                print PrintQuadruplesToTac(answer)
                print PrintQuadruplesToTac(Tac)
                self.fail('string does not match')

    def test_ComplexIfClauseNestedIntegerPollutionTestWithVarDeclaOutside(self):
        try:
            Tac = Yacc.forTesting('int main(){int x; x = 8; if(1){int x; x = 5; if(1){return x;}else{return x;}}else{int x; x = 6; return x;}}')
        except SyntaxError:
            self.fail('ExpectedException not thrown')
        else:
            answer = []
            answer.append(Yacc.Quadruple('0','function','None','None','main'))
            answer.append(Yacc.Quadruple('1','BeginFunc','0','None','main'))
            answer.append(Yacc.Quadruple('2','assign_number','8','None','_t0'))
            answer.append(Yacc.Quadruple('3','assign exp','_t0','None','x'))
            answer.append(Yacc.Quadruple('4','assign_number','1','None','_t1'))
            answer.append(Yacc.Quadruple('5','IfNode','_t1','None','_L0'))
            answer.append(Yacc.Quadruple('6','assign_number','5','None','_t2'))
            answer.append(Yacc.Quadruple('7','assign exp','_t2','None','x'))
            answer.append(Yacc.Quadruple('8','assign_number','1','None','_t3'))
            answer.append(Yacc.Quadruple('9','IfNode','_t3','None','_L1'))
            answer.append(Yacc.Quadruple('10','Return','x','None','None'))
            answer.append(Yacc.Quadruple('11','Goto','None','None','_L2'))
            answer.append(Yacc.Quadruple('12','Label','None','None','_L1'))
            answer.append(Yacc.Quadruple('13','Return','x','None','None'))
            answer.append(Yacc.Quadruple('14','Label','None','None','_L2'))
            answer.append(Yacc.Quadruple('15','Goto','None','None','_L3'))
            answer.append(Yacc.Quadruple('16','Label','None','None','_L2'))
            answer.append(Yacc.Quadruple('17','assign_number','6','None','_t4'))
            answer.append(Yacc.Quadruple('18','assign exp','_t4','None','x'))
            answer.append(Yacc.Quadruple('19','Return','x','None','None'))
            answer.append(Yacc.Quadruple('20','Label','None','None','_L3'))
            answer.append(Yacc.Quadruple('21','EndFunc','None','None','None'))
            if PrintQuadruplesToTac(answer) == PrintQuadruplesToTac(Tac):
                pass
            else:
                print 'answer'
                print PrintQuadruplesToTac(answer)
                print PrintQuadruplesToTac(Tac)
                self.fail('string does not match')

class TestWhileSimple(ParametrizedTestCase):

     def test_SimpleWhile(self):
        try:
            Tac = Yacc.forTesting('int main(){ while (1) {return x;}}')
        except SyntaxError:
            self.fail('ExpectedException not thrown')
        else:
            answer = []
            answer.append(Yacc.Quadruple('0','function','None','None','main'))
            answer.append(Yacc.Quadruple('1','BeginFunc','0','None','main'))
            answer.append(Yacc.Quadruple('2','Label','None','None','_L0'))
            answer.append(Yacc.Quadruple('3','assign_number','1','None','_t0'))
            answer.append(Yacc.Quadruple('4','IfNode','_t0','None','_L1'))
            answer.append(Yacc.Quadruple('5','Return','x','None','None'))
            answer.append(Yacc.Quadruple('6','Goto','None','None','_L0'))
            answer.append(Yacc.Quadruple('7','Label','None','None','_L1'))
            answer.append(Yacc.Quadruple('8','EndFunc','None','None','None'))
            if PrintQuadruplesToTac(answer) == PrintQuadruplesToTac(Tac):
                pass
            else:
                print 'answer'
                print PrintQuadruplesToTac(answer)
                print PrintQuadruplesToTac(Tac)
                self.fail('string does not match')

     def test_SimpleWhileWithEqualExp(self):
        try:
            Tac = Yacc.forTesting('int main(){int y; int x; x = 5; y = 0; while (y == 5) { y = y + 1 ;return x;}}')
        except SyntaxError:
            self.fail('ExpectedException not thrown')
        else:
            answer = []
            answer.append(Yacc.Quadruple('0','function','None','None','main'))
            answer.append(Yacc.Quadruple('1','BeginFunc','0','None','main'))
            answer.append(Yacc.Quadruple('2','assign_number','5','None','_t0'))
            answer.append(Yacc.Quadruple('3','assign exp','_t0','None','x'))
            answer.append(Yacc.Quadruple('4','assign_number','0','None','_t1'))
            answer.append(Yacc.Quadruple('5','assign exp','_t1','None','y'))
            answer.append(Yacc.Quadruple('6','Label','None','None','_L0'))
            answer.append(Yacc.Quadruple('7','assign_number','5','None','_t2'))
            answer.append(Yacc.Quadruple('8','==','y','_t2','_t3'))
            answer.append(Yacc.Quadruple('9','IfNode','_t3','None','_L1'))
            answer.append(Yacc.Quadruple('10','assign_number','1','None','_t4'))
            answer.append(Yacc.Quadruple('11','+','y','_t4','_t5'))
            answer.append(Yacc.Quadruple('12','assign exp','_t5','None','y'))
            answer.append(Yacc.Quadruple('13','Return','x','None','None'))
            answer.append(Yacc.Quadruple('14','Goto','None','None','_L0'))
            answer.append(Yacc.Quadruple('15','Label','None','None','_L1'))
            answer.append(Yacc.Quadruple('16','EndFunc','None','None','None'))
            if PrintQuadruplesToTac(answer) == PrintQuadruplesToTac(Tac):
                pass
            else:
                print 'answer'
                print PrintQuadruplesToTac(answer)
                print PrintQuadruplesToTac(Tac)
                self.fail('string does not match')

     def test_SimpleWhileWithGreaterExp(self):
        try:
            Tac = Yacc.forTesting('int main(){int y; int x; x = 5; y = 0; while (y < 5) { y = y + 1 ;return x;}}')
        except SyntaxError:
            self.fail('ExpectedException not thrown')
        else:
            answer = []
            answer.append(Yacc.Quadruple('0','function','None','None','main'))
            answer.append(Yacc.Quadruple('1','BeginFunc','0','None','main'))
            answer.append(Yacc.Quadruple('2','assign_number','5','None','_t0'))
            answer.append(Yacc.Quadruple('3','assign exp','_t0','None','x'))
            answer.append(Yacc.Quadruple('4','assign_number','0','None','_t1'))
            answer.append(Yacc.Quadruple('5','assign exp','_t1','None','y'))
            answer.append(Yacc.Quadruple('6','Label','None','None','_L0'))
            answer.append(Yacc.Quadruple('7','assign_number','5','None','_t2'))
            answer.append(Yacc.Quadruple('8','<','y','_t2','_t3'))
            answer.append(Yacc.Quadruple('9','IfNode','_t3','None','_L1'))
            answer.append(Yacc.Quadruple('10','assign_number','1','None','_t4'))
            answer.append(Yacc.Quadruple('11','+','y','_t4','_t5'))
            answer.append(Yacc.Quadruple('12','assign exp','_t5','None','y'))
            answer.append(Yacc.Quadruple('13','Return','x','None','None'))
            answer.append(Yacc.Quadruple('14','Goto','None','None','_L0'))
            answer.append(Yacc.Quadruple('15','Label','None','None','_L1'))
            answer.append(Yacc.Quadruple('16','EndFunc','None','None','None'))
            if PrintQuadruplesToTac(answer) == PrintQuadruplesToTac(Tac):
                pass
            else:
                print 'answer'
                print PrintQuadruplesToTac(answer)
                print PrintQuadruplesToTac(Tac)
                self.fail('string does not match')

     def test_SimpleWhileWithLessExp(self):
        try:
            Tac = Yacc.forTesting('int main(){int y; int x; x = 5; y = 0; while (y > 5) { y = y + 1 ;return x;}}')
        except SyntaxError:
            self.fail('ExpectedException not thrown')
        else:
            answer = []
            answer.append(Yacc.Quadruple('0','function','None','None','main'))
            answer.append(Yacc.Quadruple('1','BeginFunc','0','None','main'))
            answer.append(Yacc.Quadruple('2','assign_number','5','None','_t0'))
            answer.append(Yacc.Quadruple('3','assign exp','_t0','None','x'))
            answer.append(Yacc.Quadruple('4','assign_number','0','None','_t1'))
            answer.append(Yacc.Quadruple('5','assign exp','_t1','None','y'))
            answer.append(Yacc.Quadruple('6','Label','None','None','_L0'))
            answer.append(Yacc.Quadruple('7','assign_number','5','None','_t2'))
            answer.append(Yacc.Quadruple('8','>','y','_t2','_t3'))
            answer.append(Yacc.Quadruple('9','IfNode','_t3','None','_L1'))
            answer.append(Yacc.Quadruple('10','assign_number','1','None','_t4'))
            answer.append(Yacc.Quadruple('11','+','y','_t4','_t5'))
            answer.append(Yacc.Quadruple('12','assign exp','_t5','None','y'))
            answer.append(Yacc.Quadruple('13','Return','x','None','None'))
            answer.append(Yacc.Quadruple('14','Goto','None','None','_L0'))
            answer.append(Yacc.Quadruple('15','Label','None','None','_L1'))
            answer.append(Yacc.Quadruple('16','EndFunc','None','None','None'))
            if PrintQuadruplesToTac(answer) == PrintQuadruplesToTac(Tac):
                pass
            else:
                print 'answer'
                print PrintQuadruplesToTac(answer)
                print PrintQuadruplesToTac(Tac)
                self.fail('string does not match')

     def test_SimpleWhileWithNotEqualExp(self):
        try:
            Tac = Yacc.forTesting('int main(){int y; int x; x = 5; y = 0; while (y != 5) { y = y + 1 ;return x;}}')
        except SyntaxError:
            self.fail('ExpectedException not thrown')
        else:
            answer = []
            answer.append(Yacc.Quadruple('0','function','None','None','main'))
            answer.append(Yacc.Quadruple('1','BeginFunc','0','None','main'))
            answer.append(Yacc.Quadruple('2','assign_number','5','None','_t0'))
            answer.append(Yacc.Quadruple('3','assign exp','_t0','None','x'))
            answer.append(Yacc.Quadruple('4','assign_number','0','None','_t1'))
            answer.append(Yacc.Quadruple('5','assign exp','_t1','None','y'))
            answer.append(Yacc.Quadruple('6','Label','None','None','_L0'))
            answer.append(Yacc.Quadruple('7','assign_number','5','None','_t2'))
            answer.append(Yacc.Quadruple('8','!=','y','_t2','_t3'))
            answer.append(Yacc.Quadruple('9','IfNode','_t3','None','_L1'))
            answer.append(Yacc.Quadruple('10','assign_number','1','None','_t4'))
            answer.append(Yacc.Quadruple('11','+','y','_t4','_t5'))
            answer.append(Yacc.Quadruple('12','assign exp','_t5','None','y'))
            answer.append(Yacc.Quadruple('13','Return','x','None','None'))
            answer.append(Yacc.Quadruple('14','Goto','None','None','_L0'))
            answer.append(Yacc.Quadruple('15','Label','None','None','_L1'))
            answer.append(Yacc.Quadruple('16','EndFunc','None','None','None'))
            if PrintQuadruplesToTac(answer) == PrintQuadruplesToTac(Tac):
                pass
            else:
                print 'answer'
                print PrintQuadruplesToTac(answer)
                print PrintQuadruplesToTac(Tac)
                self.fail('string does not match')

class TestMultipleFunctionsCallingEachOther(ParametrizedTestCase):
     def test_TwoFunctions(self):
        try:
            Tac = Yacc.forTesting('int main(){return 2;} int test(){return 3;}')
        except SyntaxError:
            self.fail('ExpectedException not thrown')
        else:
            answer = []
            answer.append(Yacc.Quadruple('0','function','None','None','main'))
            answer.append(Yacc.Quadruple('1','BeginFunc','0','None','main'))
            answer.append(Yacc.Quadruple('2','assign_number','2','None','_t0'))
            answer.append(Yacc.Quadruple('3','Return','_t0','None','None'))
            answer.append(Yacc.Quadruple('4','EndFunc','None','None','None'))
            answer.append(Yacc.Quadruple('5','function','None','None','test'))
            answer.append(Yacc.Quadruple('6','BeginFunc','0','None','test'))
            answer.append(Yacc.Quadruple('7','assign_number','3','None','_t1'))
            answer.append(Yacc.Quadruple('8','Return','_t1','None','None'))
            answer.append(Yacc.Quadruple('9','EndFunc','None','None','None'))
            if PrintQuadruplesToTac(answer) == PrintQuadruplesToTac(Tac):
                pass
            else:
                print 'answer'
                print PrintQuadruplesToTac(answer)
                print PrintQuadruplesToTac(Tac)
                self.fail('string does not match')

     def test_TwoFunctionsCallingEachOther(self):
        try:
            Tac = Yacc.forTesting('int main(int x){return 2;} int test(){main(x)}')
        except SyntaxError:
            self.fail('ExpectedException not thrown')
        else:
            answer = []
            answer.append(Yacc.Quadruple('0','function','None','None','main'))
            answer.append(Yacc.Quadruple('1','BeginFunc','0','None','main'))
            answer.append(Yacc.Quadruple('2','assign_number','2','None','_t0'))
            answer.append(Yacc.Quadruple('3','Return','_t0','None','None'))
            answer.append(Yacc.Quadruple('4','EndFunc','None','None','None'))
            answer.append(Yacc.Quadruple('5','function','None','None','test'))
            answer.append(Yacc.Quadruple('6','BeginFunc','0','None','test'))
            answer.append(Yacc.Quadruple('7','PushParam','x','None','None'))
            answer.append(Yacc.Quadruple('8','LCall','main','None','None'))
            answer.append(Yacc.Quadruple('9','PopParams','0','None','None'))
            answer.append(Yacc.Quadruple('10','EndFunc','None','None','None'))
            if PrintQuadruplesToTac(answer) == PrintQuadruplesToTac(Tac):
                pass
            else:
                print 'answer'
                print PrintQuadruplesToTac(answer)
                print PrintQuadruplesToTac(Tac)
                self.fail('string does not match')

     def test_TwoFunctionsCallingEachOtherReversed(self):
        try:
            Tac = Yacc.forTesting('int test(){main(x)} int main(int x){return 2;}')
        except SyntaxError:
            self.fail('ExpectedException not thrown')
        else:
            answer = []
            answer.append(Yacc.Quadruple('0','function','None','None','test'))
            answer.append(Yacc.Quadruple('1','BeginFunc','0','None','test'))
            answer.append(Yacc.Quadruple('2','PushParam','x','None','None'))
            answer.append(Yacc.Quadruple('3','LCall','main','None','None'))
            answer.append(Yacc.Quadruple('4','PopParams','0','None','None'))
            answer.append(Yacc.Quadruple('5','EndFunc','None','None','None'))
            answer.append(Yacc.Quadruple('6','function','None','None','main'))
            answer.append(Yacc.Quadruple('7','BeginFunc','0','None','main'))
            answer.append(Yacc.Quadruple('8','assign_number','2','None','_t0'))
            answer.append(Yacc.Quadruple('9','Return','_t0','None','None'))
            answer.append(Yacc.Quadruple('10','EndFunc','None','None','None'))
            if PrintQuadruplesToTac(answer) == PrintQuadruplesToTac(Tac):
                pass
            else:
                print 'answer'
                print PrintQuadruplesToTac(answer)
                print PrintQuadruplesToTac(Tac)
                self.fail('string does not match')

     def test_TwoFunctionsCallingEachOtherNestedInIF(self):
        try:
            Tac = Yacc.forTesting('int test(){if (main(x)){main(x)} else {main(x)}} int main(int x){return 2;}')
        except SyntaxError:
            self.fail('ExpectedException not thrown')
        else:
            answer = []
            answer.append(Yacc.Quadruple('0','function','None','None','test'))
            answer.append(Yacc.Quadruple('1','BeginFunc','0','None','test'))
            answer.append(Yacc.Quadruple('2','PushParam','x','None','None'))
            answer.append(Yacc.Quadruple('3','LCall','main','None','_t0'))
            answer.append(Yacc.Quadruple('4','PopParams','0','None','None'))
            answer.append(Yacc.Quadruple('5','IfNode','_t0','None','_L0'))
            answer.append(Yacc.Quadruple('6','PushParam','x','None','None'))
            answer.append(Yacc.Quadruple('7','LCall','main','None','None'))
            answer.append(Yacc.Quadruple('8','PopParams','0','None','None'))
            answer.append(Yacc.Quadruple('9','Goto','None','None','_L1'))
            answer.append(Yacc.Quadruple('10','Label','None','None','_L0'))
            answer.append(Yacc.Quadruple('11','PushParam','x','None','None'))
            answer.append(Yacc.Quadruple('12','LCall','main','None','None'))
            answer.append(Yacc.Quadruple('13','PopParams','0','None','None'))
            answer.append(Yacc.Quadruple('14','Label','None','None','_L1'))
            answer.append(Yacc.Quadruple('15','EndFunc','None','None','None'))
            answer.append(Yacc.Quadruple('16','function','None','None','main'))
            answer.append(Yacc.Quadruple('17','BeginFunc','0','None','main'))
            answer.append(Yacc.Quadruple('18','assign_number','2','None','_t1'))
            answer.append(Yacc.Quadruple('19','Return','_t1','None','None'))
            answer.append(Yacc.Quadruple('20','EndFunc','None','None','None'))
            if PrintQuadruplesToTac(answer) == PrintQuadruplesToTac(Tac):
                pass
            else:
                print 'answer'
                print PrintQuadruplesToTac(answer)
                print PrintQuadruplesToTac(Tac)
                self.fail('string does not match')


     def test_Recursion(self):
        try:
            Tac = Yacc.forTesting('int main(int x) { main(x)}')
        except SyntaxError:
            self.fail('ExpectedException not thrown')
        else:
            answer = []
            answer.append(Yacc.Quadruple('0','function','None','None','main'))
            answer.append(Yacc.Quadruple('1','BeginFunc','0','None','main'))
            answer.append(Yacc.Quadruple('2','PushParam','x','None','None'))
            answer.append(Yacc.Quadruple('3','LCall','main','None','None'))
            answer.append(Yacc.Quadruple('4','PopParams','0','None','None'))
            answer.append(Yacc.Quadruple('5','EndFunc','None','None','None'))
            if PrintQuadruplesToTac(answer) == PrintQuadruplesToTac(Tac):
                pass
            else:
                print 'answer'
                print PrintQuadruplesToTac(answer)
                print PrintQuadruplesToTac(Tac)
                self.fail('string does not match')

class TestExamVerMeirTest(ParametrizedTestCase):
    def test_Exam1(self):
        try:
            Tac = Yacc.forTesting('''
                int factorial(int xParamOfFactorial)
                {
                    int result;
                    result = xParamOfFactorial * factorial(xParamOfFactorial - 1);
                }
                int main(int mainPAram)
                {
                    int factorialInput;
                    factorialInput = 5;
                    return factorial(factorialInput);
                }

            ''')
        except SyntaxError:
            self.fail('ExpectedException not thrown')
        else:
            answer = []
            answer.append(Yacc.Quadruple('0','function','None','None','factorial'))
            answer.append(Yacc.Quadruple('1','BeginFunc','0','None','factorial'))
            answer.append(Yacc.Quadruple('2','assign_number','1','None','_t0'))
            answer.append(Yacc.Quadruple('3','-','xParamOfFactorial','_t0','_t1'))
            answer.append(Yacc.Quadruple('4','PushParam','_t1','None','None'))
            answer.append(Yacc.Quadruple('5','LCall','factorial','None','_t2'))
            answer.append(Yacc.Quadruple('6','PopParams','0','None','None'))
            answer.append(Yacc.Quadruple('7','*','xParamOfFactorial','_t2','_t3'))
            answer.append(Yacc.Quadruple('8','assign exp','_t3','None','result'))
            answer.append(Yacc.Quadruple('9','EndFunc','None','None','None'))
            answer.append(Yacc.Quadruple('10','function','None','None','main'))
            answer.append(Yacc.Quadruple('11','BeginFunc','0','None','main'))
            answer.append(Yacc.Quadruple('12','assign_number','5','None','_t4'))
            answer.append(Yacc.Quadruple('13','assign exp','_t4','None','factorialInput'))
            answer.append(Yacc.Quadruple('14','PushParam','factorialInput','None','None'))
            answer.append(Yacc.Quadruple('15','LCall','factorial','None','_t5'))
            answer.append(Yacc.Quadruple('16','PopParams','0','None','None'))
            answer.append(Yacc.Quadruple('17','Return','_t5','None','None'))
            answer.append(Yacc.Quadruple('18','EndFunc','None','None','None'))
            if PrintQuadruplesToTac(answer) == PrintQuadruplesToTac(Tac):
                pass
            else:
                print 'answer'
                print PrintQuadruplesToTac(answer)
                print PrintQuadruplesToTac(Tac)
                self.fail('string does not match')

    def test_Exam2(self):
        try:
            Tac = Yacc.forTesting('''
                int ackermann(int m int n){
                if (m == 0) {return n + 1};
                if (n == 0) {return ackermann(m - 1, 1)};
                return ackermann(m - 1, ackermann(m, n - 1));
                }

            ''')
        except SyntaxError:
            self.fail('ExpectedException not thrown')
        else:
            answer = []
            answer.append(Yacc.Quadruple('0','function','None','None','ackermann'))
            answer.append(Yacc.Quadruple('1','BeginFunc','0','None','ackermann'))
            answer.append(Yacc.Quadruple('2','assign_number','0','None','_t0'))
            answer.append(Yacc.Quadruple('3','==','m','_t0','_t1'))
            answer.append(Yacc.Quadruple('4','IfNode','_t1','None','_L0'))
            answer.append(Yacc.Quadruple('5','assign_number','1','None','_t2'))
            answer.append(Yacc.Quadruple('6','+','n','_t2','_t3'))
            answer.append(Yacc.Quadruple('7','Return','_t3','None','None'))
            answer.append(Yacc.Quadruple('8','Label','None','None','_L0'))
            answer.append(Yacc.Quadruple('9','assign_number','0','None','_t4'))
            answer.append(Yacc.Quadruple('10','==','n','_t4','_t5'))
            answer.append(Yacc.Quadruple('11','IfNode','_t5','None','_L1'))
            answer.append(Yacc.Quadruple('12','assign_number','1','None','_t6'))
            answer.append(Yacc.Quadruple('13','-','m','_t6','_t7'))
            answer.append(Yacc.Quadruple('14','assign_number','1','None','_t8'))
            answer.append(Yacc.Quadruple('15','LCall','ackermann','None','_t9'))
            answer.append(Yacc.Quadruple('16','PopParams','0','None','None'))
            answer.append(Yacc.Quadruple('17','Return','_t9','None','None'))
            answer.append(Yacc.Quadruple('18','Label','None','None','_L1'))
            answer.append(Yacc.Quadruple('19','assign_number','1','None','_t10'))
            answer.append(Yacc.Quadruple('20','-','m','_t10','_t11'))
            answer.append(Yacc.Quadruple('21','assign_number','1','None','_t12'))
            answer.append(Yacc.Quadruple('22','-','n','_t12','_t13'))
            answer.append(Yacc.Quadruple('23','LCall','ackermann','None','_t14'))
            answer.append(Yacc.Quadruple('24','PopParams','0','None','None'))
            answer.append(Yacc.Quadruple('25','LCall','ackermann','None','_t15'))
            answer.append(Yacc.Quadruple('26','PopParams','0','None','None'))
            answer.append(Yacc.Quadruple('27','Return','_t15','None','None'))
            answer.append(Yacc.Quadruple('28','EndFunc','None','None','None'))
            if PrintQuadruplesToTac(answer) == PrintQuadruplesToTac(Tac):
                pass
            else:
                print 'answer'
                print PrintQuadruplesToTac(answer)
                print PrintQuadruplesToTac(Tac)
                self.fail('string does not match')
    def test_Exam3(self):
        try:
            Tac = Yacc.forTesting('''
               int main()
                {
                if(x == 5)
                {
                    x = 2;
                }
                else
                {
                    x = 3;
                };

                while(x == 4)
                {
                    x = x - 1;
                };
                }

            ''')
        except SyntaxError:
            self.fail('ExpectedException not thrown')
        else:
            answer = []
            answer.append(Yacc.Quadruple('0','function','None','None','main'))
            answer.append(Yacc.Quadruple('1','BeginFunc','0','None','main'))
            answer.append(Yacc.Quadruple('2','assign_number','5','None','_t0'))
            answer.append(Yacc.Quadruple('3','==','x','_t0','_t1'))
            answer.append(Yacc.Quadruple('4','IfNode','_t1','None','_L0'))
            answer.append(Yacc.Quadruple('5','assign_number','2','None','_t2'))
            answer.append(Yacc.Quadruple('6','assign exp','_t2','None','x'))
            answer.append(Yacc.Quadruple('7','Goto','None','None','_L1'))
            answer.append(Yacc.Quadruple('8','Label','None','None','_L0'))
            answer.append(Yacc.Quadruple('9','assign_number','3','None','_t3'))
            answer.append(Yacc.Quadruple('10','assign exp','_t3','None','x'))
            answer.append(Yacc.Quadruple('11','Label','None','None','_L1'))
            answer.append(Yacc.Quadruple('12','Label','None','None','_L2'))
            answer.append(Yacc.Quadruple('13','assign_number','4','None','_t4'))
            answer.append(Yacc.Quadruple('14','==','x','_t4','_t5'))
            answer.append(Yacc.Quadruple('15','IfNode','_t5','None','_L3'))
            answer.append(Yacc.Quadruple('16','assign_number','1','None','_t6'))
            answer.append(Yacc.Quadruple('17','-','x','_t6','_t7'))
            answer.append(Yacc.Quadruple('18','assign exp','_t7','None','x'))
            answer.append(Yacc.Quadruple('19','Goto','None','None','_L2'))
            answer.append(Yacc.Quadruple('20','Label','None','None','_L3'))
            answer.append(Yacc.Quadruple('21','EndFunc','None','None','None'))
            if PrintQuadruplesToTac(answer) == PrintQuadruplesToTac(Tac):
                pass
            else:
                print 'answer'
                print PrintQuadruplesToTac(answer)
                print PrintQuadruplesToTac(Tac)
                self.fail('string does not match')

    def test_Exam4(self):
        try:
            Tac = Yacc.forTesting('''
             int f(int x)
            {
                return 0;
            }

            ''')
        except SyntaxError:
            self.fail('ExpectedException not thrown')
        else:
            answer = []
            answer.append(Yacc.Quadruple('0','function','None','None','f'))
            answer.append(Yacc.Quadruple('1','BeginFunc','0','None','f'))
            answer.append(Yacc.Quadruple('2','assign_number','0','None','_t0'))
            answer.append(Yacc.Quadruple('3','Return','_t0','None','None'))
            answer.append(Yacc.Quadruple('4','EndFunc','None','None','None'))
            if PrintQuadruplesToTac(answer) == PrintQuadruplesToTac(Tac):
                pass
            else:
                print 'answer'
                print PrintQuadruplesToTac(answer)
                print PrintQuadruplesToTac(Tac)
                self.fail('string does not match')