#!/usr/bin/env python3

# Interview questions with if statements

name = input("What is your name?")

print("Hello " + name)

age = input("What is your age? ")

if int(age) <= 5:
	print("You are very young!")

elif int(age) <= 18:
	print("You might be a teenager and too young to vote.")

elif int(age) >=30:
	print("You are an adult!")

else:
	print("Thank you.")
