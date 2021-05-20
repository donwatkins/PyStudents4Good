# Introduction to Python Programming - Day 4
#### Some code examples come from [Teach Your Kids to Code](http://teachyourkidstocode.com/) by Dr. Bryson Payne.
----

#### Let's have some more fun with variables. In this program we are going to use the variable 'sides' to change the number of sides we draw each time. Write your program, save it and then run. 
```
# ColorSpiral.py
import turtle as t
t.bgcolor("black")
# You can choose between 2 and 6 sides for some cool shapes!
sides = 6
colors = ["red", "yellow", "blue", "orange", "green", "purple"]
for x in range(360):
 t.pencolor(colors[x%sides])
 t.forward(x * 3/sides + x)
 t.left(360/sides + 1)
 t.width(x*sides/200)
```
1. Change the number of sides and run the program again. 
2. What happened?
3. Change the background color to "blue".
4. Change line 5 of the program to read:  sides = eval(input("Enter a number of sides between 2 and 6: "))
5. Save it! Run it! 
6. What happened? 

---

#### Function are blocks of code we can use over and over again. Here is an example of how we create a function to draw ColorSquareSpiral.py. We create functions in Python using the 'def' argument. 

```
def my_function():
  print("Hello from a function")
  ```
  #### Run the function and then enter 'my_function()' in the REPL. 
  1. What was the output? 

```
# ColorSquareSpiral function
def ColorSquareSpiral():
    
    import turtle as t
    t.speed(0)
    t.bgcolor("black")
    colors = ["red", "yellow", "blue", "green", "orange"]
    for x in range(200):
        t.pencolor(colors[x%5])
        t.forward(x)
        t.left(91)
```
1. Save the code and give  it a name like 'ColorSquareSpiralFunction.py. 
2. 'Run' the code. Then open the REPL.
3. Open up the 'REPL' and enter 'ColorSquareSpiral()' and press enter. 
4. What happened?

#### Build a 5 pointed star wtih Python

```
# Turtle Star
import turtle as t
for i in range(5):
 t.forward(100)
 t.right(144)
 ```
 1. Change the size of the star. 
 2. Change the color of the star
 3. Change the color. Change the pen size. 

---
#### Another Star

```
# 5 point star with color

import turtle as t 
 
# decide colors
cir= ['red','green','blue','yellow','purple']
 
# decide pensize
t.pensize(4)
 
# Draw star pattern
t.penup()
t.setpos(-90,30)
t.pendown()
for i in range(5):
    t.pencolor(cir[i])
    t.forward(200)
    t.right(144)
 
t.penup()
t.setpos(80,-140)
t.pendown()
 
# choose pen color
t.pencolor("Black")
t.done()
```
#### Make a rainbow with Python
```
# Turtle Rainbow

# Import turtle package
import turtle as t
 
# Creating a turtle screen object
sc = t.Screen()
 
 
# Defining a method to form a semicircle
# with a dynamic radius and color
def semi_circle(col, rad, val):
 
    # Set the fill color of the semicircle
    t.color(col)
 
    # Draw a circle
    t.circle(rad, -180)
 
    # Move the turtle to air
    t.up()
 
    # Move the turtle to a given position
    t.setpos(val, 0)
 
    # Move the turtle to the ground
    t.down()
 
    t.right(180)
 
 
# Set the colors for drawing
col = ['violet', 'indigo', 'blue',
       'green', 'yellow', 'orange', 'red']
 
# Setup the screen features
sc.setup(600, 600)
 
# Set the screen color to black
sc.bgcolor('black')
 
# Setup the turtle features
t.right(90)
t.width(10)
t.speed(7)
 
# Loop to draw 7 semicircles
for i in range(7):
    semi_circle(col[i], 10*(
      i + 8), -10*(i + 1))
 
# Hide the turtle
t.hideturtle()
```
---
 #### Draw a color filled star
 ```
 # Color Filled Star

import turtle as t
 
# function to draw
# colored star
def colored_star():
     
    # size of star
    size = 80
     
    # object color
    t.color("red")
     
    # object width
    t.width(4)
     
    # angle to form star
    angle = 120
     
    # color to fill
    t.fillcolor("yellow")
    t.begin_fill()
     
    # form star
    for side in range(5):
        t.forward(size)
        t.right(angle)
        t.forward(size)
        t.right(72 - angle)
         
    # fill color
    t.end_fill()
 
# Driver code
colored_star()
```
---
