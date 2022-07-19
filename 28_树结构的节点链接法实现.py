# -*- coding: utf-8 -*-
# @Author : yxn
# @Date : 2022/7/16 23:40 
# @IDE : PyCharm(2022.1.3) Python3.9.12
class BinaryTree:
    """二叉树链表实现"""
    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newNode):
        if self.leftChild is None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self, newNode):
        if self.rightChild is None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self, obj):
        self.key = obj

    def getRootVal(self):
        """查看当前节点的值"""
        return self.key

    def preorder(self):
        """前序遍历"""
        print(self.key)
        if self.leftChild:
            self.leftChild.preorder()
        if self.rightChild:
            self.rightChild.preorder()


if __name__ == '__main__':
    r = BinaryTree('a')
    r.insertLeft('b')
    r.insertRight('c')
    r.getRightChild().setRootVal('hello')
    print(r.getRightChild().getRootVal())
    r.getLeftChild().insertRight('d')
    print(r.getLeftChild().getRightChild().getRootVal())
    print("=======")
    r.preorder()
