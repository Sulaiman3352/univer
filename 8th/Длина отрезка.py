import math
print (distace ( x1, y1, x2, y2 ))
def distance(x1, y1, x2, y2):
    dx = x1 - x2
    dy = y1 - y2
    return math.sqrt(dx ** 2 + dy ** 2)

 x1, y1 = int(input()), int(input())
 x2, y2 = int(input()), int(input())
