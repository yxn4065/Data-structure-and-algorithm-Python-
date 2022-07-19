# -*- coding: utf-8 -*-
# @Author : yxn
# @Date : 2022/4/27 22:33 
# @IDE : PyCharm(2022.1) Python3.9.12
from pprint import pprint

a = "cbacbaa"
b = "abcdbb"  # 最长公共子序列为acb


def lengthOfLCS(A, B):
    m = len(A)
    n = len(B)
    LCS = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    memo = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    pprint(memo)
    for i in range(m):
        for j in range(n):
            if A[i] == B[j]:
                LCS[i + 1][j + 1] = LCS[i][j] + 1
                memo[i + 1][j + 1] = '↖'
            else:
                LCS[i + 1][j + 1] = max(LCS[i][j + 1], LCS[i + 1][j])
    pprint(LCS)
    return LCS[-1][-1]


if __name__ == '__main__':
    # 字符串1
    s1 = "BDCABA"
    # 字符串2
    s2 = "ABCBDAB"
    # 计算最长公共子序列的长度
    res = lengthOfLCS(s1, s2)
    # 打印结果
    print(f"所求最长公共子序列为: {res}")  # 4
