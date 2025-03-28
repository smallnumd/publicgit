#include <stdio.h>
#include <assert.h>
#include "calculator.h"

void test_add() {
    printf("测试加法运算...\n");
    assert(add(2, 3) == 5);
    assert(add(-1, 1) == 0);
    assert(add(0, 0) == 0);
    printf("加法测试通过！\n");
}

void test_subtract() {
    printf("测试减法运算...\n");
    assert(subtract(5, 3) == 2);
    assert(subtract(1, 1) == 0);
    assert(subtract(0, 5) == -5);
    printf("减法测试通过！\n");
}

void test_multiply() {
    printf("测试乘法运算...\n");
    assert(multiply(2, 3) == 6);
    assert(multiply(-2, 3) == -6);
    assert(multiply(0, 5) == 0);
    printf("乘法测试通过！\n");
}

void test_divide() {
    printf("测试除法运算...\n");
    assert(divide(6, 2) == 3);
    assert(divide(5, 2) == 2.5);
    assert(divide(0, 5) == 0);
    printf("除法测试通过！\n");
}

void test_calculate() {
    printf("测试计算器功能...\n");
    
    CalculatorResult result;
    
    // 测试正常运算
    result = calculate(10, 5, '+');
    assert(result.error == NO_ERROR && result.result == 15);
    
    result = calculate(10, 5, '-');
    assert(result.error == NO_ERROR && result.result == 5);
    
    result = calculate(10, 5, '*');
    assert(result.error == NO_ERROR && result.result == 50);
    
    result = calculate(10, 5, '/');
    assert(result.error == NO_ERROR && result.result == 2);
    
    // 测试除零错误
    result = calculate(10, 0, '/');
    assert(result.error == DIVISION_BY_ZERO);
    
    // 测试无效运算符
    result = calculate(10, 5, '%');
    assert(result.error == INVALID_OPERATION);
    
    printf("计算器功能测试通过！\n");
}

int main() {
    printf("开始运行计算器单元测试...\n\n");
    
    test_add();
    test_subtract();
    test_multiply();
    test_divide();
    test_calculate();
    
    printf("\n所有测试通过！\n");
    return 0;
}