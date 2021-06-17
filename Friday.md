### Create a new poem using 'turtle.textinput'

```
# Turtle Poem
import turtle as t
import time

# input lines of poem
first_line = t.textinput("First Line of the poem", "enter the line here")
time.sleep(5)
second_line = t.textinput("Second Line of the poem", "enter the line here")
time.sleep(5)
third_line = t.textinput("Third Line of the poem", "enter the line here")
time.sleep(5)

# print the poem here
print("Here is your poem!!")
print("\n")

print(first_line)
print("\n")
print(second_line)
print("\n")
print(third_line)
print("\n")
---

```
import turtle as t
t.color('deep pink')
style = ('Courier', 36, 'italic')
t.write('Hello Olean 1', font=style, align ='center')
t.hideturtle()

---
