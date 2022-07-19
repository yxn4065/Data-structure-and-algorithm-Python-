# -*- coding: utf-8 -*-
# @Author : yxn
# @Date : 2022/7/18 22:32 
# @IDE : PyCharm(2022.1.3) Python3.9.13
"""
在一个国际象棋棋盘上，一个棋子“马（骑士），按照“马走日”的规则，从一个格子出发，
要走遍所有棋盘格怡好一次把一个这样的走棋序列称为一次“周游”
思路:首先将合法走棋次序表示为一个图,采用图搜索算法搜寻一个长度为（行×列-1）的路径，路径上包含每个顶点恰一次
"""
from pythonds import Graph


# 生成合法走棋位置
def genLegalMoves(x, y, bdSize):
    newMoves = []
    moveOffsets = [(-1, -2), (-1, 2), (-2, -1), (-2, 1), (1, -2), (1, 2), (2, -1), (2, 1)]  # 马走日的八个格子
    for i in moveOffsets:
        newX = x + i[0]
        newY = y + i[1]
        if legalCoord(newX, bdSize) and legalCoord(newY, bdSize):  # 判断移动位置是否合理
            newMoves.append((newX, newY))
    return newMoves


def legalCoord(x, bdSize):
    if 0 < x < bdSize:
        return True
    else:
        return False


def knightGraph(bdSize):  # 构建走棋关系图
    ktGraph = Graph()
    for row in range(bdSize):
        for col in range(bdSize):
            nodeId = posToNodeId(row, col, bdSize)  # 编号
            newPositions = genLegalMoves(row, col, bdSize)  # 合法走棋走到的位置
            for e in newPositions:
                nid = posToNodeId(e[0], e[1], bdSize)
                ktGraph.addEdge(nodeId, nid)  # 建立节点与边
    return ktGraph


def posToNodeId(row, col, bdSize):
    return row * bdSize + col


# 深度优先搜索
def knightTour(n, path, u, limit):
    """深度优先搜索
    :param n: 层次,即当前已经走了多少步了
    :param path:路径,走过n步之后的格子
    :param u:当前搜索的顶点
    :param limit:搜索的总深度的限制
    """
    u.setColor('grey')  # 准备搜索
    path.append(u)
    if n < limit:  # 需要继续搜索
        nbr_list = list(u.getConnections())  # 周围合法移动
        i = 0
        done = False
        while i < len(nbr_list) and not done:
            if nbr_list[i].getColor() == 'white':  # 有新节点
                done = knightTour(n + 1, path, nbr_list[i], limit)
            i += 1
        if not done:  # 说明该节点不通，往上回溯
            path.pop()
            u.setColor('white')
    else:
        done = True
    return done


def orderByAbail(n):
    """骑士周游算法的改进
    将u的合法移动目标桃盘格排序为；具有最少法移动目标的格子优先搜索
    """
    resList = []
    for v in n.getConnections():
        if v.getColor() == "white":
            c = 0
            for w in v.getConnections():
                if w.getColor() == "white":
                    c += 1
            resList.append(c, v)
    resList.sort(key=lambda x: x[0])
    return [y[1] for y in resList]


# 采用先验的知识来改进算法性能的做法，称作为“启发式规则heuristic'
# 启发式规则经常用于人工智能领域；可以有效地减小搜索范围、更快达到目标等等；
# 如棋类程序算法，会预先存入棋谱、布阵口读、高手习惯等“启发式规则”，能够在最短时间内从海量的棋局落子点搜索树中定位最佳落子。
# 例如：黑白棋中的“金角银边”口读，指导程序,优先占边角位置等等


if __name__ == '__main__':
    kt_graph = knightGraph(6)
    path = []
    knightTour(1, path, kt_graph.getVertex(5), 36)
    count = 0
    for k in path:
        print(k.id)
        count += 1
    print(count)
