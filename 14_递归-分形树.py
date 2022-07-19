# -*- coding: utf-8 -*-
# @Author : yxn
# @Date : 2022/1/27 21:01 
# @IDE : PyCharm(2021.3.1) Python3.98
import turtle


def tree(branch_len):
    if branch_len > 5:  # 递归结束条件:树干太短不画
        t.forward(branch_len)  # 画树干
        t.right(20)  # 右倾斜20度
        tree(branch_len - 15)
        t.left(40)  # 左倾斜20度
        tree(branch_len - 15)
        t.right(20)  # 回正
        t.backward(branch_len)  # 海归退回原来位置


if __name__ == '__main__':
    t = turtle.Turtle()
    t.left(90)
    t.penup()
    t.backward(100)
    t.pendown()
    t.pencolor('green')
    t.pensize(2)
    tree(75)
    t.hideturtle()
    turtle.down()
