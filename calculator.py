class CalculatorError(Exception):
    """计算器错误类"""
    pass

class Calculator:
    """简单计算器类，实现基本的四则运算"""
    
    @staticmethod
    def add(a: float, b: float) -> float:
        """加法运算"""
        return a + b
    
    @staticmethod
    def subtract(a: float, b: float) -> float:
        """减法运算"""
        return a - b
    
    @staticmethod
    def multiply(a: float, b: float) -> float:
        """乘法运算"""
        return a * b
    
    @staticmethod
    def divide(a: float, b: float) -> float:
        """除法运算"""
        if b == 0:
            raise CalculatorError("除数不能为零")
        return a / b
    
    def calculate(self, a: float, b: float, operator: str) -> float:
        """执行计算操作
        
        Args:
            a: 第一个操作数
            b: 第二个操作数
            operator: 运算符（+, -, *, /）
            
        Returns:
            计算结果
            
        Raises:
            CalculatorError: 当遇到无效的运算符或除零错误时
        """
        operations = {
            '+': self.add,
            '-': self.subtract,
            '*': self.multiply,
            '/': self.divide
        }
        
        if operator not in operations:
            raise CalculatorError(f"无效的运算符: {operator}")
        
        try:
            return operations[operator](a, b)
        except CalculatorError as e:
            raise e
        except Exception as e:
            raise CalculatorError(f"计算错误: {str(e)}")

def main():
    """主函数，用于测试计算器功能"""
    calc = Calculator()
    a, b = 10.5, 5.2
    operators = ['+', '-', '*', '/']
    
    print("计算器测试:")
    for op in operators:
        try:
            result = calc.calculate(a, b, op)
            print(f"{a} {op} {b} = {result}")
        except CalculatorError as e:
            print(f"错误: {str(e)}")

if __name__ == '__main__':
    main()