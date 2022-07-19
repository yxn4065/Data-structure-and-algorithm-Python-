# -*- coding: utf-8 -*-
# @Author : yxn
# @Date : 2022/1/25 11:11 
# @IDE : PyCharm(2021.3.1) Python3.98
"""pythonds模块实现了python的数据结构类型"""


class Stack:
    """栈:后进先出"""
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):  # 返回最后一个元素
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


if __name__ == '__main__':
    s = Stack()
    s.push(4)
    s.push("dog")
    print(s.peek())
    print(s.pop())
    print(s.size())
