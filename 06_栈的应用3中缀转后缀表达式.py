# -*- coding: utf-8 -*-
# @Author : yxn
# @Date : 2022/1/25 16:56 
# @IDE : PyCharm(2021.3.1) Python3.98
from pythonds.basic.stack import Stack


def infixToPostfix(infixexpr):
    prec = {"*": 3, "/": 3, "+": 2, "-": 2, "(": 1}  # 字典记录操作符的优先级
    opStack = Stack()
    postfixList = []
    tokenList = list(infixexpr)  # 解析表达式
    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0213456789":
            postfixList.append(token)  # 添加到列表中
        elif token == "(":
            opStack.push(token)  # 压栈
        elif token == ")":
            topToken = opStack.pop()
            while topToken != "(":
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:  # 栈非空以及当前运算符优先级较栈中优先级低
            while (not opStack.isEmpty()) and \
                    (prec[opStack.peek()] >= prec[token]):
                postfixList.append(opStack.pop())  # 先将当前栈中运算符出栈并添加到列表中
            opStack.push(token)  # 否则直接入栈

    # for i in range(opStack.size()):  # 栈的遍历
    #     print(opStack.pop())

    while not opStack.isEmpty():
        postfixList.append(opStack.pop())

    return " ".join(postfixList)


if __name__ == '__main__':
    print(infixToPostfix("A+B*C"))
    print(infixToPostfix("A+B*C/5-(4-5)*3"))
