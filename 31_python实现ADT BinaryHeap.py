# -*- coding: utf-8 -*-
# @Author : yxn
# @Date : 2022/7/17 23:07 
# @IDE : PyCharm(2022.1.3) Python3.9.12
# 实现优先队列的经典方案是来用二义堆数据结构
# 符合“堆”性质的二叉树，其中任何一条路径，均是一个已排序数列，根节点的key最小.
# 任何一个节点x，其父节点p中的key均小于x中的key
class BinHeap:
    """
    完全二义树由于其特殊性，可以用非嵌套列表，以简单的方式实现，具有很好性质
    如果节点的下标为p，那么其左子节点下标为2p，右子节点为2p+1，其父节点下标为p//2
    """
    def __init__(self):
        """采用一个列表来保存堆数据，其中表首下标为的项无用，但为了后面代码可以用到简单的整数乘除法，仍保留它。"""
        self.heapList = [0]  # 表首下标为0无用
        self.currentSize = 0

    def insert(self, key):
        """将新key加入到堆中"""
        # 插入元素到末尾然后进行上浮操作
        self.heapList.append(key)
        self.currentSize += 1
        self.percUp(self.currentSize)

    def percUp(self, i):
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i // 2]:
                tmp = self.heapList[i // 2]
                self.heapList[i // 2] = self.heapList[i]  # 与父节点进行交换
                self.heapList[i] = tmp
            i = i // 2  # 上浮操作

    def delMin(self):
        """回堆中的最小项，同时将其从堆中删除"""
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize -= 1
        self.heapList.pop()
        self.percDown(1)  # 下沉
        return retval

    def percDown(self, i):
        # “下沉”路径的选择：如果比子节点大，那么选择较小的子节点交换下沉
        while i * 2 <= self.currentSize:
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                # 交换下沉
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp
            i = mc  # 沿路径向下

    def minChild(self, i):  # 获得较小子节点
        if i * 2 + 1 > self.currentSize:  # 唯一子节点
            return i * 2
        else:  # 返回较小的
            if self.heapList[i * 2 + 1] > self.heapList[i * 2]:
                return i * 2
            else:
                return i * 2 + 1

    def buildHeap(self, lst: list):
        """从一个无序key列表创建新堆"""
        # 用“下沉”法，能够将总代价控制在0（n）
        i = len(lst) // 2  # 从最后父节点开始下沉,因为叶节点不需要下沉
        self.currentSize = len(lst)
        self.heapList = [0] + lst[:]
        while i > 0:
            self.percDown(i)
            i -= 1

    def size(self):
        """返回堆中key的个数"""
        return self.currentSize

    # 进行堆排序
    def HeapSort(self, alist):
        """堆排序"""
        self.buildHeap(alist)  # 建立小堆顶
        res = []
        while self.currentSize > 0:
            self.heapList[1], self.heapList[-1] = self.heapList[-1], self.heapList[1]
            res.append(self.heapList.pop())
            self.currentSize -= 1
            self.percDown(1)
        return res


if __name__ == '__main__':
    bh = BinHeap()
    bh.insert(5)
    bh.insert(7)
    bh.insert(3)
    bh.insert(11)
    print(bh.delMin())
    # 利用二叉堆进行排序
    h = BinHeap()
    alist = [1, 3, 43, 24, 54, 2, 3, 6, 7]
    alist = h.HeapSort(alist)
    print(alist)
