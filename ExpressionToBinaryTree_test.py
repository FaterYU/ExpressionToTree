import Expression.Expression as Expression
import unittest
from unittest.mock import patch
# error index and message:
# 0: 'Not a valid expression, wrong number of operands.',
# 1: 'Not a valid expression, operator missing.',
# 2: 'Not a valid expression, brackets mismatched.',
# 3: 'Not a valid expression, expression contains invalid characters.',
# 4: 'Not a valid expression, expression should not be empty.'
class TestExpressionToBinaryTree(unittest.TestCase):
    @patch('builtins.input')
    def test_NormalInput(self, mock_input):
        # normal expression input
        mock_input.side_effect = ['(1+2)']
        expression=Expression.Expression()
        self.assertEqual(expression.Check(),0)
        box=[['@','@','+','@','@'],['@','/','@','\\','@'],['1','@','@','@','2']]
        self.assertEqual(expression.DrawTree(),(1+2,box))
    @patch('builtins.input')
    def test_WrongNumber(self,mock_input):
        # Not a valid expression, wrong number of operands.
        mock_input.side_effect = ['(4*3*2)', '(4*(2))', '(4*(3+2)*(2+1))']
        for _ in range(3):
            expression = Expression.Expression()
            expression.Check()
            self.assertEqual(expression.err, [0])
    @patch('builtins.input')
    def test_OperatorMissing(self, mock_input):
        # Not a valid expression, operator missing.
        mock_input.side_effect = ['(((2+3)*(4*5))+(1(2+3)))']
        expression = Expression.Expression()
        expression.Check()
        self.assertEqual(expression.err, [1])
    @patch('builtins.input')
    def test_BracketsMismatched(self, mock_input):
        # Not a valid expression, brackets mismatched.
        mock_input.side_effect = ['(2*4)*(3+2)', '((2+3)*(4*5)', '(2+5)*(4/(2+2)))']
        for _ in range(3):
            expression=Expression.Expression()
            expression.Check()
            self.assertEqual(expression.err,[3])
    @patch('builtins.input')
    def test_BothErr(self, mock_input):
        # both of three errors
        mock_input.side_effect = ['(4*3*3(2)))']
        expression = Expression.Expression()
        expression.Check()
        self.assertEqual(expression.err, [0,1,3])
    @patch('builtins.input')
    def test_NormalReload(self, mock_input):
        # normal reload
        mock_input.side_effect = ['(1+2)','y']
        expression=Expression.Expression()
        expression.Check()
        expression_reload=Expression.Expression(is_reload=True)
        self.assertEqual(expression_reload.Check(),0)
        box=[['@','@','+','@','@'],['@','/','@','\\','@'],['1','@','@','@','2']]
        self.assertEqual(expression.DrawTree(),(1+2,box))
    @patch('builtins.input')
    def test_OtherTypeInput(self, mock_input):
        # other type input
        mock_input.side_effect = ['abc','\n','\0','`exit`']
        for _ in range(4):
            expression=Expression.Expression()
            expression.Check()
            self.assertEqual(expression.err,[2,3])
    @patch('builtins.input')
    def test_EmptyInput(self, mock_input):
        # empty input
        mock_input.side_effect = ['']
        expression=Expression.Expression()
        expression.Check()
        self.assertEqual(expression.err,[4])