# This program will yield the hypoteneuse when 2 sides are known
import math
Side_a = input("What is the length of the first side? ")
Side_b = input("What is the length of the second side? ")

Side_aSquare = int(Side_a) **2
Side_bSquare = int(Side_b) **2
# Square each side
Side_C = (Side_aSquare) + (Side_bSquare)


print("The Answer is... ")
print(math.sqrt(Side_C))
