# -*- coding: utf-8 -*-
# @Author : yxn
# @Date : 2022/1/27 21:38 
# @IDE : PyCharm(2021.3.1) Python3.98
def moveTower(height, fromPole, withPole, toPole):
    if height >= 1:
        moveTower(height - 1, fromPole, toPole, withPole)
        moveDisk(height, fromPole, toPole)
        moveTower(height - 1, fromPole, toPole, withPole)


def moveDisk(disk, fromPole, toPole):
    print(f"Moving disk[{disk}] from {fromPole} to {toPole}")


if __name__ == '__main__':
    moveTower(5, "#1", "#2", "#3")
