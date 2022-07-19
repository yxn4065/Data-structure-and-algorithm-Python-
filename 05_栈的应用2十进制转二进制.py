# -*- coding: utf-8 -*-
# @Author : yxn
# @Date : 2022/1/25 15:38 
# @IDE : PyCharm(2021.3.1) Python3.98
from pythonds.basic.stack import Stack


def divideBy2(number):
    """10进制转二进制"""
    s = Stack()
    while number > 0:
        rem = number % 2  # 求余数
        s.push(rem)
        number = number // 2  # 整数除
    binString = ""
    while not s.isEmpty():
        binString += str(s.pop())
    return binString


def baseConverter(decNumber, base):
    """十进制转十六以下任意进制"""
    digits = "0123456789ABCDEF"
    remstack = Stack()

    while decNumber > 0:
        rem = decNumber % base
        remstack.push(rem)
        decNumber = decNumber // base

    newString = ""
    while not remstack.isEmpty():
        newString += digits[remstack.pop()]

    return newString


if __name__ == '__main__':
    print(divideBy2(25))
    print(baseConverter(25, 2))
    print(baseConverter(25, 8))
    print(baseConverter(25, 16))
