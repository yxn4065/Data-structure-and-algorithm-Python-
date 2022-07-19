# -*- coding: utf-8 -*-
# @Author : yxn
# @Date : 2022/1/27 20:46 
# @IDE : PyCharm(2021.3.1) Python3.98
def toStr(n, base):
    """递归实现"""
    converSting = "0123456789ABCDEF"
    if n < base:
        return converSting[n]
    else:
        return toStr(n // base, base) + converSting[n % base]


if __name__ == '__main__':
    print(toStr(100, 16))
    # 获取最大递归深度
    import sys

    print(sys.getrecursionlimit())  # 1000
