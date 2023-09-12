# need to import stuff from lib, namely 
# DE graphics 
import sys
sys.path.append('../lib')
from DEgraphics_Herman import *
import random


# global because used in graphing and clearing 
global graphPoints
global cobwebLines
global seriespoints
cobwebLines = []
graphPoints = []
seriespoints = []

# mac display size 
ScreenHorizontal = 1440
ScreenVertical = 900


''' 
    Logistic Map Explorer:

    Creates a cobweb diagram
    and allows user to input 
    variables to edit the map. 
    Allows for understand of how
    bifurcation of the map works.
    
    Author: Carter Herman
        *with usage of DEGraphics
'''



def clear():
    # undraw from the time series window and the cobweb diagram 
    for i in graphPoints:
        i.undraw()
    for i in cobwebLines:
        i.undraw()
    for i in seriespoints:
        i.undraw()

def zoomIn(graphwin, transient):
    graphwin.zoom(whichWay = ZOOM_IN, keepRatio = True)
    drawBifurcation(graphwin, transient)

def zoomOut(graphwin, transient):
    graphwin.zoom(whichWay = ZOOM_OUT, keepRatio = True)
    drawBifurcation(graphwin, transient)

def drawSteadyState(graphwin):
    # Steady state line is y = x so only one 45 degree line is needed
    steadyStateLine = Line(Point(0, 0), Point(2, 2))
    steadyStateLine.setFill(color_rgb(225,0,0))
    steadyStateLine.draw(graphwin)

def drawGraph(r ,graphwin, x, iterations):
    # This function combines cobweb and logistic map function

    i = 0
    while i < 1:
        # DRAWS LOGISTIC MAP
        # from given r value
        y = (r*i)*(1-i)
        logiPoint = Point(i, y)
        graphPoints.append(logiPoint)
        logiPoint.draw(graphwin)

        i+=0.0001
    
    # Graphs cobweb because it aligns with the values
    drawCobweb(graphwin, Point(x, 0), r, 0, True, iterations)


def drawCobweb(graphwin, pt1, r, counter, lineBool, iterations):
    # number of lines in cobweb diagram
    # Basically it needs to draw a line from the point to the logistic map
        # this can be done by plugging it into the logisticmap function 
    # Then it needs to draw a horizontal line from there to the y = x line 


    # uses recursion to start from the next point that is left off
    if counter <= iterations:

        # Vertical lines 
        if lineBool == True:
            # plug the x and r in logistic map function for the y valyes 
            y = pt1.getX()*r*(1 - pt1.getX())

            # The point is going to have the same x val because it is a vertical line 
            pt2 = Point(pt1.getX(), y)

            # Creating the line from the two points
            vertLine = Line(pt1, pt2)

            # color is different for visibility 
            vertLine.setFill(color_rgb(0,0,150))

            # Add to list so it can be cleared later
            cobwebLines.append(vertLine)
            vertLine.draw(graphwin)

            # CHANGES VARIABLES SO HORIZONTAL LINE IS DRAWN NEXT
            lineBool = False
            counter+=1
            drawCobweb(graphwin, pt2, r, counter, lineBool, iterations)

        # horizontal lines
        else:
            # point will have the same y because it is a horizontal line
                # it has to be on the y = x line
                # so both points are the same 
            pt2 = Point(pt1.getY(), pt1.getY())

            # draw line from given point to created point
            horizLine = Line(pt1, pt2)
            horizLine.setFill(color_rgb(0,150,0))

            # added to list so it can be cleared later
            cobwebLines.append(horizLine)
            horizLine.draw(graphwin)

            lineBool = True
            counter+=1
            drawCobweb(graphwin, pt2, r, counter, lineBool, iterations)
    
    # Stop after amount of given iterations
    else:
        pass


def drawBifurcation(graphwin, transient):
    Rval = 0

    # R can only be between  and 4 

    while Rval <= 4:
        # Start from random x value 
        x = random.uniform(0, 1)
        for i in range(transient):
            # iterate the transient amount of times before plotting
            x = Rval*x*(1-x)
        graphwin.plot(Rval,x)
        Rval+=0.0004


def drawTimeSeries(graphwin, x, r, iterations, counter):
    # only put in the user input amount of iterations
    if counter < iterations:
        # Find value in the logistic map
        y = x*r*(1-x)
        seriesPoint = Point(counter, y)
        seriesPoint.draw(graphwin)
        seriespoints.append(seriesPoint)

        counter+=1
        # Compositing of the function through recursion
        drawTimeSeries(graphwin, y, r, iterations, counter)
    else: pass


