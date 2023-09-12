# written by: Carter Herman
# This allows the user to explore the mandelbrot set and the julia set
# The user can change the color scheme, the number of iterations, and the clarity of the plot
# The user can also zoom in and out of the plot
# The user can also change the c value of the julia set
# using the mandelbrot set as a guide



# need to import stuff from lib, namely 
# DE graphics 
import sys
sys.path.append('../lib')
from DEgraphics_Herman import *
from numpy import abs
from random import choice, uniform
import cmath

# mac user screen size 
ScreenHorizontal = 1440
ScreenVertical = 900

# Iterate the mandelbrot set 
def iterate_T(c, iterations):
    counter = 0
    greaterThanIterate = 0
    finZ = complex(0)

    while counter < iterations:
        counter += 1
        finZ = finZ**2 + c

        if abs(finZ) > abs(2):
            if greaterThanIterate == 0: 
                greaterThanIterate = counter

            break

    return [finZ, greaterThanIterate]

# Iterate the julia set 
def iterateJulia(c, z, iterations):
    counter = 0
    finZ = z
    greaterThanIterate = 0

    while counter < iterations:
        counter += 1
        finZ = finZ**2 + c

        if abs(finZ) > abs(2):
            if greaterThanIterate == 0: 
                greaterThanIterate = counter
            
            break

    return [finZ, greaterThanIterate]

def inverseJulia(c, z, iterations):
    counter = 0

    while counter < iterations:
        counter += 1
        z = cmath.sqrt(z-c) * choice([-1,1])
        
    
    return (z)


def mandelbrotPlot(win, iterations, color, defCoords, iterationDiv = 1, clarity = 200):
    # Changes the amount of points plotted based on clarity
    iterationDiv = iterationDiv * clarity
    # Starting coords
    x = defCoords[0]
    y = defCoords[1]

    # Changes iteration amount
    iter = abs(defCoords[0]/iterationDiv)

    # List created 
    coordsList = []


    while x < defCoords[2]:
        y = defCoords[1]

        while y < defCoords[3]:

            list = iterate_T(complex(x, y), iterations)
            
            if color == "Black and White":
                # check if its less than 2 
                    # plot grey if greater
                if abs(list[0]) < abs(2):
                    coordsList.append([x,y,'black'])

            elif color == "Escaping Colors":
            # THE RANGE WILL GO FROM rgb(0,0,0) to rgb(48, 25, 52) with 8 shades

                list[1] = list[1]

                if 0 == list[1]:
                    coordsList.append([x,y,'black'])
                
                elif 99 > list[1] >= 70: 
                    coordsList.append([x,y,'darkred'])

                elif 70 > list[1] >= 40: 
                    coordsList.append([x,y,'darkblue'])

                elif 40 > list[1] >= 25: 
                    coordsList.append([x,y,'purple'])

                elif 20 > list[1] >= 15: 
                    coordsList.append([x,y,'magenta'])

                elif 15 > list[1] >= 10: 
                    coordsList.append([x,y,'cyan'])

            elif color == "Pink Scale":
                # THE RANGE WILL GO COLOR ON PINK GRADIENT
    
                list[1] = list[1]

                if 99 > list[1] >= 70: 
                    coordsList.append([x,y,color_rgb(121, 48, 90)])

                elif 70 > list[1] >= 40: 
                    coordsList.append([x,y,color_rgb(142, 53, 99)])

                elif 40 > list[1] >= 25: 
                    coordsList.append([x,y,color_rgb(163, 56, 108)])

                elif 20 > list[1] >= 15: 
                    coordsList.append([x,y,color_rgb(179, 59, 114)])

                elif 15 > list[1] >= 10: 
                    coordsList.append([x,y,color_rgb(181, 83, 133)])

                elif 10 > list[1] >= 8: 
                    coordsList.append([x,y,color_rgb(191, 107, 153)])

                elif 8 > list[1] >= 6: 
                    coordsList.append([x,y,color_rgb(207, 145, 181)])

                elif 6 > list[1] >= 4: 
                    coordsList.append([x,y,color_rgb(224, 187, 210)])

                elif 4 > list[1] >= 2: 
                    coordsList.append([x,y,color_rgb(245, 217, 230)])

                elif list[1] == 1: 
                    coordsList.append([x,y,color_rgb(255, 247, 253)])

                elif list[1] == 0: 
                    coordsList.append([x,y,color_rgb(87, 38, 73)])


            y+=iter
            
        x+=iter
    
    plot(coordsList, win)
    
        

