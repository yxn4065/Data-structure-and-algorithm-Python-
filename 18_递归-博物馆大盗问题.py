# -*- coding: utf-8 -*-
# @Author : yxn
# @Date : 2022/2/1 12:20 
# @IDE : PyCharm(2021.3.1) Python3.98

def fun1():
    """动态规划"""
    # 宝物的重量和价值
    tr = [None, {'w': 2, 'v': 3}, {'w': 3, 'v': 4},
          {'w': 4, 'v': 8}, {'w': 5, 'v': 8}, {'w': 9, 'v': 10}]
    # 大盗最大承重
    max_w = 20

    # 初始化一个二维表格m[(i,w)] 表示前i个宝物中,最大重量w的组合,
    # 所得到的最大价值 当i什么都不取或i上限为0时价值为0
    m = {(i, w): 0 for i in range(len(tr)) for w in range(max_w + 1)}

    # 逐个填写二维表格
    for i in range(1, len(tr)):
        for w in range(1, max_w + 1):
            if tr[i]['w'] > w:  # 装不下第i个宝物
                m[(i, w)] = m[(i - 1, w)]  # 不装第i个宝物
            else:
                # 装与不装第i个宝物情况下的最大值
                m[(i, w)] = max(m[(i - 1, w)],
                                m[(i - 1, w - tr[i]['w'])] + tr[i]['v'])

    print(m[(len(tr) - 1, max_w)])


def fun2():
    """递归"""
    # 宝物的重量和价值
    tr = {(2, 3), (3, 4), (4, 8), (5, 8), (9, 10)}
    # 大盗最大承重
    max_w = 20
    # 初始化记忆表格m,key是(宝物组合,最大重量),value是最大价值
    m = {}

    def thief(tr, w):
        if tr == set or w == 0:
            m[(tuple(tr), w)] = 0  # tuple是key的要求
            return 0
        elif (tuple(tr), w) in m:
            return m[(tuple(tr), w)]
        else:
            vmax = 0
            for t in tr:
                if t[0] <= w:
                    # 逐个从集合去掉某个宝物,递归调用,选出所有价值中的最大价值
                    v = thief(tr - {t}, w - t[0]) + t[1]
                    vamx = max(vmax, v)
            m[(tuple(tr), w)] = vamx
            return vmax

    print(thief(tr, max_w))


if __name__ == '__main__':
    fun1()
    fun2()
