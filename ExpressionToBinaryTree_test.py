import Expression.Expression as Expression
import unittest
from unittest.mock import patch
class TestExpressionToBinaryTree(unittest.TestCase):
    @patch('builtins.input')
    # @patch('builtins.print')
    def test_normal(self, mock_input):
        mock_input.side_effect = ['(1+2)']
        expression=Expression.Expression()
        self.assertEqual(expression.Check(),0)
        box=[['@','@','+','@','@'],['@','/','@','\\','@'],['1','@','@','@','2']]
        self.assertEqual(expression.DrawTree(),(1+2,box))
    # def test_WrongNumber(self,mock_input):
    #     mock_input.side_effect = ['(4*3*2)']
    #     expression=Expression.Expression()
    #     err='Not a valid expression, wrong number of operands.'
    #     self.assertEqual(expression.Check(),err)