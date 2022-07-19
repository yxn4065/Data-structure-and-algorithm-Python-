# -*- coding: utf-8 -*-
# @Author : yxn
# @Date : 2022/7/19 13:26 
# @IDE : PyCharm(2022.1.3) Python3.9.13
"""
最短路径问题
使用广度优先搜索  每个节点记录距离
每次出列距离最小的点
通过更新修改距离和父节点
"""
from pythonds.graphs import PriorityQueue, Graph, Vertex


def dijkstra(a_graph, start):  # dijkstra算法
    pq = PriorityQueue()  # 建立优先队列，存储点
    start.setDistance(0)
    pq.buildHeap([(v.getDistance(), v) for v in a_graph])
    while not pq.isEmpty():  # 队列不为空时
        current_vertex = pq.delMin()  # 取出最小的点
        for next_vertex in current_vertex.getConnections():
            new_dist = current_vertex.getDistance() + current_vertex.getWeight(next_vertex)
            if new_dist < next_vertex.getDistance():  # 距离更小  更新
                next_vertex.setDistance(new_dist)
                next_vertex.setPred(current_vertex)
                pq.decreaseKey(next_vertex, new_dist)


def dijkstra_min_distance(start, target, graph):
    if start not in graph['V'] or target not in graph['V']:
        return '无效起点或终点！'

    visited = {}  # 记录顶点的访问情况
    dist = {}  # 记录最短距离
    path = [start]  # 记录最短路径上的每一个顶点
    V, E = graph['V'], graph['E']
    for node in V:
        visited[node] = 0  # 0表示没有访问 1表示已访问
        dist[node] = -1  # -1表示无限远
    dist[start] = 0  # 到自己的距离为0
    visited[start] = 1

    # 初始化到各顶点的距离
    for e in E:
        if e[0] == start:
            dist[e[1]] = E[e]

    # while not all(visited.values()):  # 直到访问完所有顶点 求到所有顶点的最短距离
    while not visited[target]:  # 仅求到终点的距离
        # 在所有可达的但未访问的顶点中，寻找距离最近的一个
        cur_E_li = [(e, E[e]) for e in E if visited[e[0]] and not visited[e[1]]]  # 所有可达但未访问的顶点
        cur_E_li.sort(key=lambda a: a[1])  # 按照距离进行排序
        print(cur_E_li)
        min_edge_w = cur_E_li[0]  # 第一个就是距离最短的那一个
        new_start_node = min_edge_w[0][1]

        # 刷新最短距离
        for node in dist:
            new_edge = (new_start_node, node)
            if new_edge in E:
                if dist[node] == -1:
                    dist[node] = dist[new_start_node] + E[new_edge]
                else:
                    dist[node] = min(dist[node], dist[new_start_node] + E[new_edge])

        # 更新visited
        visited[new_start_node] = 1
        path.append(new_start_node)  # 将当前节点更新到最短路径上

    return path, dist[target]


if __name__ == '__main__':
    V = {1, 2, 3, 4, 5}  # 顶点集

    E = {  # 边集
        (1, 2): 10,  # (起点,终点):权值
        (1, 5): 5,
        (2, 3): 1,
        (2, 5): 2,
        (3, 4): 4,
        (4, 1): 7,
        (4, 3): 6,
        (5, 2): 3,
        (5, 3): 9,
        (5, 4): 2,
    }
    graph = {
        'V': V,
        'E': E
    }

    print(dijkstra_min_distance(1, 4, graph))
