# -*- coding: utf-8 -*-
# @Author : yxn
# @Date : 2022/1/25 21:22 
# @IDE : PyCharm(2021.3.1) Python3.98
"""问题还原:
对于一个打印店在某一小时内大约有10名学生在场,每人会发起2次左右的打印,每次打印1~20页
打印机标准模式每分钟打印5页,质量好,草稿模式每分钟10页质量下降,在不会等太久的前提下实现高质量打印
建模过程
1.首先对问题进行抽象，确定相关的对象和过程，抛弃那些对问题实质没有关系的学生性别、年龄 、打印机型号、打印内容、纸张大小等等众多细节。
抽象的对象：打印任务、打印队列、打印机
打印任务的属性：提交时间、打印页数
打印队列的属性：具有FIFO性质的打印任务队列打印机的属性：打印速度、是否忙

2.生成和提交打印任务
确定生成概率：实例为每小时会有10个学生提交的20个作业，这样，概率是每180秒会有1个作业生成并提交，概率为每秒1/180。
确定打印页数：实例是1～20页，那么就是1～20页之间概率相同。

3.过程实施打印
当前的打印作业：正在打印的作业
打印结束倒计时：新作业开始打印时开始倒计时 ，回0表示打印完毕，可以处理下一个作业

4.模拟时间
统一的时间框架：以最小单位（秒）均匀流逝的时间，设定结束时间
同步所有过程：在一个时间单位里，对生成打印任务和实施打印两个过程各处理一次
"""
import random
from pythonds.basic.queue import Queue


class Printer:
    def __init__(self, ppm):
        self.pagerate = ppm  # 打印速度
        self.currentTask = None  # 打印任务
        self.timeRemaining = 0  # 打印倒计时

    def tick(self):  # 打印一秒
        if self.currentTask is not None:
            self.timeRemaining -= 1
            if self.timeRemaining <= 0:
                self.currentTask = None

    def busy(self):  # 打印是否忙
        if self.currentTask is not None:
            return True
        else:
            return False

    def startNext(self, newtask):  # 打印新的作业
        self.currentTask = newtask
        self.timeRemaining = newtask.getPages() * 60 / self.pagerate


class Task:
    def __init__(self, time):
        self.timestamp = time  # 生成时间戳
        self.pages = random.randrange(1, 21)  # 打印页数

    def getStamp(self):
        return self.timestamp

    def getPages(self):
        return self.pages

    def waitTime(self, currenttime):
        return currenttime - self.timestamp  # 等待时间


def newPrintTask():
    num = random.randrange(1, 181)  # 1/180的概率生成作业
    if num == 180:
        return True
    else:
        return False


def simulation(numSeconds, pagesPerMinute):  # 开始模拟
    labprinter = Printer(pagesPerMinute)
    printQueue = Queue()
    waitingtimes = []
    for currentSecond in range(numSeconds):
        if newPrintTask():
            task = Task(currentSecond)
            printQueue.enqueue(task)
        if (not labprinter.busy()) and (not printQueue.isEmpty()):
            nexttask = printQueue.dequeue()
            waitingtimes.append(nexttask.waitTime(currentSecond))
            labprinter.startNext(nexttask)
        labprinter.tick()

    averageWait = sum(waitingtimes) / len(waitingtimes)
    print("Average Wait %6.2f secs %3d tasks remaining." % (averageWait, printQueue.size()))


if __name__ == '__main__':
    # 按照5ppm,1小时的设定,模拟运行10次
    for i in range(10):
        simulation(3600, 5)
