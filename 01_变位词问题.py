# -*- coding: utf-8 -*-
# @Author : yxn
# @Date : 2022/1/23 20:20 
# @IDE : PyCharm(2021.3.1) Python3.98
"""类似于python和typhon即为变位词"""


# 解法一:逐字检查法
def fun1(s1, s2):
    alist = list(s2)  # 复制s2
    p1 = 0
    stillOk = True
    while p1 < len(s1) and stillOk:  # 循环s1的每个字符
        p2 = 0
        found = False
        while p2 < len(alist) and not found:  # 在s2中逐个进行对比
            if s1[p1] == alist[p2]:
                found = True
            else:
                p2 += 1
        if found:  # 找到,标记
            alist[p2] = None
        else:
            stillOk = False  # 未找到,失败
        p1 += 1
    return stillOk


# 解法二:排序比较
def fun2(s1, s2):
    al1 = list(s1)
    al2 = list(s2)
    al1.sort()
    al2.sort()
    p = 0
    matches = True
    while p < len(al1) and matches:
        if al1[p] == al2[p]:
            p += 1
        else:
            matches = False
    return matches


# 利用递归方式实现列表的全排列
def permutation(li):
    len_list = len(li)
    if len_list == 1:
        return li

    result = []
    for i in range(len_list):
        res_list = li[:i] + li[i + 1:]
        s = li[i]
        per_result = permutation(res_list)
        if len(per_result) == 1:
            result.append(li[i:i + 1] + per_result)
        else:
            result += [[s] + j for j in per_result]
    return result


# 解法三:暴力穷举比较法(计算量极大)
def fun3(s1, s2):
    # import itertools
    # alist = list(itertools.permutations(list(s2)))  # 对s2进行全排列
    alist = permutation(list(s2))
    for i in alist:
        if list(s1) == i:
            return True


# 解法四:计数比较法
def fun4(s1, s2):
    c1 = [0] * 26  # 创建26个全为0的数组
    c2 = [0] * 26
    for i in range(len(s1)):
        pos = ord(s1[i]) - ord('a')
        c1[pos] += 1
    for i in range(len(s2)):
        pos = ord(s2[i]) - ord('a')
        c2[pos] += 1  # 将对于数组位置的0改为1
    j = 0
    stillOk = True
    while j < 26 and stillOk:
        if c1[j] == c2[j]:
            j += 1
        else:
            stillOk = False
    return stillOk


if __name__ == '__main__':
    str1 = "python"
    str2 = "typhon"
    print(fun1(str1, str2))
    print(fun2(str1, str2))
    print(fun3(str1, str2))
    print(fun4(str1, str2))
