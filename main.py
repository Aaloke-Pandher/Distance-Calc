# Python Distance-Calc 

# Import math module
import math

# Input 
x1 = float(input("Enter the x-cordinate of the first point:"))
y1 = float(input("Enter the y-cordinate of the first point:"))
x2 = float(input("Enter the x-cordinate of the second point:")) 
y2 = float(input("Enter the y-cordinate of the second point:"))

# Process 
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Output
print("The distance between the points " + str(distance))