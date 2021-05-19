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
