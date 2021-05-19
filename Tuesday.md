# Introduction to Python programming - Day 2
#### Some code examples come from [Teach Your Kids to Code](http://teachyourkidstocode.com/) by Dr. Bryson Payne.

### Reviewing what we learned. 

print("Hello World")

print("My name is your_name")

### In the REPL (Read Evaluate Print Loop)
Add these numbers:

2+10  

2+100  


***

Subtract these numbers:

10-2  

100-45  

1000-300

***

Multiply these numbers:

100*3  

150*4  

300*1000 


***

Divide these numbers:

100/33  

200/40 

10/2  


***

#### Exponents

2**2  

10**2  

100**3  


***

###Introducing Variables

name = "Your_name"

print(name)

type(name)

*** 


***

apple = 2  

orange = 5  

print(orange-apple)

print(orange*apple)

print(orange/apple)

type(orange)

***

pi = 3.14

type(pi)
***
#### Saving programs
Click on the "+" sign in the Mu Editor. This opens a new program writing window. Use a "#" on the first line to add a comment about the purpose of the program or to explain code. All Python programs are saved with a ".py" added to the end of the program. 

#### First program
```
# YourName.py
name = input("What is your name?\n")
print("Hi, ", name)

```
Could you build on that? What could you add? 

#### Having fun with Python
```
# Fun with words
adjective = input("Please enter an adjective: ")
noun = input("Please enter a noun: ")
verb = input("Please enter a verb ending in -ed: ")
print("Your MadLib:")
print("The", adjective, noun, verb, "over the lazy brown dog.")
```
---
#### Turtle Graphics in Python
1. Import the Turtle module
2. Talk "Turtle" to Python

```
# TurtleSquare
import turtle
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
```
##### What happened? 

Let's add some color to our pen.
```
# TurtleSquare.py with color

import turtle
turtle.pencolor("blue")
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
```
##### Add a colored pen and pensize
```
# TurtleSquare.py with color and pensize

import turtle
turtle.pencolor("blue")
turtle.pensize(2)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
```
#### Use a "for loop" to draw a square easier
```
# Draw square with for loop

import turtle as t
for i in range(4):
    t.forward(100)
    t.right(90)
    

    
```
#### Draw a square spiral

```
# SquareSpiral1.py - Draws a square spiral
import turtle as t
for x in range(100):
 t.forward(x)
 t.left(90)
 ```
 ##### Now change the input values.
 ```
 # SquareSpiral1.py - Draws a square spiral
import turtle as t
for x in range(100):
 t.forward(x*2)
 t.left(94)
 ```
 ##### Now a circle spiral
 ```
import turtle as t
for x in range(100):
    t.circle(x)
    t.left(91)
   
 ```
 ##### Change the values and have some fun. 
 1. Speed up the turtle with 't.speed(0)'
 2. Change the color of the pen with 't.pencolor("blue")
 3. Change the pen size with 't.pensize(4)'
 4. Increase the circle with an exponent
 5. Change the direction of the turtle with 't.right' 
 
 
    





