# -*- coding: utf-8 -*-
# @Author : yxn
# @Date : 2022/7/17 23:39 
# @IDE : PyCharm(2022.1.3) Python3.9.13
# 二叉查找树BST:比父节点小的key都出现在左子树，比父节点大的key都出现在右子树。
# 二叉搜索树的实现：节点和链接结构

class BinarySearchTree:
    """ADT 二叉查找树"""
    def __init__(self):
        self.root = None  # BST的root成员引用根节点TreeNode
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):  # 可以使用len函数
        return self.size

    def __iter__(self):  # 可以进行迭代
        return self.root._iter_()

    def put(self, key, val):
        if self.root:
            self._put(key, val, self.root)  # 递归 使用辅助方法插入
        else:
            self.root = TreeNode(key, val)
        self.size = self.size + 1

    # 如果key>currentNode.key,则_put到右子树，否则,_put到左子树
    def _put(self, key, val, currentNode):
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                self._put(key, val, currentNode.leftChild)
            else:
                currentNode.leftChild = TreeNode(key, val, parent=currentNode)
        else:
            if currentNode.hasRightChild():
                self._put(key, val, currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(key, val, parent=currentNode)

    # 索引赋值的特殊方法
    def __setitem__(self, key, value):
        self.put(key, value)

    def get(self, key):
        if self.root:
            res = self._get(key, self.root)  # 递归函数 辅助方法
            if res:
                return res.payload
            else:
                return None
        return None

    # 使用递归进行查找
    def _get(self, key, currentNode):
        if not currentNode:
            return None
        elif currentNode.key == key:
            return currentNode
        elif currentNode.key > key:
            return self._get(key, currentNode.leftChild)
        else:
            return self._get(key, currentNode.rightChild)

    # 实现从索引找值得方法
    def __getitem__(self, key):
        return self.get(key)

    # 实现in方法
    def __contains__(self, item):
        if self._get(item, self.root):
            return True
        else:
            return False

    def delete(self, key):
        if self.size > 1:
            nodeToRemove = self._get(key, self.root)
            if nodeToRemove:
                self.remove(nodeToRemove)
                self.size = self.size - 1
            else:
                raise 'Error,key not in tree'
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size = self.size - 1
        else:
            raise 'Error,key not in tree'

    def remove(self, currentNode):
        # 第一种情况 没有子节点 直接删除
        if currentNode.isLeaf():
            if currentNode == currentNode.parent.leftChild:
                currentNode.parent.leftChild = None
            else:
                currentNode.parent.rightChild = None
        # 有两个子节点
        elif currentNode.hasBothChildren():
            succ = currentNode.findSuccessor()  # 找到后继节点
            succ.spliceOut()  # 摘除后继节点
            currentNode.key = succ.key
            currentNode.payload = succ.payload
        # 节点有一个子节点
        else:
            if currentNode.hasLeftChild():
                # 左左组合
                if currentNode.isLeftChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.leftChild
                # 右左组合
                elif currentNode.isRightChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.leftChild
                # 根左组合
                else:
                    currentNode.replaceNodeData(currentNode.leftChild.key, currentNode.leftChild.payload,
                                                currentNode.leftChild.leftChild, currentNode.leftChild.rightChild)
            else:
                # 左右组合
                if currentNode.isLeftChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.rightChild
                # 右右组合
                elif currentNode.isRightChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.rightChild
                # 根右组合
                else:
                    currentNode.replaceNodeData(currentNode.rightChild.key, currentNode.rightChild.payload,
                                                currentNode.rightChild.leftChild, currentNode.rightChild.rightChild)

    # 实现del方法
    def __delitem__(self, key):
        self.delete(key)


class TreeNode:

    def __init__(self, key, val, left=None, right=None, parent=None):
        self.key = key
        self.val = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.rightChild or self.leftChild)

    def hasAnyChildren(self):
        return self.rightChild or self.leftChild

    def hasBothChildren(self):
        return self.leftChild and self.rightChild

    def replaceNodeData(self, key, val, lc, rc):
        self.key = key
        self.val = val
        self.rightChild = rc
        self.leftChild = lc
        # 更换子节点的父节点标签
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self

    # 中序遍历的方式进行迭代
    def __iter__(self):
        if self:
            if self.hasLeftChild():
                for elem in self.leftChild:
                    yield elem
            yield self.key
            if self.hasRightChild():
                for elem in self.rightChild:
                    yield elem

    # 找到后继节点函数
    def findSuccessor(self):
        succ = None
        if self.hasRightChild():
            succ = self.rightChild.findMin()
        # 目前不会遇到 因为这段代码是在当不存在右子节点时 但我们假设存在两个节点
        else:
            if self.parent:
                if self.isLeftChild():
                    succ = self.parent
                else:
                    self.parent.rightChild = None
                    succ = self.parent.findSuccessor()
                    self.parent.rightChild = self
        return succ

    def findMin(self):
        cur = self
        while cur.hasLeftChild():
            cur = cur.leftChild
        return cur

    # 摘除后继节点
    def spliceOut(self):
        # 是叶节点 直接摘除
        if self.isLeaf():
            if self.isLeftChild():
                self.parent.leftChild = None
            else:
                self.parent.rightChild = None
        # 有子节点 只会存在右子节点
        elif self.hasAnyChildren():
            # 不会遇到这种情况
            if self.hasLeftChild():
                if self.isLeftChild():
                    self.parent.leftChild = self.leftChild
                else:
                    self.parent.rightChild = self.leftChild
                self.leftChild.parent = self.parent
            # 摘除带右子节点的节点
            else:
                if self.isLeftChild():
                    self.parent.leftChild = self.rightChild
                else:
                    self.parent.rightChild = self.rightChild
                self.rightChild.parent = self.parent


if __name__ == '__main__':
    pass
