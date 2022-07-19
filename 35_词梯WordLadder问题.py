# -*- coding: utf-8 -*-
# @Author : yxn
# @Date : 2022/7/18 22:00 
# @IDE : PyCharm(2022.1.3) Python3.9.13
"""
“ 爱 丽 丝 漫 游 奇 境 ” 的 作 者 Lewis Carroll在1878年所发明的单词游戏
从一个单词演变到另一个单词， 其中的过程可以经过多个中间单词
要求是相邻两个单词之间差异只能是1个字母，如FOOL变SAGE：
FOOL >> POOL >> POLL >> POLE >> PALE>> SALE >> SAGE
我们的目标是找到最短的单词变换序列,采用图来解决这个问题的步骤如下：
将可能的单词之间的演变关系表达为图，采用“广度优先搜索 BFS”，来搜寻从开始单词到结束单词之间的所有有效路径，
选择其中最快到达目标单词的路径
"""
from pythonds import Graph, Queue

"""建立边的最直接算法， 是对每个顶点（单词） ， 与其它所有单词进行比较， 如果相差仅1个字母， 则建立一条边
时间复杂度是O(n^2)，对于所有4个字母的5110个单词，需要超过2600万次比较
改进的算法是创建大量的桶， 每个桶可以存放若干单词
桶标记是去掉1个字母，通配符“_”占空的单词"""

word_file = 'fourletterwords.txt'


def build_graph(word_file):
    """采用字典建立桶"""
    d = {}  # 桶的集合
    g = Graph()  # 单词图
    with open(word_file, 'r') as f:
        for line in f:
            word = line[:-1]
            for i in range(len(word)):  # 给单词加下划线，并归到不同的桶# 4字母单词可属于4个桶
                bucket = word[:i] + '_' + word[i + 1:]
                if bucket in d:
                    d[bucket].append(word)
                else:
                    d[bucket] = [word]
        for bucket in d.keys():  # 添加边# 同一个桶单词之间建立边
            for word1 in d[bucket]:
                for word2 in d[bucket]:
                    if word1 != word2:
                        g.addEdge(word1, word2)
    f.close()

    return g


#  广度优先搜索
def bfs(g, start):
    start.setDistance(0)
    start.setPred(None)
    vertQueue = Queue()  # 目前需要探索的顶点队列
    vertQueue.enqueue(start)  # 将起始点放入队列
    while vertQueue.size() > 0:  # 队列不为空时
        current_vert = vertQueue.dequeue()  # 取出一个顶点
        for nbr in current_vert.getConnections():
            if nbr.getColor() == 'white':  # 白色说明还没有探索过
                nbr.setColor('gray')  # 设置为准备探索
                nbr.setDistance(current_vert.getDistance() + 1)  # 设置距离
                nbr.setPred(current_vert)  # 设置前驱节点
                vertQueue.enqueue(nbr)  # 将新发现的节点入队
        current_vert.setColor('black')  # 遍历完后将当前节点设为已探索


# 回溯节点  找到最短词梯
def traverse(y):
    x = y
    while x.getPred():
        print(x.getId())
        x = x.getPred()
    print(x.getId())


if __name__ == '__main__':
    word_graph = build_graph(word_file)  # 生成单词图
    # print(word_graph.getVertex('FOOL'))
    bfs(word_graph, word_graph.getVertex('FOOL'))  # 广度搜索
    traverse(word_graph.getVertex('SAGE'))  # 打印词梯
