# -*- coding: utf-8 -*-
# @Author : yxn
# @Date : 2022/1/25 21:07 
# @IDE : PyCharm(2021.3.1) Python3.98
from pythonds.basic.queue import Queue


def Joseph(namelist, num):
    simqueue = Queue()
    for name in namelist:
        simqueue.enqueue(name)

    while simqueue.size() > 1:
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())

        simqueue.dequeue()

    return simqueue.dequeue()


if __name__ == '__main__':
    print(Joseph(["小红", "小郎", "小黄", "小白", "小绿"], 6) + " 活了下来")
