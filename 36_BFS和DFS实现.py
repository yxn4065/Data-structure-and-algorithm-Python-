# -*- coding: utf-8 -*-
# @Author : yxn
# @Date : 2022/7/18 22:13 
# @IDE : PyCharm(2022.1.3) Python3.9.13
"""
BFS:广度优先搜索(可通过队列实现)
DFS:深度优先搜索(可通过栈实现)
"""

# BFS用队列解决搜索问题
from pythonds import Graph


def BFS(start_node):
    queue = [start_node]
    seen = set()
    seen.add(start_node)
    while len(queue) > 0:
        now_node = queue.pop(0)
        for node in graph[now_node]:
            if node not in seen:
                queue.append(node)
                seen.add(node)
        print(now_node)


# DFS 用栈解决搜索问题
def DFS(start_node):
    stack = [start_node]
    seen = set()
    seen.add(start_node)
    while len(stack) > 0:
        now_node = stack.pop()
        for node in graph[now_node]:
            if node not in seen:
                stack.append(node)
                seen.add(node)
        print(now_node)


# 求最短路径
def BFS_(start_node):
    queue = [start_node]
    seen = set()
    seen.add(start_node)
    parent = {start_node: None}  # 存储路径
    while len(queue) > 0:
        now_node = queue.pop(0)
        for node in graph[now_node]:
            if node not in seen:
                queue.append(node)
                parent[node] = now_node
                seen.add(node)
        # print(now_node)
    print(parent)
    # 搜索A--E的路径
    v = 'E'
    while v is not None:
        print(v)
        v = parent[v]


class DFSGraph(Graph):
    """通用的DFS
    BFS采用队列储存待访问顶点,DFS则是通过递归调用,隐式使用了栈"""
    def __init__(self):
        super().__init__()  # 创建子类继承父类
        self.time = 0

    def dfs(self):
        for aVertex in self:  # 颜色初始化
            aVertex.setColor("white")
            aVertex.setPred(-1)
        for aVertex in self:  # 如果有未包含的顶点则建立森林
            if aVertex.getColor() == "white":
                self.dfsvisit(aVertex)

    def dfsvisit(self, startVertex):
        startVertex.setColor("grey")
        self.time += 1  # 算法的步数
        startVertex.setDiscovery(self.time)
        for nextVertex in startVertex.getConnections():
            if nextVertex.getColor() == "white":
                nextVertex.setPred(startVertex)
                self.dfsvisit(nextVertex)  # 深度优先递归访问
        startVertex.setColor("black")
        self.time += 1
        startVertex.setFinish(self.time)


if __name__ == '__main__':
    # 建立字典：表征该点的临接点
    graph = {
        "A": ["B", "C"],
        "B": ["A", "C", "D"],
        "C": ["A", "B", "D", "F"],
        "D": ["B", "C", "E", "F"],
        "E": ["C", "D"],
        "F": ["D"]
    }

    BFS("A")
    DFS("A")
    BFS_("A")
