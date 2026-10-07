import turtle
from turtle import *
t = Turtle()

t.speed(10)

t.shape('turtle')

""" # def square():
#     length = 5
#     for i in range(60):
#         for i in range(4):
#             t.forward(length)
#             t.left(90)
#         length = length + (5)
#         t.right(5)
# square() """

def star(length):
    length = 7
    for i in range(60):
        for i in range(5):
            t.forward(length)
            t.left(144)
        length = length + (5)
        t.right(5)
star(5)
turtle.done