# GIVEN a window it labels the axes 
def drawAxes(graphwin):
    graphwin.toggleAxes()
    numlist = [0.5,1,1.5,2,2.5,3,3.5]
    

    for i in numlist:
        if i != 0:
            iText = str(i)
            # X Axis labels
            titleText = Text(Point(i, 0.05),iText)
            titleText.setTextColor('red')
            titleText.setSize(8)
            titleText.draw(graphwin)

            # Y Axis lables
            titleText = Text(Point(0.08, i),iText)
            titleText.setTextColor('red')
            titleText.setSize(8)
            titleText.draw(graphwin)
    # SETS GRAPH AXES
    for j in numlist:
        if j != 0:
            # dashes for x axis
            dashX = Line(Point(j,0.03),Point(j,-0.03), style='solid')
            dashX.draw(graphwin)

            # dashes for y axis
            dashY = Line(Point(0.03,j),Point(-0.03,j), style='solid')
            dashY.draw(graphwin)
        




'''
    The main function creates the graphwin interactable
    objects. This includes windows and buttons. 
    It then uses the other functions within the 
    program to interact with maps. 
'''
def main():
    
    # WINDOWS
    winTitle = DEGraphWin(defCoords= [-10,-10,10,10],
                        title = "Graph", 
                        width=1000, height=25,
                        offsets=[ScreenHorizontal/16 + 200, ScreenVertical/4-25],
                        hasTitlebar = False,
                        hThickness=1,)

    # This window will show the graph of the function
    winGraph = DEGraphWin(defCoords= [-0.125,-0.125,1.2,1.2],
                        title = "Graph", 
                        width=500, height=500,
                        offsets=[ScreenHorizontal/16 + 700, ScreenVertical/4],
                        hasTitlebar = False,
                        hThickness=1,)

    winBifurcation = DEGraphWin(defCoords= [-0.125,-0.125,4,1.5],
                        title = "Graph", 
                        width=500, height=250,
                        offsets=[ScreenHorizontal/16 + 200, ScreenVertical/4],
                        hasTitlebar = False,
                        hThickness=1,)

    winTimeSeries = DEGraphWin(defCoords= [-0.125,-0.125,1.2,1.2],
                        title = "Graph", 
                        width=500, height=250,
                        offsets=[ScreenHorizontal/16 + 200, ScreenVertical/4 + 250],
                        hasTitlebar = False,
                        hThickness=1,)


    winControlPanel = DEGraphWin(defCoords= [-10,-10,10,10],
                        title = "Graph", 
                        width=200, height=685,
                        offsets=[ScreenHorizontal/16 + 1200, ScreenVertical/4-25],
                        hasTitlebar = True,
                        hThickness=1,)

    winInstructions = DEGraphWin(defCoords= [-10,-10,10,10],
                        title = "Instructions", 
                        width=1000, height=200,
                        offsets=[ScreenHorizontal/16+200, ScreenVertical/4+500],
                        hasTitlebar = False,
                        hThickness=1,)
    winInstructions.setBackground((color_rgb(211,211,211)))


    # LABELING GRAPHS AND DRAWINGN STEADY STATE
    drawAxes(winBifurcation)
    drawAxes(winGraph)
    drawSteadyState(winGraph)
    drawBifurcation(winBifurcation, 100)
    


    # BUTTONS
        # Contains: 
            # graphing cobweb
            # clearing cobweb
            # get r from bifurcation 
            # zooming bifurcation
    btnGraph = Button(winControlPanel, Point(-4.5,2.5), width=11, height=1,
                edgeWidth = 2, label = 'Graph Cobweb',
                buttonColors = ['lightgray', 'black', 'black'],
                clickedColors = ['white', 'red', 'black'],
                font=('courier',11), timeDelay = 0.25)
    btnGraph.activate()

    btnClear = Button(winControlPanel, Point(-4.5,1), width=11, height=1,
                edgeWidth = 2, label = 'Clear Cobweb',
                buttonColors = ['lightgray', 'black', 'black'],
                clickedColors = ['white', 'red', 'black'],
                font=('courier',11), timeDelay = 0.25)
    btnClear.activate()

    btnBifurcation = Button(winControlPanel, Point(-4.5,-3), width=11, height=1,
                edgeWidth = 2, label = 'Bifurcation',
                buttonColors = ['lightgray', 'black', 'black'],
                clickedColors = ['white', 'red', 'black'],
                font=('courier',11), timeDelay = 0.25)
    btnBifurcation.activate()

    btnGetR = Button(winControlPanel, Point(-4.5,-4.5), width=11, height=1,
                edgeWidth = 2, label = 'Get R Val',
                buttonColors = ['lightgray', 'black', 'black'],
                clickedColors = ['white', 'red', 'black'],
                font=('courier',11), timeDelay = 0.25)
    btnGetR.activate()

    btnZoomIn = Button(winControlPanel, Point(-4.5,-6), width=11, height=1,
                edgeWidth = 2, label = 'Zoom In',
                buttonColors = ['lightgray', 'black', 'black'],
                clickedColors = ['white', 'red', 'black'],
                font=('courier',11), timeDelay = 0.25)
    btnZoomIn.activate()

    btnZoomOut = Button(winControlPanel, Point(-4.5,-7.5), width=11, height=1,
                edgeWidth = 2, label = 'Zoom Out',
                buttonColors = ['lightgray', 'black', 'black'],
                clickedColors = ['white', 'red', 'black'],
                font=('courier',11), timeDelay = 0.25)
    btnZoomOut.activate()

    btnQuit = Button(winControlPanel, Point(-4.5,-9), width=11, height=1,
                edgeWidth = 2, label = 'Quit',
                buttonColors = ['darkred', 'black', 'black'],
                clickedColors = ['white', 'red', 'black'],
                font=('courier',11), timeDelay = 0.25)
    btnQuit.activate()



    # ENTRY FOR R
    entryR = DblEntry(Point(5, 3.5), 5, span = [0,4],
                colors = ['gray','black'],
                errorColors = ['red','white'])
    entryR.setDefault(1)
    entryR.draw(winControlPanel)

    # Starting value for cobweb diagram
    entryX = DblEntry(Point(5, 5.5), 5, span = [0,1],
                colors = ['gray','black'],
                errorColors = ['red','white'])
    entryX.setDefault(1)
    entryX.draw(winControlPanel)

    # Entry for number of iterations of cobweb
    entryIteration = IntEntry(Point(5, 7.5), 5, span = [0,100],
                colors = ['gray','black'],
                errorColors = ['red','white'])
    entryIteration.setDefault(1)
    entryIteration.draw(winControlPanel)

    # Entry for number of iterations of cobweb
    entryTransientIteration = IntEntry(Point(5, -2.25), 5, span = [0,1000],
                colors = ['gray','black'],
                errorColors = ['red','white'])
    entryTransientIteration.setDefault(100)
    entryTransientIteration.setText(100)
    entryTransientIteration.draw(winControlPanel)

    

    # LABELS FOR ENTRY OBJECTS / TITLE WINDOW
        # SHOWS ALLOWED RANGES
        # TITLES THAT SEPARATE BIFDURCATION AND COBWEB BUTTONS
    textRoots = Text(Point(0,9), "Cobweb Manipulation")
    textRoots.setSize(12)
    textRoots.setStyle('bold')
    textRoots.draw(winControlPanel)
    textRoots.setTextColor("black")

    textRoots = Text(Point(0,-1), "Bifurcation Manipulation")
    textRoots.setSize(12)
    textRoots.setStyle('bold')
    textRoots.draw(winControlPanel)
    textRoots.setTextColor("black")

    textRoots = Text(Point(-4,7.5), "Iterations [0,100]: ")
    textRoots.setSize(10)
    textRoots.setStyle('bold')
    textRoots.draw(winControlPanel)
    textRoots.setTextColor("black")

    textRoots = Text(Point(-4,5.5), "X Value [0,1]: ")
    textRoots.setSize(10)
    textRoots.setStyle('bold')
    textRoots.draw(winControlPanel)
    textRoots.setTextColor("black")

    textRoots = Text(Point(-4,3.5), "R Value [0,4]: ")
    textRoots.setSize(10)
    textRoots.setStyle('bold')
    textRoots.draw(winControlPanel)
    textRoots.setTextColor("black")

    textRoots = Text(Point(-3.7,-2.25), "Transient [0,1000]: ")
    textRoots.setSize(10)
    textRoots.setStyle('bold')
    textRoots.draw(winControlPanel)
    textRoots.setTextColor("black")



    # instructions on how to use buttons
    textRoots = Text(Point(-8.5,9), "Instructions: ")
    textRoots.setSize(14)
    textRoots.setStyle('bold')
    textRoots.draw(winInstructions)
    textRoots.setTextColor("black")

    textRoots = Text(Point(-2.3,7), "- The bifurcation diagram is used to model population and the cobweb diagram shows iterations of given function")
    textRoots.setSize(10)
    textRoots.setStyle('bold')
    textRoots.draw(winInstructions)
    textRoots.setTextColor("black")

    textRoots = Text(Point(-2.9,5), " - Iterations can be any integer between 1 and 100, it controls the iterations in the cobweb and time series")
    textRoots.setSize(10)
    textRoots.setStyle('bold')
    textRoots.draw(winInstructions)
    textRoots.setTextColor("black")

    textRoots = Text(Point(-4,3), " - R is an input for the cobweb diagram that can be any floating point between 0 and 4")
    textRoots.setSize(10)
    textRoots.setStyle('bold')
    textRoots.draw(winInstructions)
    textRoots.setTextColor("black")

    textRoots = Text(Point(-4,1), " - X is an input for the cobweb diagram that can be any floating point between 0 and 1")
    textRoots.setSize(10)
    textRoots.setStyle('bold')
    textRoots.draw(winInstructions)
    textRoots.setTextColor("black")

    textRoots = Text(Point(-3.5,-1), " - Graph button graphs the function and timeseries with given input and clear button clears it")
    textRoots.setSize(10)
    textRoots.setStyle('bold')
    textRoots.draw(winInstructions)
    textRoots.setTextColor("black")

    textRoots = Text(Point(-4,-3), " - Transient is the number of iterations skipped in the bifurcation diagram from 1 to 1000")
    textRoots.setSize(10)
    textRoots.setStyle('bold')
    textRoots.draw(winInstructions)
    textRoots.setTextColor("black")

    textRoots = Text(Point(-4.1,-5), " - Get R button gets the R value from the bifurcation diagram and sets them as inputs")
    textRoots.setSize(10)
    textRoots.setStyle('bold')
    textRoots.draw(winInstructions)
    textRoots.setTextColor("black")

    textRoots = Text(Point(-5.1,-7), " - Zooming buttons allow are for zooming on bifurcation diagram only")
    textRoots.setSize(10)
    textRoots.setStyle('bold')
    textRoots.draw(winInstructions)
    textRoots.setTextColor("black")

    textRoots = Text(Point(-7.7,-9), " - Quit button closes program")
    textRoots.setSize(10)
    textRoots.setStyle('bold')
    textRoots.draw(winInstructions)
    textRoots.setTextColor("black")





    # TITLE WNDOW
    textRoots = Text(Point(0,0), "Logistic Map Explorer")
    textRoots.setSize(11)
    textRoots.setStyle('bold')
    textRoots.draw(winTitle)
    textRoots.setTextColor("black")




    # DRAW BIFURCATIOn


    # BUTTON ACTIVATION
    clickPt = winControlPanel.getMouse()
    while not btnQuit.clicked(clickPt):

        if btnGraph.clicked(clickPt):
            # Clear graph so their isnt overlap
            clear()
            drawGraph(entryR.getValue(), winGraph, entryX.getValue(), entryIteration.getValue())

            # Readjust the time series graph to the new amount of iterations
            winTimeSeries.setCoords(-0.125, -0.125, entryIteration.getValue(), 1.2)
            
            # Graph the time series in separate window 
            drawTimeSeries(winTimeSeries, entryX.getValue(), entryR.getValue(), entryIteration.getValue(), 0)

        # Draw new bifurcation diagram with transient value
        elif btnBifurcation.clicked(clickPt):
            winBifurcation.clear()
            drawBifurcation(winBifurcation, entryTransientIteration.getValue())

        elif btnGetR.clicked(clickPt):
            # When the buttons is pressed it waits for the 
            # Bifurcation window to be pressed and it gets the point thats pressed
            ptR = winBifurcation.getMouse()
            entryR.setText(round(ptR.getX(), 3))

        elif btnZoomIn.clicked(clickPt):
            zoomIn(winBifurcation, entryTransientIteration.getValue())

        elif btnZoomOut.clicked(clickPt):
            zoomOut(winBifurcation, entryTransientIteration.getValue())

        elif btnClear.clicked(clickPt):
            clear()
        
        clickPt = winControlPanel.getMouse()


    # quit all windows when quit button pressed
    winGraph.close()
    winControlPanel.close()
    winBifurcation.close()
    winTimeSeries.close()
    winTitle.close()
    winInstructions.close()


if __name__  == "__main__":
    main()