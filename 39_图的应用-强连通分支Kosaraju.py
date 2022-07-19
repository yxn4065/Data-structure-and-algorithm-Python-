# -*- coding: utf-8 -*-
# @Author : yxn
# @Date : 2022/7/19 13:15 
# @IDE : PyCharm(2022.1.3) Python3.9.13
"""
在有向图当中，如果两个点之间彼此存在一条路径相连，那么我们称这两个点强连通。
那么推广一下，如果一张图当中的一个部分中的每两个点都连通，那么这个部分就称为强连通分量。
强连通分量一般是一张完整的图的一个部分
算法步骤:
1.我们通过后序遍历的方式遍历整个有向图，并且维护每个点的出栈顺序
2.我们将有向图反向，根据出栈顺序从大到小再次遍历反向图
3.对于点u来说，在遍历反向图时所有能够到达的v都和u在一个强连通分量当中
另外的常用强连通分支算法
Tarjan算法和Gabow算法(对Tarjan的改进)

"""
N = 7
graph, rgraph = [[] for _ in range(N)], [[] for _ in range(N)]
used = [False for _ in range(N)]
popped = []  # 存储出栈节点


# 建图
def add_edge(u, v):
    graph[u].append(v)
    rgraph[v].append(u)


# 正向遍历
def dfs(u):
    used[u] = True
    for v in graph[u]:
        if not used[v]:
            dfs(v)
    popped.append(u)


# 反向遍历
def rdfs(u, scc):
    used[u] = True
    scc.append(u)
    for v in rgraph[u]:
        if not used[v]:
            rdfs(v, scc)


# 建图，测试数据
def build_graph():
    add_edge(1, 3)
    add_edge(1, 2)
    add_edge(2, 4)
    add_edge(3, 4)
    add_edge(3, 5)
    add_edge(4, 1)
    add_edge(4, 6)
    add_edge(5, 6)


if __name__ == "__main__":
    build_graph()
    for i in range(1, N):
        if not used[i]:
            dfs(i)

    used = [False for _ in range(N)]
    # 将第一次dfs出栈顺序反向
    popped.reverse()
    for i in popped:
        if not used[i]:
            scc = []
            rdfs(i, scc)
            print(scc)
