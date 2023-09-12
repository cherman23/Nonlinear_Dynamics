# need to import stuff from lib, namely 
# DE graphics 
import sys
sys.path.append('../lib')

# The * is importing everything in the file
from DEgraphics import *

# main method to run etire program 
def main(): 
    # Create DEGraphWin

    win = DEGraphWin(defCoords = [-10,-10,10,10], 
                    title ="fun with graphics", 
                    width = 800, height = 800,
                    offsets=[500,50],
                    hasTitlebar = False,
                    hThickness=1,)

    # sets background color of window
    win.setBackground(color_rgb(125,125,125))

    # create a button to shutdown the program 
    btnQuit = Button(win, Point(0,0), width=5, height=2,
                edgeWidth = 2, label = 'button captain',
                buttonColors = ['lightgray', 'black', 'black'],
                clickedColors = ['white', 'red', 'black'],
                font=('courier',18), timeDelay = 0.25)
    btnQuit.activate()

    for i in range(255):
        win.setBackground(color_rgb(i,i,i))
        time.sleep(0.5)

    clickPt = win.getMouse() # Waits for mouse click to close window
    
    # have to click on button to close window 
    while not btnQuit.clicked(clickPt):
        clickPt = win.getMouse()

    win.close()

if __name__  == "__main__":
    main()