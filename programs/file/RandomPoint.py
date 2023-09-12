import sys
sys.path.append('../lib')
from DEgraphics_Herman import *
from math import *
import random 

ScreenHorizontal = 1440
ScreenVertical = 900

def main():
    win = DEGraphWin(defCoords = [-1,-1,1,1], 
                    title ="Main", 
                    width = 500, height = 500,
                    offsets=[ScreenHorizontal/4,ScreenVertical/8],
                    hasTitlebar = False,
                    hThickness=1,)
    
    firstClick = win.getMouse()
    secondClick = win.getMouse()
    thirdClick = win.getMouse()
    
    pointList = [Point(firstClick.getX(),firstClick.getY()), Point(secondClick.getX(),secondClick.getY()), Point(thirdClick.getX(),thirdClick.getY())]
    colorList = ['red', 'green', 'blue']

    n = Point(random.uniform(-1,1), random.uniform(-1,1))

    for i in range(100000):
        
        numChoice = random.randrange(0,3)

        choice = pointList[numChoice]

        halfWay = Point(((n.getX()+choice.getX())/2), ((n.getY()+choice.getY())/2))

        n = halfWay

        win.plot(halfWay.getX(), halfWay.getY(), colorList[numChoice])

    clickPt = win.getMouse()
    while not win.clicked(clickPt):
        clickPt = win.getMouse()

    win.close()

main()