def juliaPlot(win, iterations, color, cVAL, defCoords, iterationDiv = 1, clarity = 200):
    iterationDiv = iterationDiv * clarity
    # getting x and y value of current window size
    x = defCoords[0]
    y = defCoords[1]
    iter = abs(defCoords[0]/iterationDiv)

    # list of coordinates and what color to plot them
    coordsList = []

    # iterate through the plane and find whether or not it follows the rules of the set
    if color != "Inverse Algorithm":
        while x < defCoords[2]:
            y = defCoords[1]

            while y < defCoords[3]:
       
                list = iterateJulia(cVAL, complex(x, y), iterations)

                if color == "Black and White":
                    # check if its less than 2 
                        # plot grey if greater
                    if abs(list[0]) < abs(2):
                        coordsList.append([x,y,'black'])

                elif color == "Escaping Colors":
                    # THIS WILL SHOW ONLY ESCAPING VALUES ON THE BORDER
        

                    if 99 > list[1] >= 70: 
                        coordsList.append([x,y,'darkred'])

                    elif 70 > list[1] >= 40: 
                        coordsList.append([x,y,'darkblue'])

                    elif 40 > list[1] >= 25: 
                        coordsList.append([x,y,'purple'])

                    elif 20 > list[1] >= 15: 
                        coordsList.append([x,y,'magenta'])

                    elif 15 > list[1] >= 10: 
                        coordsList.append([x,y,'cyan'])

                elif color == "Pink Scale":
                    # THE RANGE WILL GO FROM rgb(0,0,0) to rgb(48, 25, 52) with 8 shades
                
                    if 99 > list[1] >= 70: 
                        coordsList.append([x,y,color_rgb(121, 48, 90)])

                    elif 70 > list[1] >= 40: 
                        coordsList.append([x,y,color_rgb(142, 53, 99)])

                    elif 40 > list[1] >= 25: 
                        coordsList.append([x,y,color_rgb(163, 56, 108)])

                    elif 20 > list[1] >= 15: 
                        coordsList.append([x,y,color_rgb(179, 59, 114)])

                    elif 15 > list[1] >= 10: 
                        coordsList.append([x,y,color_rgb(181, 83, 133)])

                    elif 10 > list[1] >= 8: 
                        coordsList.append([x,y,color_rgb(191, 107, 153)])

                    elif 8 > list[1] >= 6: 
                        coordsList.append([x,y,color_rgb(207, 145, 181)])

                    elif 6 > list[1] >= 4: 
                        coordsList.append([x,y,color_rgb(224, 187, 210)])

                    elif 4 > list[1] >= 2: 
                        coordsList.append([x,y,color_rgb(245, 217, 230)])

                    elif list[1] == 1: 
                        coordsList.append([x,y,color_rgb(255, 247, 253)])

                    elif list[1] == 0: 
                        coordsList.append([x,y,color_rgb(87, 38, 73)])

                y+=iter
            
            x+=iter

    
    # implementing inverse julia 
    else:
        list = []
        for i in range(0,10000):
            list.append(complex(uniform(-2,2), uniform(-2,2)))

        for q in list:
            q = inverseJulia(cVAL, q, iterations)  

            coordsList.append([q.real,q.imag,'black'])

    plot(coordsList, win)


# given a list of coords and colors, plots the points
def plot(coordsList, win):
    for j in range(4):
        
        for i in range(j,len(coordsList),4):
            currList = coordsList[i]
            win.plot(currList[0], currList[1], currList[2])
        win.update()
    
# Calls each of the different windows that 
# move to show the instructions
def instructWinCall(text, textSize, offsetHoriz, offsetVert):
    # Creates window 
    instructWin = DEGraphWin(defCoords = [-10,-10,10,10], 
                    title ="instructWindow", 
                    width = 350, height = 100,
                    offsets=[ScreenHorizontal/4-offsetHoriz,ScreenVertical/8+offsetVert],
                    hasTitlebar = False,
                    hThickness=2,)
    instructWin.setBackground(color_rgb(253,215,228))

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

