# -*- coding: utf-8 -*-
# @Author : yxn
# @Date : 2022/2/3 22:25 
# @IDE : PyCharm(2021.3.1) Python3.98
def shellSortshel(alist):
    sublistcount = len(alist) // 2  # 间隔设定
    while sublistcount > 0:
        for startposition in range(sublistcount):  # 子列表排序
            gapInsertionSort(alist, startposition, sublistcount)

        print("After increments of size", sublistcount, "The list is", alist)
        sublistcount = sublistcount // 2  # 间隔缩小


def gapInsertionSort(alist, start, gap):
    for i in range(start + gap, len(alist), gap):
        currentvalue = alist[i]
        position = i

        while position >= gap and alist[position - gap] > currentvalue:
            alist[position] = alist[position - gap]
            position -= gap

        alist[position] = currentvalue


if __name__ == '__main__':
    testlist = [1, 100, 32, 8, 17, 19, 42, 13, 4]
    print(shellSortshel(testlist))
