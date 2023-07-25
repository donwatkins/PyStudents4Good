#Ice Cream Store

import time

cost = eval(input("What is the price per scoop?"))
number_of_scoops = eval(input("How many scoops of ice cream do you want?"))

final_price = (cost * number_of_scoops)
time.sleep(2)

print("Your ice cream will cost.")
time.sleep(1)

print('$',final_price)
