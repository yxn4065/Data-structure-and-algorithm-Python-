# -*- coding: utf-8 -*-
# @Author : yxn
# @Date : 2022/1/25 20:46 
# @IDE : PyCharm(2021.3.1) Python3.98
from pythonds.basic.stack import Stack


def postfixEval(x):
    s = Stack()
    tokenList = list(x)
    for token in tokenList:
        if token in "0123456789":
            s.push(int(token))
        else:
            o2 = s.pop()
            o1 = s.pop()
            result = doMath(token, o1, o2)
            s.push(result)
    return s.pop()


def doMath(op, op1, op2):
    if op == '*':
        return op1 * op2
    elif op == '/':
        return op1 / op2
    elif op == '+':
        return op1 + op2
    else:
        return op1 - op2


if __name__ == '__main__':
    print(postfixEval("123*+"))
