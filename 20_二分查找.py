# -*- coding: utf-8 -*-
# @Author : yxn
# @Date : 2022/2/3 21:42 
# @IDE : PyCharm(2021.3.1) Python3.98
def binarySearch(alist, item):
    found = False
    first = 0
    last = len(alist) - 1
    while first <= last and not found:
        midpoint = (first + last) // 2
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1

    return found


def binarySearch1(alist, item):
    """递归版本二分查找"""
    if len(alist) == 0:
        return False
    midpoint = len(alist) // 2
    if alist[midpoint] == item:
        return True
    else:
        if item < alist[midpoint]:
            return binarySearch1(alist[:midpoint], item)
        else:
            return binarySearch1(alist[midpoint + 1:], item)


if __name__ == '__main__':
    testlist1 = [1, 2, 32, 8, 17, 19, 42, 13, 0]
    testlist2 = [1, 6, 8, 11, 26, 58, 69, 77, 100]
    print(binarySearch(testlist1, 42))
    print(binarySearch(testlist2, 66))
    print(binarySearch1(testlist2, 69))
