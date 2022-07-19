# -*- coding: utf-8 -*-
# @Author : yxn
# @Date : 2022/2/1 11:01 
# @IDE : PyCharm(2021.3.1) Python3.98
def recDC(coinValueList, change, knownResults):
    minCoins = change
    if change in coinValueList:  # 递归基本结束条件
        knownResults[change] = 1  # 记录最优解
        return 1
    elif knownResults[change] > 0:  # 查表成功,直接用最优解
        return knownResults[change]
    else:
        for i in [c for c in coinValueList if c <= change]:
            numCoins = 1 + recDC(coinValueList, change - i, knownResults)
            if numCoins < minCoins:
                minCoins = numCoins
                # 找到最优解,记录到表中
                knownResults[change] = minCoins
        return minCoins


def dpMakeChange(coinValueList, change, minCoins, coinsUsed):
    """动态规划算法"""
    # 从1分开始到change逐个计算最少硬币数
    for cents in range(change + 1):
        # 1.初始化一个最大值
        coinCount = cents
        newCoins = 1  # 初始化一个新加硬币
        # 2.减去每个硬币向后查找最少硬币数,同时记录总的最少数
        for j in [c for c in coinValueList if c <= cents]:
            if minCoins[cents - j] + 1 < coinCount:
                coinCount = minCoins[cents - j] + 1
                newCoins = j  # 对应最小数量,所减的硬币
        # 3.得到当前最少硬币数,记录到表中
        minCoins[cents] = coinCount
        coinsUsed[cents] = newCoins  # 记录本步骤所加的一个硬币
    # 返回最后一个结果
    return minCoins[change]


def printCoins(coinsUsed, change):
    coin = change
    while coin > 0:
        thisCoin = coinsUsed[coin]
        print(thisCoin)
        coin -= thisCoin


if __name__ == '__main__':
    memo = [0] * 64
    # print(memo == ([0] * 64))  # TODO False
    print(recDC([1, 5, 10, 25], 63, memo))
    # print(memo)

    print("*" * 20)
    print(dpMakeChange([1, 5, 10, 21, 25], 63, [0] * 64, memo), " coins")

    print(printCoins(memo, 63))