def welcomeScreen(controlWin):
    welcomeText = Text(Point(0, 6), "Welcome to the Super Mandelbrot Explorer!")
    welcomeText.setSize(24)
    welcomeText.draw(controlWin)
    welcomeText.setTextColor("pink")

    carterText = Text(Point(0, 4.5), "by Carter Herman")
    carterText.setSize(14)
    carterText.draw(controlWin)
    carterText.setTextColor("pink")

    defText = Text(Point(0, 2), "DEFINITION: The Mandelbrot Set is the set of complex numbers c for which")
    defText.setSize(12)
    defText.draw(controlWin)
    defText.setTextColor("lightblue")

    defText2 = Text(Point(0, 1), "the function f(z) = z^2 + c when iterated from z = 0 does not diverge to infinity")
    defText2.setSize(12)
    defText2.draw(controlWin)
    defText2.setTextColor("lightblue")

    defText3 = Text(Point(0, 0), "and remains bounder by a circle of radius 2 centered at the origin")
    defText3.setSize(12)
    defText3.draw(controlWin)
    defText3.setTextColor("lightblue")

    defText4 = Text(Point(0, -1.5), "DEFINITION: Julia sets are similar except iterating through Z values instead of C")
    defText4.setSize(12)
    defText4.draw(controlWin)
    defText4.setTextColor("lightblue")

    defText5 = Text(Point(0, -4), "Please press instructions on the next screen")
    defText5.setSize(13)
    defText5.draw(controlWin)
    defText5.setTextColor("pink")

    btnContinue = Button(controlWin, Point(-4,-5), width=8, height=2,
                edgeWidth = 2, label = 'Continue',
                buttonColors = ['pink', 'black', 'black'],
                clickedColors = ['white', 'red', 'black'],
                font=('courier',11), timeDelay = 0.25)
    btnContinue.activate()

    clickPt = controlWin.getMouse()
    while not btnContinue.clicked(clickPt):
        clickPt = controlWin.getMouse()

    # Undraw all the welcome screen text before launching the rest
    # of the program
    welcomeText.undraw()
    carterText.undraw()
    btnContinue.undraw()
    defText.undraw()
    defText2.undraw()
    defText3.undraw()
    defText4.undraw()
    defText5.undraw()


