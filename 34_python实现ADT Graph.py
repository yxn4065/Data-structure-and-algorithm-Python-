# -*- coding: utf-8 -*-
# @Author : yxn
# @Date : 2022/7/18 21:16 
# @IDE : PyCharm(2022.1.3) Python3.9.13
"""
painting:用笔刷画的油画
drawing:用硬笔画的素描或线条画
picture:真实形象反应的画,如照片等
image:由印象而来的画,如遥感影像
figure:轮廓图的意思,某个侧面的轮廓
diagram:抽象的概念关系图,如电路图,海洋环流图,类层次图等
chart:由数字统计来的柱状图,折线图等
map:地图 plot:地图上的一小块
graph:重在由一些基本元素构造而来的图,如点或者线段等
顶点Vertex(也称节点Node)
边Edge(也称弧Arc)
有向无环图DAG:directed acyclic graph
"""


class Vertex:
    """顶点类"""
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}

    def addNeighbor(self, nbr, weight=0):
        """
        :param nbr: 顶点对象的值
        """
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + "connected to:" + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self, nbr):
        return self.connectedTo[nbr]


class Graph:
    """保存所有顶点"""
    def __init__(self):
        self.vertList = {}  # 定义顶点的列表
        self.numVertices = 0  # 顶点数量

    def addVertex(self, key):  # 新加顶点
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self, n):  # 通过key查找顶点
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self, n):  # 定义in操作
        return n in self.vertList

    def addEdge(self, f, t, cost=0):
        # 不存在的顶点先添加
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        # 调用起始顶点方法添加邻接边
        self.vertList[f].addNeighbor(self.vertList[t], cost)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):  # 定义迭代函数方法
        return iter(self.vertList.values())


if __name__ == '__main__':
    g = Graph()
    for i in range(6):
        g.addVertex(i)

    print(g.vertList)
    g.addEdge(0, 1, 5)
    g.addEdge(0, 5, 2)
    g.addEdge(1, 2, 4)
    g.addEdge(2, 3, 9)
    g.addEdge(3, 4, 7)
    g.addEdge(3, 5, 3)
    g.addEdge(4, 0, 1)
    g.addEdge(5, 4, 8)
    g.addEdge(5, 2, 1)

    for v in g:
        for w in v.getConnections():
            print("(%s,%s)" % (v.getId(), w.getId()))
