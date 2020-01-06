# First Python Lesson
The Python programming language was named after the Monty
Python’s Flying Circus TV show, not after python the snake.
According to [Python.org](https://python.org): "Python is a programming language that lets you work more quickly and integrate your systems more effectively."
### The Shell
Python commands are executed one line at a time. The action takes place in the Python shell. A typical Python shell looks like this. 
![Python Shell](https://github.com/donwatkins/PyGirls4Good/blob/master/Images/PythonShell1.png)

Here's a code example executed in the Python shell. 
![Hello Class](https://github.com/donwatkins/PyGirls4Good/blob/master/Images/PythonShell2.png)

### In this class we are going to use the Mu Editor which is designed for beginning programmers. 
The Mu Editor comes with the software included with your Raspberry Pi computer.

![Code with Mu](https://github.com/donwatkins/PyGirls4Good/blob/master/Images/CodeWithMu.png)

### We need to learn how to use our Mu Editor. Here is a great tutorial which will get us started on our Python Learning Journey. 
### [Code with Mu Tutorial](https://codewith.mu/en/tutorials/1.0/start)

____
### We can enter code in the REPL (Read, Evaluate, Print, Loop). The REPL is pictured below. 
![REPL](https://github.com/donwatkins/PyGirls4Good/blob/master/Images/Mu_REPL.png)


### At the REPL enter the following expressions
* 2 + 3
* 2 * 3 
* 3/5
* 2 **4
### What happened? 
----
### Order of operations
* '+' = Addition

* '-' = Subtraction

* '/' = Division

* '*' = Multiplication

* '**' = Exponent

* '//' = Integer division

* '%' = Modulus remainder
----
### You can also enter code one line at a time in the REPL. Here is our first program using the "print" function. 
![Hello World](https://github.com/donwatkins/PyGirls4Good/blob/master/Images/HelloWorld.png)

### Use the "print" function to enter your name in the REPL. Here is the sample code: 
```python
print("Your Name")
print("I go to Olean Middle School")
print("I like chocolate")
```
---
## Variables
 Variables play an important role in Python. They hold values that we assign to them. Some variables are "string' variables that contain strings of text. There are variables that contain integers. Those are numeric values like 1,2,100, etc. There also variables that contain floating point values like "1.5, 2.10, 3.15" etc. 
![Variables by Type](https://github.com/donwatkins/PyGirls4Good/blob/master/Images/variable_types.png)

Variables are like labels. We can add, subtract, multiply and divide variables that are type integer and float.We can add string variables to each other but we cannot subtract, multiply or divide them. Using the REPL, let's assign some variables and perform some mathematics with them. 
```python
pizzas = 10
cost_per_pizza = 4.00
total_cost = pizzas * cost_per_pizza
print(pizzas)
print(cost_per_pizza)
print(total_cost)
```
### Strings 
Strings are collection of letters and numbers. Your name could be string. Your address could be another string. Your age could be another string. We can use variables to represent a string. Foe example "your_name = "John"" , your_age = 12. Notice that strings with integers are not encloseed in quotations but text strings are. Enter these string examples in the REPL. 

* my_name = "your name"
* my_address = "your address" 
* my_age = 11 (whatever your age is) 

Once the variabele is assigned you can retrieve the value by entering the variable at the prompt or by using the 'print' function. Example: 
* print(my_name)
* print(my_age)





