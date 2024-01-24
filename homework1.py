print("hello world again")
print("hi")

a=36
B=555
print(a+B)

MQ = input("Am I cool:")
MQ = MQ.capitalize()
MQ = MQ.strip()

if MQ == "Yes":
    print("Correct")
elif MQ == "No":
    print("Incorrect")

import turtle
import random

s = int(input("Enter number of sides(3 or more): "))

wn = turtle.Screen()
wn.bgcolor("Blue")
shaggy = turtle.Turtle()
shaggy.shape('turtle')
shaggy.color('red')

x = random.randrange(-300,300)
y = random.randrange(-200,200)

shaggy.penup()
shaggy.goto(x,y)
shaggy.pendown()

Angle = 360/s


for i in range(s):
    shaggy.stamp()
    shaggy.forward(100)
    shaggy.left(Angle)