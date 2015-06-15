__author__ = 'demathieu'

import unittest
import LexTest as LexTest
import YaccTestVarDecla as YaccTestVarDecla
import YaccTestSimpleFunction as YaccTestSimpleFunction
import YaccTestLoops as YaccTestLoops


testList = [
['INT','int'],
['IF','if'],
['ELSE','else'],
['NEQUAL','!='],
['RETURN','return'],
['LPAR','('],
['RPAR',')'],
['LBRACE','{'],
['RBRACE','}'],
['LBRACK','['],
['RBRACK',']'],
['ASSIGN','='],
['SEMICOLON',';'],
['PLUS','+'],
['MINUS','-'],
['TIMES','*'],
['DIVIDE','/'],
['EQUAL','=='],
['CHAR','char'],
['WRITE','write'],
['READ','read'],
['GREATER','>'],
['LESS','<'],
['NOT','!'],
['LENGTH','length'],
['WHILE','while'],
['NAME','naam']
]
suite = unittest.TestSuite()
# for test in testList:
#      if test != None:
#          suite.addTest(LexTest.ParametrizedTestCase.parametrize(LexTest.TestTokenDefault, param =test))
# suite.addTest(LexTest.ParametrizedTestCase.parametrize(LexTest.TestTokenName))
# suite.addTest(LexTest.ParametrizedTestCase.parametrize(LexTest.TestTokenNumber))
# suite.addTest(YaccTestVarDecla.ParametrizedTestCase.parametrize(YaccTestVarDecla.TestIntegerVarDeclarations))
# suite.addTest(YaccTestVarDecla.ParametrizedTestCase.parametrize(YaccTestVarDecla.TestCharVarDeclarations))
# suite.addTest(YaccTestVarDecla.ParametrizedTestCase.parametrize(YaccTestVarDecla.TestIntegerAndCharCombined))
# suite.addTest(YaccTestSimpleFunction.ParametrizedTestCase.parametrize(YaccTestSimpleFunction.TestSimpleFunctionNoParamsNoBody))
# suite.addTest(YaccTestSimpleFunction.ParametrizedTestCase.parametrize(YaccTestSimpleFunction.TestSimpleFunctionNoParamsWithSimpleBodyAndVarDeclaration))
# suite.addTest(YaccTestSimpleFunction.ParametrizedTestCase.parametrize(YaccTestSimpleFunction.TestSimpleFunctionNoParamsWithVarInitialization))
# suite.addTest(YaccTestLoops.ParametrizedTestCase.parametrize(YaccTestLoops.TestIfClauseWithoutElse))
# suite.addTest(YaccTestLoops.ParametrizedTestCase.parametrize(YaccTestLoops.TestIfClauseWitElseButNotUsed))
#suite.addTest(YaccTestLoops.ParametrizedTestCase.parametrize(YaccTestLoops.TestIfClauseBody))
suite.addTest(YaccTestLoops.ParametrizedTestCase.parametrize(YaccTestLoops.TestWhileLoop))
unittest.TextTestRunner(verbosity=3).run(suite)