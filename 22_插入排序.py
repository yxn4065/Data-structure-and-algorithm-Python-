# -*- coding: utf-8 -*-
# @Author : yxn
# @Date : 2022/2/3 22:12 
# @IDE : PyCharm(2021.3.1) Python3.98
def insertSort(alist):
    for index in range(1, len(alist)):
        currentvalue = alist[index]
        position = index
        while position > 0 and alist[position - 1] > currentvalue:
            alist[position] = alist[position - 1]
            position -= 1

        alist[position] = currentvalue

    return alist


if __name__ == '__main__':
    testlist = [1, 100, 32, 8, 17, 19, 42, 13, 4]
    print(insertSort(testlist))
