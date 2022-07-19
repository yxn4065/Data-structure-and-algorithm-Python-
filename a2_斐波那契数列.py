# -*- coding: utf-8 -*-
# @Author : yxn
# @Date : 2022/3/5 21:17 
# @IDE : PyCharm(2021.3.1) Python3.9.10
def fib1(n):
    if n < 1:
        print('input error')
        return -1
    if n == 1 or n == 2:
        return 1
    else:
        return fib1(n - 1) + fib1(n - 2)


def fib2(n):
    n1 = 1
    n2 = 1
    n3 = 1
    if n < 1:
        print('input error')
        return -1
    while (n - 2) > 0:
        n3 = n2 + n1
        n1 = n2
        n2 = n3
        n -= 1
    return n3


if __name__ == '__main__':
    pass
