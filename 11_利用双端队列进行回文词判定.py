# -*- coding: utf-8 -*-
# @Author : yxn
# @Date : 2022/1/26 19:54 
# @IDE : PyCharm(2021.3.1) Python3.98
class Deque:
    """采用List实现,0为尾端,-1为首端"""
    
    def __init__(self):
        self.item = []

    def isEmpty(self):
        return self.item == []

    def addFront(self, item):
        self.item.append(item)

    def addRear(self, item):
        self.item.insert(0, item)

    def removeFront(self):
        return self.item.pop()

    def removeRear(self):
        return self.item.pop(0)

    def size(self):
        return len(self.item)


def palchecker(s):
    chardeque = Deque()
    for ch in s:
        chardeque.addRear(ch)

    stillEqual = True
    while chardeque.size() > 1 and stillEqual:
        first = chardeque.removeFront()
        last = chardeque.removeRear()
        if first != last:
            stillEqual = False

    return stillEqual


if __name__ == '__main__':
    print(palchecker("上海自来水来自海上"))
    print(palchecker("山东落花生花落东山"))
    print(palchecker("北京输油管油输京北"))
