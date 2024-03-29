# Introduction to Python programming - Day 3
#### Some code examples come from [Teach Your Kids to Code](http://teachyourkidstocode.com/) by Dr. Bryson Payne

### Reviewing what we learned. 

#### Variables

apple = 4
orange = 5 

```
print(apple + orange
print(apple * orange)
```
---

### A simple poem
```
print("This program will help you write a simple three line poem")
first_line  = input("What is the first line of the poem?")
second_line = input("What is the second line of the poem?")
third_line = input("What is the third line of the poem?")
print(first_line)
print(second_line)
print(third_line)

```
----
### Review of the Turtle

1. Write a four line program to draw a square
2. Change the pencolor to "blue". 
3. Change the pensize to 3

----
----

### New Turtle Learning

```
# A new spiral
import turtle as t
t.shape("turtle")
t.pencolor("blue")
t.pensize(4)
t.speed(5)

for x in range(4):
t.forward(100)
t.left(90)
```
1. Change the color to green. 
2. Change the color to red.
3. Change the pensize to make the line thinner.
4. Change the turtle shape.(“arrow”, “turtle”, “circle”, “square”, “triangle”, “classic”.)
5. Make the turtle go futher than 100 pixels. 
6. Change the angle of the turtle turn. 

### Turtle Spiral
```
import turtle as t
for x in range(100):
 t.circle(x)
 t.left(91)
 ```
 1. Change the 't.circle' value to x**2
 2. Change the turn from left to right = t.right(91)
 3.  Add color to the spiral with "turtle.pencolor"
 4.  Change the background color with "t.bgcolor" to blue. 

#### New Spiral -- experiment with changing the background color.
```
import turtle as t
t.speed(0)
t.pencolor("red")
t.bgcolor("black")
for x in range(100):
    t.circle(x*2)
    t.left(91)
```
---
#### Try a new color spiral using a list of colors.
```
import turtle as t
colors = ["red", "yellow", "blue", "green"]
for x in range(100):
 t.pencolor(colors[x%4])
 t.forward(x)
 t.left(91)
```
 ---`
 
 #### Multi-color spiral
 ```
import turtle as t
colors = ["red", "yellow", "blue", "green"]
for x in range(100):
 t.pencolor(colors[x%4])
 t.circle(x)
 t.left(91)
 ```
 ---
 1. Change the background to black
 2. Change the background to blue
 3. Change a color(s) in the colors list

---

#### [] = The square brackets indicate a 'list' in Python. Objects in lists can be reordered. In this next spiral we are going to use a list of colors which we will circulate through which will add more color to our program. Notice that in this list the objects are enclosed in "double quotes." 
```
# ColorSquareSpiral.py
import turtle as t
colors = ["red", "yellow", "blue", "green"]
for x in range(100):
 t.pencolor(colors[x%4])
 t.forward(x)
 t.left(91)
 ```
---
1. Add a color to the list and be sure to change the 't.pencolor(colors[x%5])
2. Other colors you can use are "orange" "purple" "black"
3. change t.forward to (x*2), x**2 
4. change the direction of the turn to right
5. change the range to 500
----
#### Now we are going to use the same list of colors to draw a spirals. 
```
# ColorCircleSpiral.py
import turtle as t
t.bgcolor("black")
colors = ["red", "yellow", "blue", "green"]
for x in range(100):
 t.pencolor(colors[x%4])
 t.circle(x)
 t.left(91)
```
---
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
---
### Try this code that uses the 'time' module.
```
# Experiment with time function

import turtle as t
import time
t.speed(0)
t.pencolor("blue")
for i in range(100):
    t.forward(190)
    t.right(86)
    
time.sleep(3)
t.penup()
t.setpos(-100,100)
t.pendown()
t.pencolor("green")
for x in range(100):
    t.forward(190)
    t.left(86)
    
 ```
 ___
1. Experiment with changing the position, the pen color and using 'penup' and 'pendown' 
2. Explore the 'time' module and its methods. 

 
 

