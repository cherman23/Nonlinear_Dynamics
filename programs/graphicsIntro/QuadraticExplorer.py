import sys
import math
sys.path.append('../lib')

# The * is importing everything in the file
from DEgraphics import *
from utils import *

#  MY SCREEN IS 3240 x 2160
# made global variables just in case somewhere it needs to be edited
global ScreenHorizontal
global ScreenVertical 
ScreenHorizontal = 3240
ScreenVertical = 2160


# Global variables for A, B, and C 
# so they can be edited/used in multiple 
global A
global B
global C
A = 1
B = 1
C = 1

''' Function that displays the Quadratic Function: 
    It contains: input for the variables, 
    changing light and dark mode,
    graph of the function that user inputs,
    button that exists windows,
    button for instructions,
    roots of the function.

    Large spaces in between functions are 
    for the legibility of the reader
    
    Author: Carter Herman 
        *with usage of DEGraphics module'''


def main():

    # Sections of Window Creation

    # This window will display the quadratic equation
    winEquation = DEGraphWin(defCoords = [-10,-10,10,10], 
                    title ="fun with graphics", 
                    width = 200, height = 100,
                    offsets=[ScreenHorizontal/16,ScreenVertical/8],
                    hasTitlebar = False,
                    hThickness=1,)

    # This window will display data about the equation
    # It will also have input data and button for instructions 
    winEquationData = DEGraphWin(defCoords = [-10,-10,10,10], 
                    title ="fun with graphics", 
                    width = 200, height = 400,
                    offsets=[ScreenHorizontal/16,ScreenVertical/5.83],
                    hasTitlebar = False,
                    hThickness=1,)

    # This window will show the graph of the function
    winGraph = DEGraphWin(defCoords= [-10,-10,10,10],
                        title = "Graph", 
                        width=500, height=500,
                        offsets=[ScreenHorizontal/16 + 200, ScreenVertical/8],
                        hasTitlebar = False,
                        hThickness=1,)

    # This is a title bar that includes the quit button
    winTitle = DEGraphWin(defCoords= [-10,-10,10,10],
                        title = "QuitBar", 
                        width=700, height=30,
                        offsets=[ScreenHorizontal/16, ScreenVertical/9],
                        hasTitlebar = False,
                        hThickness=1,)

    winControl = DEGraphWin(defCoords= [-10,-10,10,10],
                        title = "QuitBar", 
                        width=200, height=530,
                        offsets=[(ScreenHorizontal/16)+700, ScreenVertical/9],
                        hasTitlebar = False,
                        hThickness=1,)

    # pop-up panel for instructions on how to use the garphing
    winInstructions = DEGraphWin(defCoords= [-10,-10,10,10],
                        title = "QuitBar", 
                        width=200, height=530,
                        offsets=[(ScreenHorizontal/16)+900, ScreenVertical/9],
                        hasTitlebar = False,
                        hThickness=1,)




    #  SETS COLORS OF WINDOWS
    winEquationData.setBackground(color_rgb(225,225,225))
    winEquation.setBackground(color_rgb(225,225,225)) 
    winGraph.setBackground(color_rgb(225,225,225))
    winTitle.setBackground(color_rgb(225,225,225))
    winControl.setBackground(color_rgb(225,225,225))
    winInstructions.setBackground(color_rgb(225,225,225))

    # sets instructions windows to closed 
    winInstructions.close()





    # SETS GRAPH AXES
    j = -10
    winGraph.toggleAxes()
    while j < 10:
        if j != 0:
            # dashes for x axis
            dashX = Line(Point(j,0.2),Point(j,-0.2), style='solid')
            dashX.draw(winGraph)

            # dashes for y axis
            dashY = Line(Point(0.2,j),Point(-0.2,j), style='solid')
            dashY.draw(winGraph)
        j+=0.5



    # ALL BUTTONS: 
    
    # ZOOM IN BUTTON
    btnZoomIn= Button(winControl, Point(-4.5, 2.5), width=10, height=1,
                label="Zoom In", 
                buttonColors = ['darkgrey', 'black', 'black'],
                clickedColors = ['white', 'red', 'black'],
                font=('courier',11), timeDelay = 0.25)
    btnZoomIn.activate()

    # ZOOM OUT BUTTON
    btnZoomOut= Button(winControl, Point(-4.5, 0), width=10, height=1,
                label="Zoom Out", 
                buttonColors = ['darkgrey', 'black', 'black'],
                clickedColors = ['white', 'red', 'black'],
                font=('courier',11), timeDelay = 0.25)
    btnZoomOut.activate()

    # CLEAR BUTTON
    btnClear= Button(winControl, Point(-4.5, -2.5), width=10, height=1,
                label="Clear Graph", 
                buttonColors = ['darkgrey', 'black', 'black'],
                clickedColors = ['white', 'red', 'black'],
                font=('courier',9), timeDelay = 0.25)
    btnClear.activate()

    # QUIT BUTTON
    btnQuit = Button(winControl, Point(-4.5,-7.5), width=10, height=1,
                edgeWidth = 2, label = 'Quit',
                buttonColors = ['darkred', 'black', 'black'],
                clickedColors = ['white', 'red', 'black'],
                font=('courier',11), timeDelay = 0.25)
    btnQuit.activate()

    # DARK MODE AND LIGHT MODE BUTTON
    btnDarkMode = Button(winControl, Point(-4.5,-5), width=10, height=1,
                edgeWidth = 2, label = 'Dark Mode',
                buttonColors = ['darkgrey', 'black', 'black'],
                clickedColors = ['white', 'red', 'black'],
                font=('courier',11), timeDelay = 0.25)
    btnDarkMode.activate()

    # BUTTON FOR INSTRUCTIONS
    btnInstruct = Button(winControl, Point(-4.5,7.5), width=10, height=1,
                edgeWidth = 2, label = 'Instruction',
                buttonColors = ['darkgrey', 'black', 'black'],
                clickedColors = ['white', 'red', 'black'],
                font=('courier',11), timeDelay = 0.25)
    btnInstruct.activate()

    # FINDING ROOTS
    btnCalc = Button(winControl, Point(-4.5,5), width=10, height=1,
                    edgeWidth = 2, label = 'Graph',
                    buttonColors = ['darkgrey', 'black', 'black'],
                    clickedColors = ['white', 'red', 'black'],
                    font=('courier',11), timeDelay = 0.25)
    btnCalc.activate()




    # ALL TEXT:

    # LABEL FOR GRAPH
    for i in range(-9,10):
        if i != 0:
            iText = str(i)
            # X Axis labels
            titleText = Text(Point(i, 0.5),iText)
            titleText.setTextColor('red')
            titleText.setSize(8)
            titleText.draw(winGraph)

            # Y Axis lables
            titleText = Text(Point(0.5, i),iText)
            titleText.setTextColor('red')
            titleText.setSize(8)
            titleText.draw(winGraph)


    # title window
    titleText = Text(Point(0,0),"Quadratic Equation Explorer")
    titleText.setStyle('bold')
    titleText.setTextColor('Black')
    titleText.setSize(12)
    titleText.draw(winTitle)

    # CONTROL PANEL
    controlText = Text(Point(0,9.4),"Control Panel")
    controlText.setStyle('bold')
    controlText.setTextColor('darkred')
    controlText.setSize(11)
    controlText.draw(winControl)

    # Text that shows quadratic equation and edits its features
    equationText = Text(Point(0,0),"Ax^2 + Bx + C")
    equationText.setStyle('bold')
    equationText.setTextColor('darkred')
    equationText.setSize(11)
    equationText.draw(winEquation)

    # Labels for input variables
    textInput = Text(Point(0,8.5),"Inputs Domain: [-10, 10]")
    textInput.setTextColor('darkred')
    textInput.setSize(13)
    textInput.setStyle('bold')
    textInput.draw(winEquationData)

    # label for A input
    textA = Text(Point(-7,6),"A =")
    textA.setTextColor('darkred')
    textA.setSize(11)
    textA.setStyle('bold')
    textA.draw(winEquationData)

    # label for B input
    textB = Text(Point(-7,2),"B =")
    textB.setTextColor('darkred')
    textB.setSize(11)
    textB.setStyle('bold')
    textB.draw(winEquationData)

    # label for C input
    textC = Text(Point(-7,-2),"C =")
    textC.setTextColor('darkred')
    textC.setSize(11)
    textC.setStyle('bold')
    textC.draw(winEquationData)

    # ROOTS OF FUNCTION
    # (-b +- sqrt(b^2-4ac)) / 2a
    textRoots = Text(Point(-1,-6), "Roots: None")
    textRoots.setSize(10)
    textRoots.setStyle('bold')
    textRoots.draw(winEquationData)
    textRoots.setTextColor("darkred")

    # explanation of roots
    rootX = Text(Point(-1,-8), "(when y equals 0)")
    rootX.setSize(8)
    rootX.setStyle('bold')
    rootX.draw(winEquationData)
    rootX.setTextColor("darkred")


    # ALL ENTRY OBJECTS

    # Inputs for variables 
    entryA = IntEntry(Point(-3,6), 5, span = [-10,10],
                       colors = ['gray','black'],
                       errorColors = ['darkred','white'])
    entryA.setDefault(1)
    entryA.setSize(11)
    entryA.draw(winEquationData)
    A = entryA.getValue()

    entryB = IntEntry(Point(-3,2), 5, span = [-10,10],
                       colors = ['gray','black'],
                       errorColors = ['darkred','white'])
    entryB.setDefault(1)
    entryB.setSize(11)
    entryB.draw(winEquationData)
    B = entryB.getValue()

    entryC = IntEntry(Point(-3,-2), 5, span = [-10,10],
                       colors = ['gray','black'],
                       errorColors = ['darkred','white'])
    entryC.setDefault(1)
    entryC.setSize(11)
    entryC.draw(winEquationData)
    C = entryC.getValue()





    # ACTIVATE ALL CLICKS FOR BUTTONS 
    # and dark mode bool
    # and instruction pop-up bool
    clickPt = winControl.getMouse()
    Dark = False
    instructWin = False


    # Lists of objects so they don't disappear during zooms
    rootCircles = []
    graphPoints = []

    # ACTIVATE BUTTONS

    # while quit button is not clicked allow other buttons to be clicked
    while not btnQuit.clicked(clickPt):

        # CALCULATING NEW ROOTS AND GRAPHING AGAIN

        if btnCalc.clicked(clickPt):
            # get current values 
            A = entryA.getValue()
            B = entryB.getValue()
            C = entryC.getValue()

            # check for zero cases and remove them
            if A == 0: 
                A = 1
                entryA.setText(1)

            #  A function that returns a string for roots of function
            strRoots = quadFunc(A, B, C)
            textRoots.setText(strRoots)

            # CLEAR GRAPH FOR NEW FUNCTION:
            # Clears the circles 
            for i in range(len(rootCircles)):
                rootCircles[i].undraw()
            # Clears the points
            for i in range(len(graphPoints)):
                graphPoints[i].undraw()

            # Erases lists to because graph is gone
            rootCircles = []
            graphPoints = []

            # X values for graphing
            xs = (x * 0.01 for x in range(-1000, 1000))
            
            # GRAPHING -> Connected to btnCalc
            for i in xs:
                y = (A*(i*i))+(B*i)+C
                gp = Point(i, y)
                # add points to list so they can be undrawn when clearing
                graphPoints.append(gp)
                gp.draw(winGraph)
            
            # Drawing circles to show roots
            # quadFuncCircles returns a list of circles
            rootCircles = quadFuncCircles(A, B, C)
            # If the function has roots
            if len(rootCircles) > 0:
                for i in range(len(rootCircles)):
                    rootCircles[i].draw(winGraph)
                    
      
            
        # button to open and close the instruction window
        # only open when the use needs it 
        elif btnInstruct.clicked(clickPt):
            if instructWin == True:
                # window can be closed to declutter space 
                winInstructions.close()
                instructWin = False
                btnInstruct.setCaption('Instruction')
            elif instructWin == False:

                # Have to create a new window every time it is closed
                # because there is no open function for windows
                winInstructions = DEGraphWin(defCoords= [-10,-10,10,10],
                        title = "QuitBar", 
                        width=200, height=530,
                        offsets=[(ScreenHorizontal/16)+900, ScreenVertical/9],
                        hasTitlebar = False,
                        hThickness=1,)

                # INSTRUCTIONS have to redrawn every time
                # text has to be redrawn everytime the window opens
                # SETS EACH TO BOLD and DARK RED
                # PLACES EACH ONE NEXT TO THE BUTTON IT CORRESPONDS TO
                textRoots = Text(Point(0,9), "Instructions:")
                textRoots.setSize(12)
                textRoots.setStyle('bold')
                textRoots.draw(winInstructions)
                textRoots.setTextColor("darkred")
                
                textRoots = Text(Point(0,7), "<- Close instruction window")
                textRoots.setSize(10)
                textRoots.setStyle('bold')
                textRoots.draw(winInstructions)
                textRoots.setTextColor("darkred")

                textRoots = Text(Point(0,4.5), "-> Press to Graph Function")
                textRoots.setSize(10)
                textRoots.setStyle('bold')
                textRoots.draw(winInstructions)
                textRoots.setTextColor("darkred")

                textRoots = Text(Point(0,2.5), "-> Click two points and")
                textRoots.setSize(10)
                textRoots.setStyle('bold')
                textRoots.draw(winInstructions)
                textRoots.setTextColor("darkred")

                textRoots = Text(Point(0,2), "click point in created square")
                textRoots.setSize(10)
                textRoots.setStyle('bold')
                textRoots.draw(winInstructions)
                textRoots.setTextColor("darkred")

                textRoots = Text(Point(0,-0.5), "-> Click to fully zoom out")
                textRoots.setSize(10)
                textRoots.setStyle('bold')
                textRoots.draw(winInstructions)
                textRoots.setTextColor("darkred")

                textRoots = Text(Point(0,-3), "-> Click to clear graph")
                textRoots.setSize(10)
                textRoots.setStyle('bold')
                textRoots.draw(winInstructions)
                textRoots.setTextColor("darkred")

                textRoots = Text(Point(0,-5.5), "-> Click for dark mode")
                textRoots.setSize(10)
                textRoots.setStyle('bold')
                textRoots.draw(winInstructions)
                textRoots.setTextColor("darkred")

                textRoots = Text(Point(0,-8), "-> Click to quit")
                textRoots.setSize(10)
                textRoots.setStyle('bold')
                textRoots.draw(winInstructions)
                textRoots.setTextColor("darkred")


                # Makes sure it coencides with the rest of the windows
                if Dark == False:
                    winInstructions.setBackground(color_rgb(225,225,225))
                elif Dark == True:
                    winInstructions.setBackground(color_rgb(50,50,50))
                
                # Changes button so use knnows they can close instructions
                btnInstruct.setCaption('Close Win')
                instructWin = True

        # BUTTON TO CLEAR GRAPH
        elif btnClear.clicked(clickPt):
            # Clears the circles 
            for i in range(len(rootCircles)):
                rootCircles[i].undraw()
            # Clears the points
            for i in range(len(graphPoints)):
                graphPoints[i].undraw()

            # Erases lists to because graph is gone
            rootCircles = []
            graphPoints = []

            # Roots set to none because function is clears
            textRoots.setText("Roots: None")

        # buttons to zoom in
        elif btnZoomIn.clicked(clickPt):
            winGraph.zoom(whichWay = ZOOM_IN, keepRatio = True)
            
        # zoom out button
        elif btnZoomOut.clicked(clickPt):
            winGraph.zoom(whichWay = ZOOM_OUT, keepRatio = True)
            
            


        # When clicked the windows backgrounds become darker 
        # Added for aesthetic use
        elif btnDarkMode.clicked(clickPt):
            if Dark == False:
                winEquationData.setBackground(color_rgb(50,50,50))
                winEquation.setBackground(color_rgb(50,50,50)) 
                winGraph.setBackground(color_rgb(50,50,50))
                winTitle.setBackground(color_rgb(50,50,50))
                winControl.setBackground(color_rgb(50,50,50))
                if instructWin == True:
                    winInstructions.setBackground(color_rgb(50,50,50))
                titleText.setTextColor('white')
                
                # Ability to switch back to light mode
                Dark = True 
                btnDarkMode.setCaption('Light Mode')
                
            # if the windows are already dark, turn it to light mode 
            elif Dark == True:
                winEquationData.setBackground(color_rgb(225,225,225))
                winEquation.setBackground(color_rgb(225,225,225)) 
                winGraph.setBackground(color_rgb(225,225,225))
                winTitle.setBackground(color_rgb(225,225,225))
                winControl.setBackground(color_rgb(225,225,225))

                # checks to see if instructions are open because if its closed 
                # The program would crash altering a closed window
                if instructWin == True:
                    winInstructions.setBackground(color_rgb(225,225,225))
                btnDarkMode.setCaption('Dark Mode')
                titleText.setTextColor('black')
                Dark = False
        
        # get click point again so buttons can be pressed
        clickPt = winControl.getMouse()


    # closing all windows after quit button is pressed 
    winEquationData.close()
    winTitle.close()
    winGraph.close()
    winEquation.close()
    # checks to see if instructions is currently open 
    # so no error is thrown if already closed
    if instructWin == True:
        winInstructions.close()


if __name__  == "__main__":
    main()