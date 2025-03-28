#ifndef CALCULATOR_H
#define CALCULATOR_H

// 基本运算函数声明
double add(double a, double b);
double subtract(double a, double b);
double multiply(double a, double b);
double divide(double a, double b);

// 错误处理
typedef enum {
    NO_ERROR,
    DIVISION_BY_ZERO,
    INVALID_OPERATION
} CalculatorError;

// 计算结果结构体
typedef struct {
    double result;
    CalculatorError error;
} CalculatorResult;

// 带错误处理的计算函数
CalculatorResult calculate(double a, double b, char operator);

#endif // CALCULATOR_H