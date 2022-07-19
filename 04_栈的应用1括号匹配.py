# -*- coding: utf-8 -*-
# @Author : yxn
# @Date : 2022/1/25 11:26 
# @IDE : PyCharm(2021.3.1) Python3.98

from pythonds.basic.stack import Stack


def matches(open, close):
    opens = "([{"
    closer = ")]}"
    return opens.index(open) == closer.index(close)


def parCheck(brackets):
    s = Stack()  # 1.生成一个空栈
    balanced = True
    index = 0
    while index < len(brackets) and balanced:
        symbol = brackets[index]  # 2.从左往右依次取括号
        if symbol in "([{":  # 左括号->压栈
            s.push(symbol)
        else:  # 右括号->
            if s.isEmpty():  # 栈空,匹配失败
                balanced = False
            else:  # 不空,从栈顶移除
                top = s.pop()
                if not matches(top, symbol):  # 与栈顶元素对比,是否匹配
                    balanced = False
        index += 1  # 3.继续2

    if balanced and s.isEmpty():
        return True
    else:
        return False


if __name__ == '__main__':
    print(parCheck("([{}])"))
    print(parCheck("([()]){}"))
    print(parCheck("()(]}{[])"))
