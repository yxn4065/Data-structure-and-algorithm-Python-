# -*- coding: utf-8 -*-
# @Author : yxn
# @Date : 2022/7/19 13:40 
# @IDE : PyCharm(2022.1.3) Python3.9.13
"""
最短距离Dijkstra算法和最小生成树prim算法的区别非常相似，稍不留意就会造成混淆。
首先，两个算法都是利用优先队列实现，都是典型的贪心策略算法。
其次，都是以一个无向图G，起始定点start，作为参数。
其算法程序框架几乎一样，不同点如下：
1，Dijkstra算法利用节点的dist属性来记录节点到起始节点的最短权重距离，而prim算法则利用节点的dist属性来记录节点到已建树节点集合的最小权重代价；
2，Dijkstra算法每次从优先队列提取的是到起始节点最短权重距离的节点作为当前节点，而prim算法每次从优先队列提取的是到已建树节点集合最小权重代价的节点作为当前节点；
3，Dijkstra算法遍历当前节点的每一个邻接节点，如果当前节点最短权重距离加上邻接边权重，比邻接节点已有的最短权重距离还短，那就更新邻接节点的最短权重距离和前驱；
prim算法遍历当前节点的每一个安全邻接节点（不在已建树节点集合里），如果当前节点到安全邻接节点的权重，比安全邻接节点已有的最小权重代价还小，那就更新安全邻接节点的最小权重代价和前驱；
4，Dijkstra算法执行完毕后，每个节点的dist记录了到起始节点的最短距离，pred记录了最短距离路径的前驱节点；
prim算法执行完毕后，每个节点的dist记录了到前驱节点的边权重，pred记录了最小生成树路径的前驱节点，把所有dist求和，就是最小生成树的权重代价。
"""

# 最短路径
# G - 无向赋权图
# start - 开始节点
# 返回从开始节点到其它所有节点的最短带权路径
from pythonds import Graph, PriorityQueue


def dijkstra(G, start):
    pq = PriorityQueue()  # 创建优先队列
    start.setDistance(0)  # 起点距离设置为0，其它节点距离默认maxsize
    # 将节点排入优先队列，start在最前面
    pq.buildHeap([(v.getDistance(), v) for v in G])
    while not pq.isEmpty():
        # 取从start开始距离最小的节点出队列，作为当前节点
        # 当前节点已解出最短路径
        currentVert = pq.delMin()
        # 遍历节点的所有邻接节点
        for nextVert in currentVert.getConnections():
            # 从当前节点出发，逐个加上邻接节点的距离进行检验
            newDist = currentVert.getDistance() \
                      + currentVert.getWeight(nextVert)
            # 如果小于邻接节点原有距离，就更新邻接节点
            if newDist < nextVert.getDistance():
                # 更新距离值
                nextVert.setDistance(newDist)
                # 更新返回路径
                nextVert.setPred(currentVert)
                # 更新优先队列
                pq.decreaseKey(nextVert, newDist)


if __name__ == '__main__':
    G = Graph()
    ndedge = [('u', 'v', 2), ('u', 'w', 5), ('u', 'x', 1),
              ('v', 'x', 2), ('v', 'w', 3), ('x', 'w', 3),
              ('x', 'y', 1), ('w', 'y', 1), ('w', 'z', 5),
              ('y', 'z', 1)]
    for nd in ndedge:
        G.addEdge(nd[0], nd[1], nd[2])
        G.addEdge(nd[1], nd[0], nd[2])
    start = G.getVertex('u')
    dijkstra(G, start)
    print(G)


# 最小生成树prim算法
# G - 无向赋权图
# start - 开始节点
# 返回从开始节点创建最小生成树
def prim(G, start):
    pq = PriorityQueue()  # 创建优先队列
    start.setDistance(0)  # 起点最小权重代价设置为0，其它节点最小权重代价默认maxsize
    # 将节点排入优先队列，start在最前面
    pq.buildHeap([(v.getDistance(), v) for v in G])
    while not pq.isEmpty():
        # 取距离*已有树*最小权重代价的节点出队列，作为当前节点
        # 当前节点已解出最小生成树的前驱pred和对应最小权重代价dist
        currentVert = pq.delMin()
        # 遍历节点的所有邻接节点
        for nextVert in currentVert.getConnections():
            # 从当前节点出发，逐个检验到邻接节点的权重
            newCost = currentVert.getWeight(nextVert)
            # 如果邻接节点是"安全边"，并且小于邻接节点原有最小权重代价dist，就更新邻接节点
            if nextVert in pq and newCost < nextVert.getDistance():
                # 更新最小权重代价dist
                nextVert.setPred(currentVert)
                # 更新返回路径
                nextVert.setDistance(newCost)
                # 更新优先队列
                pq.decreaseKey(nextVert, newCost)

    # G = Graph()
    # ndedge = [('A', 'B', 2), ('A', 'C', 3), ('B', 'C', 1),
    #           ('B', 'D', 1), ('B', 'E', 4), ('C', 'F', 5),
    #           ('D', 'E', 1), ('E', 'F', 1), ('F', 'G', 1)]
    # for nd in ndedge:
    #     G.addEdge(nd[0], nd[1], nd[2])
    #     G.addEdge(nd[1], nd[0], nd[2])
    # start = G.getVertex('A')
    # prim(G, start)
    # print(G)
    #
    # G = Graph()
    # ndedge = [('v1', 'v2', 6), ('v1', 'v3', 1), ('v1', 'v4', 5),
    #           ('v2', 'v3', 5), ('v3', 'v4', 5), ('v2', 'v5', 3),
    #           ('v3', 'v5', 6), ('v3', 'v6', 4), ('v4', 'v6', 2),
    #           ('v5', 'v6', 6)]
    # for nd in ndedge:
    #     G.addEdge(nd[0], nd[1], nd[2])
    #     G.addEdge(nd[1], nd[0], nd[2])
    # start = G.getVertex('v1')
    # prim(G, start)
    # print(G)
