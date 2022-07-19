# -*- coding: utf-8 -*-
# @Author : yxn
# @Date : 2022/7/18 16:21 
# @IDE : PyCharm(2022.1.3) Python3.9.13
from pythonds.trees.bst import TreeNode


class AVLTree:
    """二叉平衡树mooc"""
    def __init__(self):
        self.root = None  # BST的root成员引用根节点TreeNode
        self.size = 0

    def _put(self, key, val, currentNode):
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                self._put(key, val, currentNode.leftChild)
            else:
                currentNode.leftChild = TreeNode(key, val, parent=currentNode)
                self.updateBalance(currentNode.leftChild)
        else:
            if currentNode.hasRightChild():
                self._put(key, val, currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(key, val, parent=currentNode)
                self.updateBalance(currentNode.rightChild)

    def updateBalance(self, node):
        if node.balanceFactor > 1 or node.balanceFactor < -1:
            self.rebalance(node)
            return
        if node.parent is not None:
            if node.isLeftChild():
                node.parent.balanceFactor += 1
            elif node.isRightChild():
                node.parent.balanceFactor -= 1

            if node.parent.balanceFactor != 0:
                self.updateBalance(node.parent)

    def rotateLeft(self, rotRoot):
        newRoot = rotRoot.rightChild
        rotRoot.rightChild = newRoot.leftChild
        if newRoot.leftChild is not None:
            newRoot.leftChild.parent = rotRoot
        newRoot.parent = rotRoot.parent
        if rotRoot.isRoot():
            self.root = newRoot
        else:
            if rotRoot.isLeftChild():
                rotRoot.parent.leftChild = newRoot
            else:
                rotRoot.parent.rightChild = newRoot
        newRoot.leftChild = rotRoot
        rotRoot.parent = newRoot
        rotRoot.balanceFactor = rotRoot.balanceFactor + 1 - min(newRoot.balanceFactor, 0)
        newRoot.balanceFactor = newRoot.balanceFactor + 1 + max(rotRoot.balanceFactor, 0)

    def rotateRight(self, node):
        pass

    def rebalance(self, node):
        if node.balanceFactor < 0:
            if node.rightChild.balanceFactor > 0:
                # Do an LR Rotation
                self.rotateRight(node.rightChild)
                self.rotateLeft(node)
            else:
                # single left
                self.rotateLeft(node)
        elif node.balanceFactor > 0:
            if node.leftChild.balanceFactor < 0:
                # Do an RL Rotation
                self.rotateLeft(node.leftChild)
                self.rotateRight(node)
            else:
                # single right
                self.rotateRight(node)


class tree:
    """平衡二叉树(知乎 https://zhuanlan.zhihu.com/p/349702795)"""
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class Tree:
    """平衡二叉树(知乎 https://zhuanlan.zhihu.com/p/349702795)"""
    def __init__(self):
        self.head = None

    def print1(self):  # 层次输出二叉树的值
        a = []
        if self.head is None:
            print("元素为空")
        else:
            a.append(self.head)
            while len(a) != 0:
                temp = a[0]
                print(temp.data)
                if temp.left is not None:
                    a.append(temp.left)
                if temp.right is not None:
                    a.append(temp.right)
                a.pop(0)

    def deep(self, head):  # 递归求某一个节点的深度
        if head is None:
            return 0
        else:
            return self.max1(self.deep(head.left), self.deep(head.right)) + 1

    def max1(self, a, b):
        if a < b:
            return b
        else:
            return a

    def LL(self, a):
        temp = a.left.right
        temp1 = a.left
        temp1.right = a
        a.left = temp
        return temp1

    def RR(self, a):
        temp = a.right.left
        temp1 = a.right
        temp1.left = a
        a.right = temp
        return temp1

    def LR(self, a):
        a.left = self.RR(a.left)
        return self.LL(a)

    def RL(self, a):
        a.right = self.LL(a.right)
        return self.RR(a)

    def insert1(self, a, data):  # avl树的插入过程
        if a is None:
            a = tree(data)
            return a
        else:
            if data < a.data:
                a.left = self.insert1(a.left, data)
            else:
                a.right = self.insert1(a.right, data)
            if self.deep(a.left) - self.deep(a.right) > 1:
                if data < a.left.data:  # LL型,即插入的数字在a节点的左边的左边
                    a = self.LL(a)
                else:  # LR型,即插入的数字在a节点的左边的右边
                    a = self.LR(a)
            elif self.deep(a.right) - self.deep(a.left) > 1:
                if data > a.right.data:  # RR型,即插入的数字在a节点的右边的右边
                    a = self.RR(a)
                else:  # RL型,即插入的数字在a节点的右边的左边
                    a = self.RL(a)
        return a


if __name__ == '__main__':
    tr = Tree()
    a = [1, 3, 5, 4, 4.5]
    for i in a:
        tr.head = tr.insert1(tr.head, i)
    tr.print1()
