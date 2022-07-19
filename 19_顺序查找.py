# -*- coding: utf-8 -*-
# @Author : yxn
# @Date : 2022/2/3 21:32 
# @IDE : PyCharm(2021.3.1) Python3.98
def sequentialSearch(alist, item):
    """无序表的顺序查找"""
    pos = 0
    found = False

    while pos < len(alist) and not found:
        if alist[pos] == item:
            found = True
        else:
            pos += 1
    return found


def orderedSequentialSearch(alist, item):
    """有序表的顺序查找"""
    pos = 0
    found = False
    stop = False
    while stop < len(alist) and not found and not stop:
        if alist[pos] == item:
            found = True
        else:
            if alist[pos] > item:
                stop = True
            pos += 1
    return found


if __name__ == '__main__':
    testlist1 = [1, 2, 32, 8, 17, 19, 42, 13, 0]
    testlist2 = [1, 6, 8, 11, 26, 58, 69, 77, 100]
    print(sequentialSearch(testlist1, 13))
    print(sequentialSearch(testlist2, 13))
