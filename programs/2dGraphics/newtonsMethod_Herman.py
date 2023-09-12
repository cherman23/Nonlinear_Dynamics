'''
    Newtons Method Explorer is 
    a program that allows the user 
    to input functions and view 
    fractals created from distance to roots 

    Author: Carter Herman 
        with DEGraphics, numpy, sympy 
'''

# need to import stuff from lib, namely 
# DE graphics 
import sys
sys.path.append('../lib')
from DEgraphics import * 

# import sympy to create equations and differentiate 
from sympy import sympify, diff, Symbol, lambdify, solveset

# import numpy for closest root function 
import numpy as np

# mac user screen size 
ScreenHorizontal = 1440
ScreenVertical = 900

# Global list for roots
global Roots
Roots = []

global r 
r = []

# set up global functions
global e
global eDiff


# fucntions uses newtons method
# to find routes given a starting integer and
# a given amount of iterations
def computeNewtons(x, counter):
    global Roots

    final = x

    iter = 0
    while iter <= counter:
        iter += 1
        final = final - (e(final) / eDiff(final))
    
    return final    

# CREATES FUNCTION AND SOLVES IT
# finds all the roots of the function 
#  using the newtons method function
def findAllRoots(strFunc):
    global Roots
    global e  
    global eDiff
    global r 
    r = []

    x = Symbol("x")
    # using sympy create equation objects 
    startingFunc = sympify(strFunc)

    # use lamdify to create a callable function
    e = lambdify(x, startingFunc)

    derivativeFunc = diff(startingFunc, x)

    # Find derivative 
    eDiff = lambdify(x, derivativeFunc)

    # USING SYMPY FIND ALL ROOTS
    Roots = solveset(startingFunc, x)

    # IT IS NECESSARY TO CAST ALL AS COMPLEX FOR LATER OPERATIONS
    for i in Roots:
        d = complex(i)
        r.append(d)

    r = np.asarray(r)

# given a point, it finds the closest root in Roots
def findClosestRoot(x):
    global r
    
    closestRoot = (np.abs(r - x)).argmin()

    # Return index of root
    return closestRoot


# Given a list of points and the color that corresponds to it 
# Then graphs that pixel that color 
def drawFractal(w, iter, colorBool = True):
    # lists of usable colors and list for once colors are calculated
    rootColorsOne = ['orange','green','purple','red','magenta','cyan']
    rootColorsTwo = ['black','grey','blue','gold', 'silver', 'white',]
    colorList = []

    if colorBool == True: rootColors = rootColorsOne
    else: rootColors = rootColorsTwo

    # calculations first to prevent calculation overflow
    max = 1000
    min = -1000
    add = 4

    x = min
    y = min
    # GOES THROUGH EVERY POINT FROM (-1000,-1000i) to (1000,1000i)
        # Use newtons method on this complex point as z
        # Then find the closest root to the newtons method returns 
        # Assign this root and point a color 
    while x <= max:
        while y <= max:
            if x != 0:
                z = computeNewtons(complex(x, y), iter)

                rootIndex = findClosestRoot(z)

                colorList.append(rootColors[rootIndex])

            y += add

        y = min
        x += add

    fill(w, colorList)

def fill(w, colorList):
    
    # THESE POINTS GO FROM TOP LEFT DOWN TO BOTTOM RIGHT 
        # IT GOES DOWN THE COLUMN FIRST THEN ACROSS THE ROW  
        # THE PLOT FUNCTION USES DEF COORDS NOT PIXELS IN THING
    x2 = -1
    y2 = -1
    i = 0

    while x2 <= 1:
        while y2 <= 1:
            if i < 250000: # this line exists so the list doesnt overflow 
                w.plot(x2,y2, colorList[i])

            y2 += 0.004
            i+=1
        
        x2 += 0.004
        y2 = -1

        w.update()
        i += 1
    

