import sys
sys.path.append('../lib')
from DEgraphics_Herman import *
from math import *

ScreenHorizontal = 1440
ScreenVertical = 900

# global variable that keeps 
# a tally on the lines used 
# to draw the Koch curve
global KC_Lines 
KC_Lines = []

global polyList
polyList = []

# global variable that keeps
# the set values used to 
# configure the koch curve
global koch_Sets
koch_Sets = {"Length" : 0, "Theta" : 0, "Incline Angle" : 0, "Level" : 0, "Polygon_Sides" : 0}


def drawLine(w, startPt, direction, length):
    global KC_Lines
    xFinal = startPt.getX() + length * cos(radians(direction))
    yFinal = startPt.getY() + length * sin(radians(direction))
    endPt = Point(xFinal,yFinal)
    lineSegment = Line(startPt, endPt)
    KC_Lines.append(lineSegment)
    lineSegment.draw(w)
    
    startPt.move(xFinal-startPt.getX(), yFinal-startPt.getY())

def drawKC(w, start, theta, inclineAngle, length, level):
    if level == 0:
        drawLine(w, start, inclineAngle, length)

    else:
        scaleFactor = 1/(2*(1+cos(radians(theta))))
        length *= scaleFactor
        level -= 1
        drawKC(w, start, theta, inclineAngle, length, level)
        drawKC(w, start, theta, inclineAngle+theta, length, level)
        drawKC(w, start, theta, inclineAngle-theta, length, level)
        drawKC(w, start, theta, inclineAngle, length, level)


## DONE ##
def drawKC_Polygon(w, start, theta, length, level, n, inclineAngle):
    if n == 1: 
        drawKC(w, start, theta, inclineAngle, length, level)

    else:
        polygonAngle = 360/n
        curr = 360

        for i in range(n):
            drawKC(w, start, theta, curr, length, level)
            curr-=polygonAngle
    
# n is preset to one as most of the time it is a polygon
def getLength(length, level, theta, w, n = 1):
    length = length/(2*(1+cos(radians(theta))))

    finLen =  4**level * length * n
    units = ''

    if len(str(round(finLen))) <= 2: units = 'cm'
    if len(str(round(finLen))) == 3 and len(str(finLen)) <= 5: 
        units = 'm'
        finLen /= 100
    else:
        units = 'km'
        finLen /= 1000

    strL = "Length: " + str(round(finLen, 3)) + units
    return strL


def instructWinCall(text, textSize, offsetHoriz, offsetVert):
    # Creates window 
    instructWin = DEGraphWin(defCoords = [-10,-10,10,10], 
                    title ="instructWindow", 
                    width = 350, height = 100,
                    offsets=[ScreenHorizontal/4-offsetHoriz,ScreenVertical/8+offsetVert],
                    hasTitlebar = False,
                    hThickness=2,)
    instructWin.setBackground(color_rgb(110,110,110))

    # Instruction text 
    instructText = Text(Point(0, 0), text)
    instructText.setSize(textSize)
    instructText.draw(instructWin)
    instructText.setTextColor("black")

    # close instruction window early 
    btnNext = Button(instructWin, Point(5,-5), width=4, height=4,
        edgeWidth = 2, label = 'Next',
        buttonColors = ['white', 'black', 'black'],
        clickedColors = ['white', 'red', 'black'],
        font=('courier',11), timeDelay = 0.25)
    btnNext.activate()
    
    # when next is clicked it closes the current window
    clickPt = instructWin.getMouse()
    while not btnNext.clicked(clickPt):
        clickPt = instructWin.getMouse()
    instructWin.close()

# DOESNT WORK FULLY -> COLORS FINAL LEVEL ONLY
def KochColor(w, colors, level, pointList, polyList):
    if level > 0:
        list = []
        i = 0
        while i <= len(pointList)-3:
            # create point and set color
            poly = Polygon(pointList[i], pointList[i+1], pointList[i+2])
            poly.setFill(colors[level])
            
            # add to lists 
            polyList.append(poly)
            list.append(pointList[i+3])

            poly.draw(w)
            
            i+=4
        level -= 1
        KochColor(w, colors, level, pointList, polyList)

