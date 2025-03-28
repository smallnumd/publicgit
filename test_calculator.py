import unittest
from calculator import Calculator, CalculatorError

class TestCalculator(unittest.TestCase):
    """计算器测试类"""
    
    def setUp(self):
        """测试前的准备工作"""
        self.calc = Calculator()
    
    def test_add(self):
        """测试加法运算"""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertEqual(self.calc.add(1.5, 2.5), 4.0)
    
    def test_subtract(self):
        """测试减法运算"""
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(1, 1), 0)
        self.assertEqual(self.calc.subtract(0, 5), -5)
        self.assertEqual(self.calc.subtract(2.5, 1.5), 1.0)
    
    def test_multiply(self):
        """测试乘法运算"""
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        self.assertEqual(self.calc.multiply(0, 5), 0)
        self.assertEqual(self.calc.multiply(1.5, 2), 3.0)
    
    def test_divide(self):
        """测试除法运算"""
        self.assertEqual(self.calc.divide(6, 2), 3)
        self.assertEqual(self.calc.divide(5, 2), 2.5)
        self.assertEqual(self.calc.divide(0, 5), 0)
        self.assertEqual(self.calc.divide(3.6, 1.2), 3.0)
        
        # 测试除零错误
        with self.assertRaises(CalculatorError):
            self.calc.divide(5, 0)
    
    def test_calculate(self):
        """测试计算器功能"""
        # 测试正常运算
        self.assertEqual(self.calc.calculate(10, 5, '+'), 15)
        self.assertEqual(self.calc.calculate(10, 5, '-'), 5)
        self.assertEqual(self.calc.calculate(10, 5, '*'), 50)
        self.assertEqual(self.calc.calculate(10, 5, '/'), 2)
        
        # 测试除零错误
        with self.assertRaises(CalculatorError):
            self.calc.calculate(10, 0, '/')
        
        # 测试无效运算符
        with self.assertRaises(CalculatorError):
            self.calc.calculate(10, 5, '%')

if __name__ == '__main__':
    unittest.main(verbosity=2)