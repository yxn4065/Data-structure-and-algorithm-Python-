# -*- coding: utf-8 -*-
# @Author : yxn
# @Date : 2022/7/17 22:27 
# @IDE : PyCharm(2022.1.3) Python3.9.12
"""三种遍历方法
前序遍历：根->左->右
中序遍历：左->根->右
后序遍历：左->右->根"""


def preorder(tree):
    if tree:
        print(tree.getRootVal())
        preorder(tree.getLeftChild())
        preorder(tree.getRightChild())


def postorder(tree):
    if tree:
        preorder(tree.getLeftChild())
        preorder(tree.getRightChild())
        print(tree.getRootVal())


def inorder(tree):
    if tree:
        preorder(tree.getLeftChild())
        print(tree.getRootVal())
        preorder(tree.getRightChild())
