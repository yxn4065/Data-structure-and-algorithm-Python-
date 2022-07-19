# -*- coding: utf-8 -*-
# @Author : yxn
# @Date : 2022/4/28 23:08 
# @IDE : PyCharm(2022.1) Python3.9.12

def lcs(a: str, b: str) -> tuple[list[list[int]], list[list[int]]]:
    """
    :param a: 子序列1
    :param b: 子序列2
    :return: 优化函数res->C,标记函数flag->B
    """
    lena = len(a)
    lenb = len(b)
    res = [[0 for _ in range(lenb + 1)] for _ in range(lena + 1)]
    flag = [[0 for _ in range(lenb + 1)] for _ in range(lena + 1)]
    for i in range(lena):
        for j in range(lenb):
            if a[i] == b[j]:
                res[i + 1][j + 1] = res[i][j] + 1
                flag[i + 1][j + 1] = '↖'
            elif res[i + 1][j] > res[i][j + 1]:
                res[i + 1][j + 1] = res[i + 1][j]
                flag[i + 1][j + 1] = '←'
            else:
                res[i + 1][j + 1] = res[i][j + 1]
                flag[i + 1][j + 1] = '↑'
    return res, flag


def printLcs(flag, a, i, j):
    """自定义打印输出函数
    :param flag: 标记函数
    :param a: 序列X
    :param i: 序列X的长度(下标为0到i)
    :param j: 序列j的长度(下标为0到j)
    :return: None
    """
    if i == 0 or j == 0:
        return  # 此时序列为空
    if flag[i][j] == '↖':  # 遇到↖进行输出
        printLcs(flag, a, i - 1, j - 1)
        print(a[i - 1], end='')
    elif flag[i][j] == '←':  # 向左移动
        printLcs(flag, a, i, j - 1)
    else:  # ↑向上移动
        printLcs(flag, a, i - 1, j)
    print('', end=" ")


if __name__ == '__main__':
    X = 'ABCBDAB'
    Y = 'BDCABA'
    # 得到优化函数C,标记函数B
    C, B = lcs(X, Y)
    for i in C:
        print(i)
    print('')
    for j in B:
        print(j)
    print("\n所求最长公共子序列为: ", end="")
    printLcs(B, X, len(X), len(Y))
