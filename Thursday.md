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
#### Random color choices
```
import turtle as t
import random

colors  = ["red","green","blue","orange","purple","pink","yellow"] # Make a list of colors to picvk from

t.width(10) #What does this line do?


length = 10
for count in range(200):
  color = random.choice(colors) #Choose a random color
  t.forward(length)
  t.right(135)
  t.color(color) # Why is color spelt like this?
  length = length + 5
  ```
  ---
  
  #### Card game using random function
  
  ```
  # Card Game
import random
faces = ["Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace"]
suits = ["Hearts", "Clubs", "Spades", "Diamonds"]
print("Your card choice is.")
print(random.choice(faces))
print("Of")
print(random.choice(suits))
```

---

#### Password generator with random
```
# Password Generator

import string
import random
characters = string.ascii_letters + string.punctuation  + string.digits
password =  "".join(random.choice(characters) for x in range(random.randint(8,16)))
print(password)
```
---
#### We can create random spirals using the random module together with the turtle module. 

```
#RandomSpirals.py
import random
import turtle as t
t.bgcolor("black")
colors = ["red", "yellow", "blue", "green", "orange", "purple", 
          "white", "gray"]
for n in range(50):
    # Generate spirals of random sizes/colors at random locations
    t.pencolor(random.choice(colors))   # Pick a random color 
    size = random.randint(10,40)        # Pick a random spiral size
    # Generate a random (x,y) location on the screen
    x = random.randrange(-t.window_width()//2,
                         t.window_width()//2)
    y = random.randrange(-t.window_height()//2,
                         t.window_height()//2)
    t.penup()
    t.setpos(x,y)
    t.pendown()
    for m in range(size):
        t.forward(m*2)
        t.left(91)
 ```
 ---
 # Resources for Learners
#### [Welcome to Python](https://www.python.org/) 

#### [PyCon.US](https://us.pycon.org/2021/about/what-is-pycon/) y

#### Code Examples from the Raspberry Pi Foundation. [Raspberry Pi:Teaching Turtles](https://github.com/RaspberryPiFoundation/python-curriculum/blob/master/pl-PL/lessons/Teaching%20Turtles/Teaching%20Turtles.md)

### [Adventures in Raspberry Pi](https://www.amazon.com/Adventures-Raspberry-Carrie-Anne-Philbin/dp/1119269067/ref=tmm_pap_swatch_0?_encoding=UTF8&qid=&sr=)-- Carrie Anne Philbin

### [Teach Your Kids to Code](https://www.amazon.com/dp/1593276141/ref=cm_sw_r_cp_ep_dp_F1k6BbAXS5268)-- Bryson Payne

### [Python for Kids](https://www.amazon.com/dp/B00ADX21Z6/ref=cm_sw_em_r_mt_dp_U_fqhSDbFGRZZJ2) -- Jason Briggs

### [Code this Game](https://us.macmillan.com/books/9781250306692)  - Meg Ray

### [Invent with Python](https://inventwithpython.com/) -- Al Sweigart 

### [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/) - Al Sweigart

### [Python Trinket](https://trinket.io/python) -- Share Code from any Device

### [Opensource.com Raspberry Pi Cheat Sheet](https://opensource.com/downloads/getting-started-raspberry-pi-cheat-sheet)

### [Opensource.com Python 3.7 Cheat Sheet](https://opensource.com/downloads/cheat-sheet-python-37-beginners)

### [Python for Everyone](https://www.py4e.com/lessons) 

### [Making Games with Python](http://inventwithpython.com/pygame/) 

### [Simple Turtle Tutorial\(https://github.com/asweigart/simple-turtle-tutorial-for-python/blob/master/simple_turtle_tutorial.md)




