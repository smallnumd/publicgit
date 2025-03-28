#include <stdio.h>
#include "calculator.h"

double add(double a, double b) {
    return a + b;
}

double subtract(double a, double b) {
    return a - b;
}

double multiply(double a, double b) {
    return a * b;
}

double divide(double a, double b) {
    return a / b;
}

CalculatorResult calculate(double a, double b, char operator) {
    CalculatorResult result = {0, NO_ERROR};
    
    switch(operator) {
        case '+':
            result.result = add(a, b);
            break;
        case '-':
            result.result = subtract(a, b);
            break;
        case '*':
            result.result = multiply(a, b);
            break;
        case '/':
            if (b == 0) {
                result.error = DIVISION_BY_ZERO;
                return result;
            }
            result.result = divide(a, b);
            break;
        default:
            result.error = INVALID_OPERATION;
            break;
    }
    
    return result;
}

// 主函数用于测试
int main() {
    double a = 10.5, b = 5.2;
    char operators[] = {'+', '-', '*', '/'};
    
    printf("计算器测试:\n");
    for (int i = 0; i < 4; i++) {
        CalculatorResult result = calculate(a, b, operators[i]);
        if (result.error == NO_ERROR) {
            printf("%.2f %c %.2f = %.2f\n", a, operators[i], b, result.result);
        } else if (result.error == DIVISION_BY_ZERO) {
            printf("错误：除数不能为零\n");
        } else {
            printf("错误：无效的运算符\n");
        }
    }
    
    return 0;
}