def main():
    instructWin = False

    # CREATE WINDOWS
    newtonWin = DEGraphWin(defCoords = [-1,-1,1,1], 
                    title ="newtonsWindow", 
                    width = 500, height = 500,
                    offsets=[ScreenHorizontal/3,ScreenVertical/8],
                    hasTitlebar = False,
                    hThickness=0,)

    controlWin = DEGraphWin(defCoords = [-10,-10,10,10], 
                    title ="Newtons Fractal Controls", 
                    width = 500, height = 300,
                    offsets=[ScreenHorizontal/3,ScreenVertical/8+500],
                    hasTitlebar = True,
                    hThickness=0,)
    controlWin.setBackground(color_rgb(211,211,211))


    # CREATE BUTTONS
    btnGraph = Button(controlWin, Point(-7.5,2), width=7, height=2,
                edgeWidth = 2, label = 'Draw Newton Fractal',
                buttonColors = ['lightgray', 'black', 'black'],
                clickedColors = ['white', 'red', 'black'],
                font=('courier',11), timeDelay = 0.25)
    btnGraph.activate()

    btnClear = Button(controlWin, Point(-7.5,-3), width=7, height=2,
                edgeWidth = 2, label = 'Clear Fractal',
                buttonColors = ['lightgray', 'black', 'black'],
                clickedColors = ['white', 'red', 'black'],
                font=('courier',11), timeDelay = 0.25)
    btnClear.activate()

    btnZoomIn = Button(controlWin, Point(1,-1), width=7, height=2,
                edgeWidth = 2, label = 'Zoom In',
                buttonColors = ['lightgray', 'black', 'black'],
                clickedColors = ['white', 'red', 'black'],
                font=('courier',11), timeDelay = 0.25)
    btnZoomIn.activate()

    btnZoomOut = Button(controlWin, Point(1,-4.5), width=7, height=2,
                edgeWidth = 2, label = 'Zoom Out',
                buttonColors = ['lightgray', 'black', 'black'],
                clickedColors = ['white', 'red', 'black'],
                font=('courier',11), timeDelay = 0.25)
    btnZoomOut.activate()

    btnInstruction = Button(controlWin, Point(-7.5,-7.5), width=7, height=2,
                edgeWidth = 2, label = 'Instructions',
                buttonColors = ['lightgray', 'black', 'black'],
                clickedColors = ['white', 'red', 'black'],
                font=('courier',11), timeDelay = 0.25)
    btnInstruction.activate()

    btnQuit = Button(controlWin, Point(1,-7.5), width=7, height=2,
                edgeWidth = 2, label = 'Quit',
                buttonColors = ['darkred', 'black', 'black'],
                clickedColors = ['white', 'red', 'black'],
                font=('courier',11), timeDelay = 0.25)
    btnQuit.activate()


    # CREATE INPUTS 
    functionInput = Entry(Point(-4.5, 4.5), 15)
    functionInput.setSize(11)
    functionInput.setText("x**4-1")
    functionInput.draw(controlWin)

    iterInput = Entry(Point(4.5, 4.5), 15)
    iterInput.setSize(11)
    iterInput.setText("50")
    iterInput.draw(controlWin)

    colorInput = Entry(Point(4.5,1), 15)
    colorInput.setSize(11)
    colorInput.setText("light")
    colorInput.draw(controlWin)

    #CREATE TEXT
    instructText = Text(Point(-4.5, 7), "Enter Function Here:")
    instructText.draw(controlWin)

    interText = Text(Point(4.5, 7), "Enter Iteration Amount Here:")
    interText.draw(controlWin)

    colorText = Text(Point(4.5, 2.5), "Enter color here (light or dark):")
    colorText.draw(controlWin)

    # ACTIVATE BUTTONS 
    clickPt = controlWin.getMouse()
    while not btnQuit.clicked(clickPt):
        if btnGraph.clicked(clickPt):
            # Create functions with the given input function
            # after calling it sets up the e and ediff functions to call
            # use newtons method to find the rooots of given function
            findAllRoots(functionInput.getText())

            colorBool = True
            if colorInput.getText() == 'light': colorBool = True
            elif colorInput.getText() == 'dark': colorBool = False

            # once roots are found, draw fractal
            drawFractal(newtonWin, int(iterInput.getText()), colorBool)

        elif btnZoomIn.clicked(clickPt):
            newtonWin.zoom(whichWay = ZOOM_IN, keepRatio = True)
            # make sure to check for correct colors when redrawing
            colorBool = True
            if colorInput.getText() == 'light': colorBool = True
            elif colorInput.getText() == 'dark': colorBool = False
            drawFractal(newtonWin, int(iterInput.getText()), colorBool)

        elif btnZoomOut.clicked(clickPt):
            newtonWin.zoom(whichWay = ZOOM_OUT, keepRatio = True)
            # make sure to check for correct colors when redrawing

            colorBool = True
            if colorInput.getText() == 'light': colorBool = True
            elif colorInput.getText() == 'dark': colorBool = False

            drawFractal(newtonWin, int(iterInput.getText()), colorBool)

        elif btnClear.clicked(clickPt):
            # Clears the points
            newtonWin.clear()

        elif btnInstruction.clicked(clickPt):
            if instructWin == True:
                # window can be closed to declutter space 
                instructionWin.close()
                instructWin = False
                btnInstruction.setCaption('Instructions')
            else:

                #EVERYTHING HAS TO BE REDRAWN EVERY TIME IT IS OPENED AND CLOSED
                instructionWin = DEGraphWin(defCoords = [-10,-10,10,10], 
                        title ="Instructions", 
                        width = 500, height = 250,
                        offsets=[ScreenHorizontal/3+500,ScreenVertical/8+500],
                        hasTitlebar = True,
                        hThickness=0,)
                controlWin.setBackground(color_rgb(211,211,211))

                textRoots = Text(Point(0,9), "Type a function into the enter bar (using ** notation for exponents up to 6)")
                textRoots.setSize(10)
                textRoots.setStyle('bold')
                textRoots.draw(instructionWin)
                textRoots.setTextColor("black")

                textRoots = Text(Point(0,7), "- Then select a number of iterations for newtons method")
                textRoots.setSize(10)
                textRoots.setStyle('bold')
                textRoots.draw(instructionWin)
                textRoots.setTextColor("black")

                textRoots = Text(Point(0,5), " - The higher number of iterations increases")
                textRoots.setSize(10)
                textRoots.setStyle('bold')
                textRoots.draw(instructionWin)
                textRoots.setTextColor("black")
                textRoots = Text(Point(0,3.5), "  the accuracy for the root each point is closest to")
                textRoots.setSize(10)
                textRoots.setStyle('bold')
                textRoots.draw(instructionWin)
                textRoots.setTextColor("black")

                textRoots = Text(Point(0,0), "Use Draw and Clear buttons to create the fractal (it may take some time)")
                textRoots.setSize(10)
                textRoots.setStyle('bold')
                textRoots.draw(instructionWin)
                textRoots.setTextColor("darkblue")

                textRoots = Text(Point(0,-2.5), "Use the zoom buttons to view sections of the graph")
                textRoots.setSize(10)
                textRoots.setStyle('bold')
                textRoots.draw(instructionWin)
                textRoots.setTextColor("darkblue")

                textRoots = Text(Point(0,-5), "- (for zoom in click two points on graph)")
                textRoots.setSize(10)
                textRoots.setStyle('bold')
                textRoots.draw(instructionWin)
                textRoots.setTextColor("darkblue")

                textRoots = Text(Point(0,-7.5), "- (it will take time to redraw fractal after zooming)")
                textRoots.setSize(10)
                textRoots.setStyle('bold')
                textRoots.draw(instructionWin)
                textRoots.setTextColor("darkblue")

                textRoots = Text(Point(0,-9), "Choose between the two color schemes by typing 'light' or 'dark'")
                textRoots.setSize(10)
                textRoots.setStyle('bold')
                textRoots.draw(instructionWin)
                textRoots.setTextColor("darkblue")

                # CHANGES THE VARIABLES 
                btnInstruction.setCaption('Close Instructions')
                instructWin = True


        # retrieve click point to prevent infinite interation
        clickPt = controlWin.getMouse()


    newtonWin.close()
    controlWin.close()

main()