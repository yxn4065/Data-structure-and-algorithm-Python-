# -*- coding: utf-8 -*-
# @Author : yxn
# @Date : 2022/7/17 16:46 
# @IDE : PyCharm(2022.1.3) Python3.9.12
import operator

from pythonds import BinaryTree, Stack


def buildParseTree(fpexp):
    fplist = []
    for i in fpexp:
        fplist.append(i)  # 分割为列表
    pStack = Stack()  # 新建栈用于保存父节点
    eTree = BinaryTree('')  # 创建树
    pStack.push(eTree)  # 当前节点入栈
    currentTree = eTree  # 设置当前节点
    for i in fplist:
        if i == "(":  # 当i为"("时 表达式开始 创建左子节点 当前节点下降 将老的当前节点（父节点）入栈
            currentTree.insertLeft('')
            pStack.push(currentTree)
            currentTree = currentTree.getLeftChild()
        elif i not in ["+", "-", "*", "/"] and i != ")":  # 当i为操作数时 节点值设置为操作数 上升
            currentTree.setRootVal(int(i))
            parent = pStack.pop()
            currentTree = parent
        elif i in ["+", "-", "*", "/"]:  # 当i为操作符 当前节点值设置为操作符 下降到右子节点 并保存父节点入栈
            currentTree.setRootVal(i)
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree = currentTree.getRightChild()
        elif i == ")":  # 当i为")" 表达式结束 出栈上升到父节点
            currentTree = pStack.pop()
        else:  # 防止出错
            raise ValueError
    return eTree


def evaluate(parseTree):
    opers = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}  # TODO 存在问题
    leftC = parseTree.getLeftChild()
    rightC = parseTree.getRightChild()

    if leftC and rightC:
        fn = opers[parseTree.getRootVal()]
        return fn(evaluate(leftC), evaluate(rightC))
    else:
        return parseTree.getRootVal()


def postorderevel(tree):
    """后续遍历法重写表达式求值"""
    opers = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
    res1 = None
    res2 = None
    if tree:
        res1 = postorderevel(tree.getLeftChild())
        res2 = postorderevel(tree.getRightChild())
        if res1 and res2:
            return opers[tree.getRootVal()](res1, res2)
        else:
            return tree.getRootVal()


def printexp(tree):
    """全括号中缀表达式的生成(中序遍历)"""
    # todo 存在问题:每个数字都加了括号
    sVal = ""
    if tree:
        sVal = '(' + printexp(tree.getLeftChild())
        sVal = sVal + str(tree.getRootVal())
        sVal = sVal + printexp(tree.getRightChild() + ')')
    return sVal


if __name__ == '__main__':
    fpexp = "(3*(4+5))"
    parseTree = buildParseTree(fpexp)
    print(evaluate(parseTree))