def main():
    global koch_Sets

    win = DEGraphWin(defCoords = [-10,-10,10,10], 
                    title ="Main", 
                    width = 600, height = 600,
                    offsets=[ScreenHorizontal/4,ScreenVertical/8],
                    hasTitlebar = False,
                    hThickness=1,)

    win_Header = DEGraphWin(defCoords = [-10,-10,10,10], 
                    title ="header", 
                    width = 600, height = 50,
                    offsets=[ScreenHorizontal/4,ScreenVertical/8-50],
                    hasTitlebar = False,
                    hThickness=1,)
    win_Header.setBackground(color_rgb(110,110,110))

    win_Control = DEGraphWin(defCoords = [-10,-10,10,10], 
                    title ="Control", 
                    width = 600, height = 200,
                    offsets=[ScreenHorizontal/4,ScreenVertical/8+600],
                    hasTitlebar = True,
                    hThickness=1,)
    win_Control.setBackground(color_rgb(110,110,110))

    win_Settings = DEGraphWin(defCoords = [-10,-10,10,10], 
                                title ="Settings", 
                                width = 200, height = 850,
                                offsets=[6000,6000],
                                hasTitlebar = True,
                                hThickness=1,)
    win_Settings.setBackground(color_rgb(110,110,110))

    headerText = Text(Point(0, 9.5), "Settings")
    headerText.setSize(18)
    headerText.setStyle("bold")
    headerText.draw(win_Settings)
    headerText.setTextColor("lightblue")

    colorDrop = DropDown(Point(0,7), choices=["Lined", 'Color'], bg = 'lightgrey')
    colorDrop.draw(win_Settings)

    length_Slider = Slider(Point(0, 5), min=0, max = 8, label = "Length", length=150, height=5)
    length_Slider.draw(win_Settings)

    level_Slider = Slider(Point(0, 2), min=0, max = 7, label = "Level", length=150, height=5)
    level_Slider.draw(win_Settings)

    incline_Slider = Slider(Point(0, -1), min=0, max = 90, label = "Incline", length=150, height=5)
    incline_Slider.draw(win_Settings)

    theta_Slider = Slider(Point(0, -4), min=0, max = 90, label = "Theta", length=150, height=5)
    theta_Slider.draw(win_Settings)

    sides_Slider = Slider(Point(0, -7), min=1, max = 5, label = "Poly Sides", length=150, height=5)
    sides_Slider.draw(win_Settings)
    
    # TEXT
    headerText = Text(Point(0, 0), "Koch Explorer")
    headerText.setSize(18)
    headerText.draw(win_Header)
    headerText.setStyle("bold")
    headerText.setTextColor("lightblue")


    # INPUTS
    btnGraphKoch = Button(win_Control, Point(-5,2.5), width=10, height=5,
                edgeWidth = 2, label = 'Draw Koch Curve',
                buttonColors = ['lightblue', 'black', 'black'],
                clickedColors = ['white', 'red', 'black'],
                font=('courier',11), timeDelay = 0.25)
    btnGraphKoch.activate()

    btnSettings = Button(win_Control, Point(-9.75,9), width=1.5, height=2,
                edgeWidth = 2, label = '⚙︎',
                buttonColors = ['lightgrey', 'black', 'black'],
                clickedColors = ['white', 'red', 'black'],
                font=('courier',11), timeDelay = 0.25)
    btnSettings.activate()

    btnInstruct = Button(win_Control, Point(-8,9), width=1.5, height=2,
                edgeWidth = 2, label = 'ⓘ',
                buttonColors = ['lightgrey', 'black', 'black'],
                clickedColors = ['white', 'red', 'black'],
                font=('courier',11), timeDelay = 0.25)
    btnInstruct.activate()

    btnQuit = Button(win_Control, Point(8,-7), width=1.5, height=2,
                edgeWidth = 2, label = 'Quit',
                buttonColors = ['darkred', 'black', 'black'],
                clickedColors = ['white', 'red', 'black'],
                font=('courier',11), timeDelay = 0.25)
    btnQuit.activate()


    # SETTINGS WINDOW IS SET TO NOT VIEWABLE AT FIRST
    settingsClicked = False
    clickPt = win_Control.getMouse()
    while not btnQuit.clicked(clickPt):
        
        if btnSettings.clicked(clickPt):
            if settingsClicked == True:
                settingsClicked = False
                win_Settings.moveTo(6000, 6000, ScreenHorizontal, ScreenVertical)
            elif settingsClicked == False:
                win_Settings.moveTo(ScreenHorizontal/4+600, ScreenVertical/8-50, 200, 850)
                settingsClicked = True

        elif btnInstruct.clicked(clickPt):
            instructWinCall("The button next to this allows you to modify the koch curve", 10, ScreenHorizontal/4-15, ScreenVertical/8+500)
            instructWinCall("This includes: Length, Level, Theta, Incline Angle,", 10, ScreenHorizontal/4-15, ScreenVertical/8+500)
            instructWinCall("Polygon sides", 10, ScreenHorizontal/4-15, ScreenVertical/8+500)
            instructWinCall("Length changes length of sides", 10, ScreenHorizontal/4-15, ScreenVertical/8+500)
            instructWinCall("Level changes how many koch curves their are ", 10, ScreenHorizontal/4-15, ScreenVertical/8+500)
            instructWinCall("Theta changes the angle of the koch curve", 10, ScreenHorizontal/4-15, ScreenVertical/8+500)
            instructWinCall("Incline angle changes the angle on which the curve sits", 10, ScreenHorizontal/4-15, ScreenVertical/8+500)
            instructWinCall("Poly sides changes the shape", 10, ScreenHorizontal/4-15, ScreenVertical/8+500)
            instructWinCall("Why dont you try pressing it after the instructions", 10, ScreenHorizontal/4-15, ScreenVertical/8+500)

        elif btnGraphKoch.clicked(clickPt):

            # GET VALS
            koch_Sets['Length'] = length_Slider.getValue()
            koch_Sets['Level'] = level_Slider.getValue()
            koch_Sets['Incline Angle'] = incline_Slider.getValue()
            koch_Sets['Theta'] = theta_Slider.getValue()
            koch_Sets['Polygon_Sides'] = sides_Slider.getValue()
            # CENTER POINT
            if koch_Sets['Level'] == 1:
                p = Point(-koch_Sets['Length']/2, 0)
            else:
                p = Point(-koch_Sets['Length']/2, koch_Sets['Length']/2)
            # UNDRAW PREVIOUS LINES
            global KC_Lines
            if len(KC_Lines) != 0:
                for i in KC_Lines:
                    i.undraw()
                KC_Lines = []

            # UNDRAW POLYGONS
            global polyList
            if len(polyList) != 0:
                for i in polyList:
                    i.undraw()
                polyList = []

            # DRAW KOCH CURVE
            drawKC_Polygon(win, p, koch_Sets['Theta'], koch_Sets['Length'], koch_Sets['Level'], koch_Sets['Polygon_Sides'], koch_Sets['Incline Angle'])
            if colorDrop.getChoice() == "Color":
                polyList = []
                pointList = []
                colors = ["red", 'green', 'blue', 'yellow', 'cyan', 'magenta', 'pink']
                
                for line in KC_Lines:
                    pointList.append(line.getP2())

                KochColor(win, colors,  koch_Sets['Level'], pointList, polyList)
            strL = getLength(koch_Sets['Length'],koch_Sets['Level'],koch_Sets['Theta'],win_Control,koch_Sets['Polygon_Sides'])

            # DISPLAY AND DELETE LENGTH TEXT
            if 'lenText' in locals():
                lenText.undraw()
            lenText = Text(Point(0, -5), strL)
            lenText.setSize(8)
            lenText.draw(win_Control)
            lenText.setTextColor("lightblue")    
            
                


        clickPt = win_Control.getMouse()


    win.close()
    win_Control.close()
    win_Settings.close()


main()