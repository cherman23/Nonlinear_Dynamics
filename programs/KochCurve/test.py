from time import *
from math import *

def cpuSpeed():

    startime = time()
    for i in range(10000):
        sqrt(i)
    endtime = time()

    ttime= endtime-startime

    return ttime

print(cpuSpeed())




def drawColor(w, startPt, vertex, endPT, level):
    pass
    # TAKES THREE POINTS 
    triangle = Polygon(startPt, vertex, endPT)
    # DRAWS A POLYGON OF A COLOR DEPENDING ON LEVEL
    triangle.setFill(colors[level])
    triangle.draw(w)


def color_KC(w, start, theta, inclineAngle, length, level):
    # START WITH THE END POINTS OF LINES 
    if level == 0:
        len = length * 1/3
        
        # NEEDS TO BE COMPLETED 
     
    # RECURSIVELY GO THROUGH THOSE TWO POINTS AND REPEAT X AMOUNT OF TIMES 
    else:
        start = Point(start.getX() + length * 1/3,start.getY() + length * 1/3)
        length *= 1/3
        level -= 1
        color_KC(w, start, theta, inclineAngle, length, level)
        color_KC(w, start, theta, inclineAngle+theta, length, level)
        color_KC(w, start, theta, inclineAngle-theta, length, level)
        color_KC(w, start, theta, inclineAngle, length, level)
