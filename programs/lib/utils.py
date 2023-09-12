import math
from DEgraphics import *

def quadFunc(A, B, C):
    root1 = 0
    root2 = 0
    discriminant = (B*B) - (4*A*C)

    # CALCULATING ROOTS
    if discriminant > 0:
        num = math.sqrt(discriminant)
        root1 = ((0-B) - num)/(2*A)
        root2 = ((0-B) + num)/(2*A)
        strResult = "Roots",":","(", str(round(root1,3)), ",0)", ",", "(",str(round(root2,3)),  ",0)"
        return strResult

    # NO POSSIBLE 
    elif discriminant < 0:
        return "Roots: None"
    else:
        root1 = -B/(2*A) 
        strResult = "Root",":","(", str(round(root1,3)), ",0)"
        return strResult

def quadFuncCircles(A, B, C):
    root1 = 0
    root2 = 0
    discriminant = (B*B) - (4*A*C)
    CircleList = []

    # CALCULATING ROOTS
    if discriminant > 0:
        num = math.sqrt(discriminant)
        root1 = ((0-B) - num)/(2*A)
        root2 = ((0-B) + num)/(2*A)
        circle1 = Circle(Point(root1, 0), 0.5)
        
        circle2 = Circle(Point(root2, 0), 0.5)
        CircleList.append(circle1)
        CircleList.append(circle2)
        

    # NO POSSIBLE 
    elif discriminant < 0:
        pass
    else:
        root1 = -B/(2*A) 
        circle1 = Circle(Point(root1, 0), 0.5)

        CircleList.append(circle1)

    return CircleList