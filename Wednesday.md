# Introduction to Python programming - Day 3

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

#### New Spiral 
```
import turtle as t
t.speed(0)
t.pencolor("red")
t.bgcolor("black")
for x in range(100):
    t.circle(x*2)
    t.left(91)
    ```
    
    ```






