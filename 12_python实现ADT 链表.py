# -*- coding: utf-8 -*-
# @Author : yxn
# @Date : 2022/1/26 20:15 
# @IDE : PyCharm(2021.3.1) Python3.98
class Node:
    """链表实现:节点Node"""

    def __init__(self, initdate):
        self.data = initdate
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newData):
        self.data = newData

    def setNext(self, newNext):
        self.next = newNext


class UnorderedList:
    """链表实现:无序表"""

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return len(self.head)

    def add(self, item):
        temp = Node(item)  # 生成新节点
        temp.setNext(self.head)  # 指向head所指向的节点
        self.head = None  # head节点设为空

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.getNext()
        return count

    def search(self, item):
        current = self.head
        found = False
        while current is not None and found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        if previous is None:
            self.head = current.getNext()
        else:
            previous.getNext(current.getNext)


class OrderedList:
    """链表实现:有序表"""
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return len(self.head)

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.getNext()
        return count

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        if previous is None:
            self.head = current.getNext()
        else:
            previous.getNext(current.getNext)

    def search(self, item):
        current = self.head
        found = False
        stop = False
        while current != None and found and not stop:
            if current.getData() == item:
                found = True
            else:
                if current.getData() > item:
                    stop = True
                current = current.getNext()
        return found

    def add(self, item):
        current = self.head
        previous = None
        stop = False
        while current is not None and not stop:
            if current.getData() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()

        temp = Node(item)
        if previous is None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)


if __name__ == '__main__':
    temp = Node(93)
    print(temp.getData())
    m = UnorderedList()
    print(m.head)
