import math

x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

dx = x2 - x1
dy = y2 - y1

distance = math.sqrt(math.pow(dx, 2) + math.pow(dy, 2))
dist = round(distance , 2)
print("The distance between the two points is:", dist)