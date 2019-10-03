# NAME - Akshant Jain
# CLASS - CS 111 - PROJECT 1
# NET ID - ajain78
# Lab Time - Monday, 10:00 AM - 10:50 AM

# Use of File Picker for Picture
file = pickAFile()
print(file)

scene = makePicture(file)

# DEFINING VARIOUS FUCTIONS-

# 1).Defining function to draw a square of any side-length using loops
def drawSquare(turtle, length):
 x=0
 while (x<4):
  forward(turtle, length)
  turnRight(turtle)
  x=x+1

# 2).Defining function to draw a hexagon of any side-length using loops
def drawHexagon(turtle, length):
 x=0
 while (x<6):
  forward(turtle, length)
  turn(turtle, 360/6)
  x=x+1

# 3).Defining funuction to draw a rectangle of any side-length-breadth without loops
def drawRectangle(turtle, a, b):
 x=0
 while (x<2):
  forward(turtle, a)
  turnRight(turtle)
  forward(turtle, b)
  turnRight(turtle)
  x=x+1

# 4).Defining function to draw circle using loops
def drawCircle(turtle, sides):
  loopcount = 0
  while (loopcount < sides):
   forward(turtle, 10)
   turn(turtle, 360/sides)
   loopcount = loopcount + 1

# 5).Defining a function to draw a 5-pointed star using loops
def drawStar(turtle):
 x=1
 while (x<=5): 
    forward(turtle,15)
    turn(turtle, 144)
    x=x+1

# 6).Defining a function to draw a multi-pointed star using drawStar function and loops
def multiStar(turtle):
 turns=0
 while (turns<10):
  drawStar(turtle)
  turtle.turn(360/10)
  turns=turns+1

# 7).Defining a function to draw a increasing width line using loops
def Increase(turtle):
 x=0
 while(x<7):
  turtle.setPenWidth(7*x/4)
  forward(turtle, 70)
  x=x+1

# 8).Defining a function to draw a cocentric circle to make a moon using drawCircle Function(Function #3) 
def ConcentricCircles(turtle, sides, space):
 x=1
 while (x<4):
  drawCircle(turtle, sides*x)
  penUp(turtle)
  turn(turtle, 270)
  forward(turtle, space)
  turnRight(turtle)
  penDown(turtle)
  x=x+1

#9).Defining a function to draw a parallelogram using loops
def drawParallelogram(turtle, a, b):
 x=0
 while (x<2):
  forward(turtle, a)
  turn(turtle, 60)
  forward(turtle, b)
  turn(turtle, 120)
  x=x+1

#10).Defining a function for arranging squares on each floor using loops
def windows(turtle, length):
 x=0
 while (x<3):
  penUp(turtle)
  forward(turtle, 800/7)
  turn(turtle, 180)
  penDown(turtle)
  drawSquare(turtle, length)
  turn(turtle, 180)
  x=x+1

#11).Defining function to arrange windows in a floor order
def Floors(turtle, length):
 x=0
 while (x<7):
  penUp(turtle)
  forward(turtle, 400/7)
  turnRight(turtle)
  forward(turtle, 100)
  turnRight(turtle)
  forward(turtle, 400)
  turn(turtle, 180)
  penDown(turtle)
  windows(turtle, length)
  x=x+1
  

# Creating Turtles and setting up their attributes

t1=makeTurtle(scene)
t1.setPenColor(white)
t1.setPenWidth(1)

t2=makeTurtle(scene)
t2.setPenColor(white)
t2.setPenWidth(2)

t3=makeTurtle(scene)
t3.setPenColor(white)
t3.setPenWidth(8)

t4=makeTurtle(scene)
t4.setPenColor(white)
t4.setPenWidth(50)

# SETTING UP THE POSITION AND ALIGNMENT OF ALL TURTLES.

# Position of turtle: t1
penUp(t1)
turnRight(t1)
forward(t1, 250)
turnLeft(t1)
forward(t1, 380)
turn(t1, 102)
penDown(t1)

# Position of turtle: t2
penUp(t2)
turnRight(t2)
forward(t2, 250)
turnLeft(t2)
forward(t2, 380)
turn(t2, 103)
forward(t2, 485) 
penDown(t2)

# Position of turtle: t3
penUp(t3)
turn(t3, 180)
forward(t3, 490)
turnRight(t3)
forward(t3, 300)
penDown(t3)

# Position of turtle: t4
penUp(t4)
turnRight(t4)
forward(t4, 650)
turnLeft(t4)
forward(t4, 400)
penDown(t4)

Increase(t1)
multiStar(t2)
ConcentricCircles(t4, 10, 8)

t3.setPenColor(white)

drawRectangle(t3, 400, 900)

forward(t3, 150)
penDown(t3)

t3.setPenWidth(2)

drawRectangle(t3, 100, 150)

forward(t3, 50)
turnRight(t3)
forward(t3, 150)
turnRight(t3)
forward(t3, 50)
turnLeft(t3)
penUp(t3)
forward(t3, 15)
turnRight(t3)
forward(t3, 25)
turn(t3, 180)
penDown(t3)

t3.setPenWidth(2)

drawParallelogram(t3, 150, 30)

penUp(t3)
forward(t3, 25)
turnLeft(t3)
forward(t3, 165)
turnRight(t3)
forward(t3, 250)
turnRight(t3)
forward(t3, 900)
turnRight(t3)
forward(t3, 342)
penDown(t3)

t3.setPenWidth(5)

Floors(t3, 400/6)

penUp(t3)
forward(t3, 65)
turnRight(t3)
forward(t3, 200)
turnRight(t3)
forward(t3, 100)
turnRight(t3)
forward(t3, 70)
penDown(t3)

t3.setPenWidth(3)

drawHexagon(t3, 40)

penUp(t3)
turn(t3, 90)
turnRight(t3)
forward(t3, 70)
turnRight(t3)
forward(t3, 250)
turnRight(t3)
forward(t3, 80)
penDown(t3)

t3.setPenWidth(3)

drawHexagon(t3, 40)

# SHOWING PICTURE
scene.show()