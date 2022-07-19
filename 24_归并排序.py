# -*- coding: utf-8 -*-
# @Author : yxn
# @Date : 2022/2/3 22:35 
# @IDE : PyCharm(2021.3.1) Python3.98
def merge_sort(lst):
    # 递归结束条件
    if len(lst) <= 1:
        return lst

    # 分解问题,递归调用
    middle = len(lst) // 2
    left = merge_sort(lst[:middle])
    right = merge_sort(lst[middle:])

    # 合并左右半部,完成排序
    meged = []
    while left and right:
        if left[0] <= right[0]:
            meged.append(left.pop(0))
        else:
            meged.append(right.pop(0))
    meged.extend(right if right else left)
    return meged


if __name__ == '__main__':
    testlist = [1, 100, 32, 8, 17, 19, 42, 13, 4]
    print(merge_sort(testlist))
