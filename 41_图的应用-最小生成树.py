# -*- coding: utf-8 -*-
# @Author : yxn
# @Date : 2022/7/19 13:31 
# @IDE : PyCharm(2022.1.3) Python3.9.13
"""
最小生成树
解决广播问题  所有节点都要收到一次信息
选择具有最小权重的生成树
使用贪心算法 Prim  每次添加一条权重最小的可以添加的边（一端在树里，一端连外面的点）
"""

import sys

from pythonds.graphs import PriorityQueue
from math import inf


def prim(G, start):
    pq = PriorityQueue()  # 建立优先队列
    for v in G:
        v.setDistance(sys.maxsize)
        v.setPred(None)
    start.setDistance(0)
    pq.buildHeap([(v.getDistance(), v) for v in G])
    while not pq.isEmpty():
        current_vertex = pq.delMin()  # 取出当前距离最小的点
        for next_vertex in current_vertex.getConnections():
            new_cost = current_vertex.getWeight(next_vertex)  # current和next之间边的权重
            if next_vertex in pq and new_cost < next_vertex.getDistance():  # 确保加入的节点不再当前生成树里
                next_vertex.setPred(current_vertex)
                next_vertex.setDistance(new_cost)
                pq.decreaseKey(next_vertex, new_cost)


def prim_min_span_tree(graph):
    visited = {node: 0 for node in graph}  # 用于表示一个顶点是否被访问
    root = 1  # 任意取一个顶点
    visited[root] = 1
    T_w = {}

    while not all(visited.values()):  # 只要不是所有的顶点被访问了，就一直进行下去

        # 查找与树T距离最近，但未被访问的顶点
        not_visited_nodes = {node for node in graph if not visited[node]}  # 未被访问的顶点
        visited_nodes = {node for node in graph if visited[node]}  # 树T

        min_distance = inf
        min_node = None
        min_edge = None

        # 求到树T距离最近的节点
        for t in visited_nodes:
            for node in not_visited_nodes:
                cur_edge = '-'.join(map(str, sorted((t, node))))
                cur_w = W.get(cur_edge, -1)  # 当前边的权重
                if cur_w != -1 and cur_w < min_distance:
                    min_distance = cur_w
                    min_node = node
                    min_edge = cur_edge

        print(f'当前距离树T最近的节点:{min_node},权重为:{min_distance}')
        T_w[min_edge] = min_distance  # 添加到树T的权重记录表中
        visited[min_node] = 1  # 更新当前节点为已访问
    print(T_w)


if __name__ == '__main__':
    # 邻接表法表示图
    graph = {
        1: {2, 3, 4},
        2: {1, 3, 5},
        3: {1, 2, 4, 5, 6},
        4: {1, 3, 6},
        5: {2, 3, 6},
        6: {3, 4, 5}
    }

    W = {
        '1-2': 6,
        '1-3': 1,
        '1-4': 5,
        '2-3': 5,
        '2-5': 3,
        '3-4': 5,
        '3-5': 6,
        '3-6': 4,
        '4-6': 2,
        '5-6': 6
    }  # 权重
    print(prim_min_span_tree(graph))
