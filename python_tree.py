#Create object 
#create function for tree
#move up
#Create turtle o
# Turn right 30 degrees
#customize

import turtle
import time
tree = turtle.Turtle()
tree.left(90)
tree.speed(0)
tree.color("brown")

def drawTree(i):
  if i <= 10:
    return
  else:
    tree.forward(i)
    tree.left(30)
    drawTree(i*.7)
    tree.right(60)
    drawTree(i*.7)
    tree.left(30)
    tree.backward(i)


drawTree(100)

turtle.done()