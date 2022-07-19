# -*- coding: utf-8 -*-
# @Author : yxn
# @Date : 2022/2/3 21:59 
# @IDE : PyCharm(2021.3.1) Python3.98
def bubbleSort(alist):
    for passnum in range(len(alist) - 1, 0, -1):
        for i in range(passnum):
            if alist[i] > alist[i + 1]:
                alist[i], alist[i + 1] = alist[i + 1], alist[i]

    return alist


def shortBubbleSort(alist):
    """冒泡排序性能改进"""
    exchange = True
    passnum = len(alist) - 1
    while passnum > 0 and exchange:
        exchange = False
        for i in range(passnum):
            if alist[i] > alist[i + 1]:
                exchange = True
                alist[i], alist[i + 1] = alist[i + 1], alist[i]
        passnum -= 1
    return alist


def selectSort(alist):
    """选择排序"""
    for fillslot in range(len(alist) - 1, 0, -1):
        positionOfMax = 0
        for location in range(1, fillslot + 1):
            if alist[location] > alist[positionOfMax]:
                positionOfMax = location

        temp = alist[fillslot]
        alist[fillslot] = alist[positionOfMax]
        alist[positionOfMax] = temp
    return alist


if __name__ == '__main__':
    testlist = [1, 100, 32, 8, 17, 19, 42, 13, 4]
    print(bubbleSort(testlist))
    print(shortBubbleSort(testlist))
    print(selectSort(testlist))
