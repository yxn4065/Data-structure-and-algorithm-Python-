# -*- coding: utf-8 -*-
# @Author : yxn
# @Date : 2022/1/24 14:33 
# @IDE : PyCharm(2021.3.1) Python3.98
"""python官方算法复杂度网站
https://wiki.python.org/moin/TimeComplexity/
"""
import timeit
from timeit import Timer
import random


# 生成列表的4种方式
def test1():
    l = []
    for i in range(1000):
        l += [i]


def test2():
    l = []
    for i in range(1000):
        l.append(i)


def test3():
    l = [i for i in range(1000)]


def test4():
    l = list(range(1000))


if __name__ == '__main__':
    # Timer("反复运行的语句", "只运行一次的'安装语句'")
    t1 = Timer("test1()", "from __main__ import test1")
    print("循环连接方式: concat %fs" % t1.timeit(number=1000))
    t2 = Timer("test2()", "from __main__ import test2")
    print("append添加元素方式: concat %fs" % t2.timeit(number=1000))
    t3 = Timer("test3()", "from __main__ import test3")
    print("列表推导式: concat %fs" % t3.timeit(number=1000))
    t4 = Timer("test4()", "from __main__ import test4")
    print("range转列表方式: concat %fs" % t4.timeit(number=1000))
    print("=====*list.pop 计时测试*==========")
    x = list(range(200000))
    popzero = timeit.Timer("x.pop(0)", "from __main__ import x")
    popend = timeit.Timer("x.pop()", "from __main__ import x")
    print("x.pop(0): %fs " % popzero.timeit(number=1000))
    print("x.pop( ): %fs " % popend.timeit(number=1000))
    print("===增长趋势===")
    print("pop(0)        pop()")
    for i in range(100000, 1000001, 100000):
        x = list(range(i))
        pz = popzero.timeit(number=1000)
        pt = popend.timeit(number=1000)
        print("%.5f, %10.5f" % (pz, pt))

    print("\n*********字典和列表************")
    for i in range(10000, 100001, 10000):
        t = timeit.Timer("random.randrange(%d) in x" % i,
                         "from __main__ import random, x")
        x = list(range(i))
        lst_time = t.timeit(number=1000)
        x = {j: None for j in range(i)}
        d_time = t.timeit(number=1000)
        print("%d,%10.3f,%10.3f" % (i, lst_time, d_time))

"""结论        
pop()的时间复杂度为O(1),而pop(n)的时间复杂度为O(n)
字典的执行时间与规模无关,是常数,列表执行时间随规模增大而线性上升
"""
