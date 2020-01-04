# Strings, lists and the turtle
Lists are more powerful than strings. Lists are enclosed in brackets []. A list might contain all the students in this class. [
* class_list = ["Kathy", "Marla", "Margaret"]
* colors = ["red", "blue", "orange"]
### We can add to a list.
*Use the 'class_list.append() command. 
![List append](https://github.com/donwatkins/PyGirls4Good/blob/master/Images/AddToList.png)

## Your first program
Entering code in the REPL can give us immediate feedback but we need to write the code down and save it. Our first program will be to say "Hello World." After entering the code we want to click on the 'Save' button at the top of Mu. 
![Hello World](https://github.com/donwatkins/PyGirls4Good/blob/master/Images/MyFirstProgram.png)
### After clicking on the 'Save' button you will see a dialog box and you will be given the opportunity to save your file. A good name might be 'first.py.' When saving Python programs be sure to end with the file extension '.py'. 
![Save my first program](https://github.com/donwatkins/PyGirls4Good/blob/master/Images/SaveMyFirstProgram.png)
### After saving the program then click on the 'Run' button to see the output of your program. 

## Turtle function
There are many functions in Python. We have already used the 'print' function. Now we are going to use the 'turtle' function. We have to import it first. We do that by entering 'import turtle' in the REPL. 
![import turtle](https://github.com/donwatkins/PyGirls4Good/blob/master/Images/import_turtle.png)
### Notice that we can tell the turtle to move forward with the 'turtle.forward(100)' command. You will see this 'dot' notation more and more in our exploration of Python. Let's draw a square. Enter these commands:
```python
import turtle
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
```

### Now we want to write our first program using the the 'turtle' function and save it.  We begin by clicking on the 'New' button in Mu. Then we enter "import turtle.' Add a comment at the top of your file. What are the next lines of code? Be sure to 'Save' and then 'Run' your program. 
![First Turtle](https://github.com/donwatkins/PyGirls4Good/blob/master/Images/FirstTurtleProgram.png)
---
### Here's a way we can do more with less code using the 'for' loop and specify a 'range'. 
![Turtle For Loop](https://github.com/donwatkins/PyGirls4Good/blob/master/Images/TurtleForLoop.png)
### Note what changed. We imported 'turtle' by specified it as a variable 't'. Then we used a 'for' loop together with the 'range' function to eliminate some of code and we still finished with a nice square. Be sure to do this yourself and save your work. 

### Let's have some more fun and generate something more exciting than a square. Change the 'range' value to 100 and the turn angle to 91. What happened? 

Another iteration: 
```python
import turtle as t
for x in range(100):
  t.forward(x)
  t.left(91)
  ```
### What happened? 







