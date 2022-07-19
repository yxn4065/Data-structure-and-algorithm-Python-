# -*- coding: utf-8 -*-
# @Author : yxn
# @Date : 2022/1/25 20:58 
# @IDE : PyCharm(2021.3.1) Python3.98

class Queue:
    """队列:先进先出"""
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):  # 入队操作,O(n)
        self.items.insert(0, item)

    def dequeue(self):  # 出队操作,O(1)
        return self.items.pop()

    def size(self):
        return len(self.items)


if __name__ == '__main__':
    q = Queue()
    q.enqueue(4)
    q.enqueue("hhhh")
    print(q.size())
