import sys
sys.path.append('../lib')

# The * is importing everything in the file
from DEgraphics import *

#  MY SCREEN IS 3240 x 2160

# main constructor 
def main():

    win = DEGraphWin(defCoords = [-10,-10,-10,-10], 
                    title = "box 1", 
                    width = 200, height = 700,
                    offsets=[400,200],
                    hasTitlebar = False,
                    hThickness=1,)

    # sets background color of window
    win.setBackground(color_rgb(255,255,255))

    # second
    win2 = DEGraphWin(defCoords = [10,10,10,10], 
                    title = "box 2", 
                    width = 500, height = 700,
                    offsets=[600,200],
                    hasTitlebar = False,
                    hThickness=1,)

    # sets background color of window
    win2.setBackground(color_rgb(0,0,0))

    #third 
    win3 = DEGraphWin(defCoords = [10,10,10,10], 
                    title = "box 2", 
                    width = 700, height = 100,
                    offsets=[400,100],
                    hasTitlebar = False,
                    hThickness=1,)

    # sets background color of window
    win3.setBackground(color_rgb(50,50,50))

    win4 = DEGraphWin(defCoords = [10,10,10,10], 
                    title = "box 2", 
                    width = 700, height = 100,
                    offsets=[400,900],
                    hasTitlebar = False,
                    hThickness=1,)

    # sets background color of window
    win4.setBackground(color_rgb(160,160,160))


    
    
    clickPt = win4.getMouse() 
    win4.close()

    clickPt = win3.getMouse() 
    win3.close()

    clickPt = win2.getMouse() 
    win2.close()

    clickPt = win.getMouse() 
    win.close()
    


if __name__  == "__main__":
    main()