# Fun with the Turtle and other Python functions

### In the last lesson we learned how to use the 'turtle' function to draw a square, a spiral, and differently colored spirals. 
Now we are going to learn more. In an earlier lesson we learned that we can create variables that are made up of a list of objects. Now we are going to create a list of colors that we are going to use to create a four color spiral. Remember a list is contained in [] brackets. Here is our plan

1. Import the turtle module and set up a turtle
2. Tell the computer which colors we are going to use. 
3. Setup a loop to draw 150 lines in our spiral
4. Pick a different pen color for each side of the spiral.
5. Move the turtle forward to draw each line.
6. Turn the turtle to get it ready to draw the next line. 

```python
colors = ["red", "yellow", "blue", "green"]

```
### Here is our code:
```python
import turtle as t
colors = ["red", "yellow", "blue", "green"]
for x in range(100):
  t.pencolor(colors[x%4])
  t.forward(x)
  t.left(91)
  ```
  
### We want to make the colors really stand out so we are going to change the backgroud color to black. 
We do that by using the 'bgcolor' method. Our code will look like this. 
```python
import turtle as t
t.bgcolor("black")
colors = ["red", "yellow", "blue", "green"]
for x in range(100):
  t.pencolor(colors[x%4])
  t.forward(x)
  t.left(91)
  ```
### We can change from a square spiral to a circle spiral by using a new iteration. 
```python
import turtle as t
t.bgcolor("black")
colors = ["red", "yellow", "blue", "green"]
for x in range(100):
  t.pencolor(colors[x%4])
  t.circle(x)
  t.left(91)
  ```
  