def main():

    # WINDOWS 
    headerWin = DEGraphWin(defCoords = [-10,-10,10,10], 
                    title ="header", 
                    width = 800, height = 50,
                    offsets=[ScreenHorizontal/4,ScreenVertical/8-50],
                    hasTitlebar = False,
                    hThickness=3,)
    headerWin.setBackground(color_rgb(90,90,90))

    mandelWin = DEGraphWin(defCoords = [-2,-2,2,2], 
                    title ="mandelbrotWindow", 
                    width = 400, height = 400,
                    offsets=[ScreenHorizontal/4,ScreenVertical/8],
                    hasTitlebar = False,
                    hThickness=1,)
    mandelWin.setBackground(color_rgb(255,255,255))

    juliaWin = DEGraphWin(defCoords = [-2,-2,2,2], 
                    title ="mandelbrotWindow", 
                    width = 400, height = 400,
                    offsets=[ScreenHorizontal/4+400,ScreenVertical/8],
                    hasTitlebar = False,
                    hThickness=1,)
    juliaWin.setBackground(color_rgb(255,255,255))

    controlWin = DEGraphWin(defCoords = [-10,-10,10,10], 
                    title ="control panel", 
                    width = 800, height = 450,
                    offsets=[ScreenHorizontal/4,ScreenVertical/8+400],
                    hasTitlebar = True,
                    hThickness=0,)
    controlWin.setBackground(color_rgb(90,90,90))



    # HEADER TEXT
    headerText = Text(Point(0, 0), "Super Mandelbrot Explorer")
    headerText.setSize(18)
    headerText.draw(headerWin)
    headerText.setTextColor("pink")



    # GENERATE WELCOME SCREEN
    welcomeScreen(controlWin)

    '''
        Once the welcome screen is passed 
        it opens up the rest of the program 
        for the user to explore
    '''

    # MANDELBROT AND JULIA GRAPHING
    btnGraphMandelBrot = Button(controlWin, Point(-9.5,-4), width=8, height=2,
                edgeWidth = 2, label = 'Draw Mandelbrot Fractal',
                buttonColors = ['lightgray', 'black', 'black'],
                clickedColors = ['white', 'red', 'black'],
                font=('courier',11), timeDelay = 0.25)
    btnGraphMandelBrot.activate()

    btnGraphJulia = Button(controlWin, Point(1,-4), width=8, height=2,
                edgeWidth = 2, label = 'Get C Value',
                buttonColors = ['lightgray', 'black', 'black'],
                clickedColors = ['white', 'red', 'black'],
                font=('courier',11), timeDelay = 0.25)
    btnGraphJulia.activate()



    # QUIT BUTTON
    btnQuit = Button(controlWin, Point(1,-7.5), width=8, height=2,
                edgeWidth = 2, label = 'Quit',
                buttonColors = ['darkred', 'black', 'black'],
                clickedColors = ['white', 'red', 'black'],
                font=('courier',11), timeDelay = 0.25)
    btnQuit.activate()



    # INSTRUCTIONS BUTTON
    btnInstructions = Button(controlWin, Point(-9.5,-7.5), width=8, height=2,
                edgeWidth = 2, label = 'Instructions',
                buttonColors = ['pink', 'black', 'black'],
                clickedColors = ['white', 'red', 'black'],
                font=('courier',11), timeDelay = 0.25)
    btnInstructions.activate()



    # ZOOMING BUTTONS
    btnZoomInMandel = Button(controlWin, Point(-9.5,-1), width=4, height=2,
                edgeWidth = 2, label = 'Zoom In Mandel',
                buttonColors = ['lightgray', 'black', 'black'],
                clickedColors = ['white', 'red', 'black'],
                font=('courier',11), timeDelay = 0.25)
    btnZoomInMandel.activate()

    btnZoomOutMandel = Button(controlWin, Point(-5.5,-1), width=4, height=2,
                edgeWidth = 2, label = 'Zoom Out Mandel',
                buttonColors = ['lightgray', 'black', 'black'],
                clickedColors = ['white', 'red', 'black'],
                font=('courier',11), timeDelay = 0.25)
    btnZoomOutMandel.activate()

    btnZoomInJulia = Button(controlWin, Point(1,-1), width=4, height=2,
                edgeWidth = 2, label = 'Zoom In Julia',
                buttonColors = ['lightgray', 'black', 'black'],
                clickedColors = ['white', 'red', 'black'],
                font=('courier',11), timeDelay = 0.25)
    btnZoomInJulia.activate()

    btnZoomOutJulia = Button(controlWin, Point(5,-1), width=4, height=2,
                edgeWidth = 2, label = 'Zoom Out Julia',
                buttonColors = ['lightgray', 'black', 'black'],
                clickedColors = ['white', 'red', 'black'],
                font=('courier',11), timeDelay = 0.25)
    btnZoomOutJulia.activate()



    # SETTINGS FOR COLORS WITH DROPDOWN
    mandelSlider = DropDown(Point(-5.5, 1), choices=['Black and White', 'Escaping Colors', 'Pink Scale'], bg = 'lightgrey')
    mandelSlider.draw(controlWin)

    juliaSlider = DropDown(Point(5, 1), choices=['Black and White', 'Escaping Colors', 'Pink Scale', 'Inverse Algorithm',], bg = 'lightgrey')
    juliaSlider.draw(controlWin)



    # ITERATION AMOUNTS 
    entryMandelText = Text(Point(-6.25, 8), "Iteration amount for Mandelbrot [0,250]: ")
    entryMandelText.setSize(10)
    entryMandelText.setStyle('bold')
    entryMandelText.draw(controlWin)
    entryMandelText.setTextColor("white")

    entryIterationsMandel = IntEntry(Point(-2.5, 8), 5, span = [0,250],
                colors = ['gray','black'],
                errorColors = ['red','white'])
    entryIterationsMandel.setDefault(100)
    entryIterationsMandel.setText(100)
    entryIterationsMandel.draw(controlWin)

    entryJuliaText = Text(Point(4, 8), "Iteration amount for Julia Set [0,250]: ")
    entryJuliaText.setStyle('bold')
    entryJuliaText.setSize(10)
    entryJuliaText.draw(controlWin)
    entryJuliaText.setTextColor("white")

    entryIterationsJulia = IntEntry(Point(7.75, 8), 5, span = [0,250],
                colors = ['gray','black'],
                errorColors = ['red','white'])
    entryIterationsJulia.setDefault(100)
    entryIterationsJulia.setText(100)
    entryIterationsJulia.draw(controlWin)



    # CLARITY SETTINGS
    mandelClarity = DropDown(Point(-3.5, 4.5), choices=['100%', '90%','75%','50%', '25%'], bg = 'lightgrey')
    mandelClarity.draw(controlWin)

    entryJuliaClarity = Text(Point(-6.7, 4.5), "Mandelbrot Set Clarity:")
    entryJuliaClarity.setStyle('bold')
    entryJuliaClarity.setSize(10)
    entryJuliaClarity.draw(controlWin)
    entryJuliaClarity.setTextColor("white")

    juliaClarity = DropDown(Point(7, 4.5), choices=['100%', '90%', '75%','50%', "25%"], bg = 'lightgrey')
    juliaClarity.draw(controlWin)

    entryJuliaClarity = Text(Point(4, 4.5), "Julia Set Clarity:")
    entryJuliaClarity.setStyle('bold')
    entryJuliaClarity.setSize(10)
    entryJuliaClarity.draw(controlWin)
    entryJuliaClarity.setTextColor("white")


    # WHEN BUTTONS ARE CLICKED
    clickPt = controlWin.getMouse()
    zoomAmount = 1
    zoomAmountJulia = 1
    while not btnQuit.clicked(clickPt):
        Zoomed = False
        Zoomed_Julia = False

        # Getting clarity choice for mandelbrot
        mandelClarityVal = mandelClarity.getChoice()
        mandelClarityVal = mandelClarityVal[0:len(mandelClarityVal)-1]
        mandelClarityVal = int(mandelClarityVal)*2

        # getting clarity choice for julia
        juliaClarityVal = juliaClarity.getChoice()
        juliaClarityVal = juliaClarityVal[0:len(juliaClarityVal)-1]
        juliaClarityVal = int(juliaClarityVal)*2



        # Graphing mandel brot fractal
        if btnGraphMandelBrot.clicked(clickPt):
            mandelWin.clear() 

            if 'cLineX' in locals():
                cLineX.undraw()
                cLineY.undraw()

            try: 
                int(entryIterationsMandel.getText()) >= 0
            except:
                entryIterationsMandel.setText(100)
            mandelbrotPlot(mandelWin, int(entryIterationsMandel.getText()), 
            mandelSlider.getChoice(), mandelWin.defaultCoords, zoomAmount, mandelClarityVal)

            if 'cLineX' in locals():
                cLineX.draw(mandelWin)
                cLineY.draw(mandelWin)



        # use mouse to get c value from mandelbrot
        elif btnGraphJulia.clicked(clickPt):
            global ptC
            ptC = mandelWin.getMouse()

            juliaWin.clear()

            try: 
                int(entryIterationsJulia.getText()) >= 0
            except:
                entryIterationsJulia.setText(100)
            juliaPlot(juliaWin, int(entryIterationsJulia.getText()), juliaSlider.getChoice(), 
            complex(ptC.getX(),ptC.getY()), juliaWin.defaultCoords, 1, juliaClarityVal)
            
            # check if it is already drawn and undraw it so a new value can be drawn
            if 'cTextDrawn' in locals():
                cTextDrawn.undraw()
                cLineX.undraw()
                cLineY.undraw()

            # creating a string for the point values of c val
            strCVal = "C Value at (" + str(round(ptC.getX(),3)) + ", " + str(round(ptC.getY(),3)) + "i)"

            # write out the c values
            cTextDrawn = Text(Point(4.9, -6.8), strCVal)
            cTextDrawn.setStyle('bold')
            cTextDrawn.setSize(10)
            cTextDrawn.draw(controlWin)
            cTextDrawn.setTextColor("pink")

            # draw line on the mandelbrot set for where it is 
            cLineY = Line(Point(ptC.getX(), -2), Point(ptC.getX(), 2), style='solid')
            cLineY.setFill('red')
            cLineX = Line(Point(-2, ptC.getY()), Point(2, ptC.getY()), style='solid')
            cLineX.setFill('red')
            cLineX.draw(mandelWin)
            cLineY.draw(mandelWin)


        # zoom in button, this changes the mutliplier so the image is still clear when zoomed in 
        elif btnZoomInMandel.clicked(clickPt):
            if 'cLineX' in locals():
                cLineX.undraw()
                cLineY.undraw()

            Zoomed = True
            if Zoomed == True:
                zoomAmount += 0.5

            try: 
                int(entryIterationsMandel.getText()) >= 0
            except:
                entryIterationsMandel.setText(100)
            mandelWin.zoom(whichWay = ZOOM_IN, keepRatio = True)
            mandelbrotPlot(mandelWin, int(entryIterationsMandel.getText()), mandelSlider.getChoice(),
             mandelWin.currentCoords, zoomAmount, mandelClarityVal)
            
            if 'cLineX' in locals():
                cLineX.draw(mandelWin)
                cLineY.draw(mandelWin)


        # zooms out to max frame 
        elif btnZoomOutMandel.clicked(clickPt):
            # UNDRAW C VAL LINES
            if 'cLineX' in locals():
                cLineX.undraw()
                cLineY.undraw()

            Zoomed = False
            zoomAmount = 1
            try: 
                int(entryIterationsMandel.getText()) >= 0
            except:
                entryIterationsMandel.setText(100)
            mandelWin.zoom(whichWay = ZOOM_OUT, keepRatio = True)
            mandelbrotPlot(mandelWin, int(entryIterationsMandel.getText()), mandelSlider.getChoice(),
            mandelWin.currentCoords, 1, mandelClarityVal)

            # REDRAW THE C VAL LINES
            if 'cLineX' in locals():
                cLineX.draw(mandelWin)
                cLineY.draw(mandelWin)

        elif btnZoomInJulia.clicked(clickPt):
            Zoomed_Julia = True
            if Zoomed_Julia == True:
                zoomAmountJulia += 0.5
            juliaWin.zoom(whichWay = ZOOM_IN, keepRatio = True)
            try: 
                int(entryIterationsJulia.getText()) >= 0
            except:
                entryIterationsJulia.setText(100)
            juliaPlot(juliaWin, int(entryIterationsJulia.getText()), juliaSlider.getChoice(),
            complex(ptC.getX(), ptC.getY()), juliaWin.currentCoords, zoomAmountJulia, juliaClarityVal)

        elif btnZoomOutJulia.clicked(clickPt):
            zoomAmountJulia = 1
            juliaWin.zoom(whichWay = ZOOM_OUT, keepRatio = True)

            try: 
                int(entryIterationsJulia.getText()) >= 0
            except:
                entryIterationsJulia.setText(100)
            juliaPlot(juliaWin, int(entryIterationsJulia.getText()), juliaSlider.getChoice(),
            complex(ptC.getX(), ptC.getY()), juliaWin.currentCoords, 1, juliaClarityVal)

        # calls the instructWin function to display instructions for the mandelbrot set
        elif btnInstructions.clicked(clickPt):
            instructWinCall("This is the mandelbrot set window ->", 12, 350, 150)
            instructWinCall("This will change how many times z^2 + c is iterated ->", 9, 350, 425)
            instructWinCall("This will make the image more or less clear ->", 11, 350, 500)
            instructWinCall("This will change the colors and/or algorithm for the image->", 10, 350, 590)
            instructWinCall("These buttons allow you to zoom in and out of the mandelbrot->", 9, 350, 650)
            instructWinCall("This button will graph the mandelbrot set ->", 11, 350, 725)
            instructWinCall("<- Everything else is the same on this side except get C", 10, -850, 550)
            instructWinCall("<- Press the Get C button and click the mandelbrot to get a C val", 8, -850, 650)
            instructWinCall("First try graphing the mandelbrot set -> ", 11, 350, 725)

        clickPt = controlWin.getMouse()
    # if the error popup from c value is open  close it as well


    mandelWin.close()
    controlWin.close()
    juliaWin.close()
    headerWin.close()

main()