# need to import stuff from lib, namely 
# DE graphics 
import sys
sys.path.append('../lib')
from DEgraphics import *

def fill(w, precision = 1, numSweeps = 4):
    xmin = w.currentCoords[0]
    xmax = w.currentCoords[2]

    ymin = w.currentCoords[1]
    ymax = w.currentCoords[3]

    h_step = (xmax - xmin)/w.width
    v_step = (ymax - ymin)/w.height


    for sweep in range(numSweeps):
        x = xmin + sweep
        while x < xmax:
            y = ymin
            while y < ymax:
                if y < x**2:
                    w.plot(x,y, 'blue')
                    y += v_step
                else:
                    w.plot(x,y, 'red')
                    y += v_step
            x += precision * h_step
            w.update()

def main():
    win = DEGraphWin(defCoords= [-10,-10,10,10],
                        title = "2dgraphics", 
                        width=1000, height=1000,
                        offsets=[200, 100],
                        hasTitlebar = True, autoflush= False,
                        hThickness=1,)

    win.getMouse()
    fill(win, 9)
    win.close()


main()