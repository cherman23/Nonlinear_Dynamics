import sys
sys.path.append('../lib')
from DEgraphics_Herman import *
from transform import * 
from math import *
import random 

ScreenHorizontal = 1440
ScreenVertical = 900
global transList 
transList = []
# INITIAL VALUE IS GIVEN SO LIST IS NOT EMPTY
transList.append(IFS_Transform(0.5, 0.5, 0, 0, 0, 0, 1, 'black'))

def plot(w, iterations):
    global transList
    n = Point(random.uniform(-1,1), random.uniform(-1,1))
    for i in range(iterations):
        
        b = random.randint(0,len(transList)-1)
        x,y = transList[b].transformPoint(n.getX(), n.getY())
        w.plot(x, y, transList[b].getColor())
        n = Point(x, y)

def instructWinCall(text, textSize, offsetHoriz, offsetVert):
    # Creates window 
    instructWin = DEGraphWin(defCoords = [-10,-10,10,10], 
                    title ="instructWindow", 
                    width = 350, height = 200,
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

def main():
    global transList
    win = DEGraphWin(defCoords = [-1,-1,1,1], 
                    title ="Main", 
                    width = 500, height = 500,
                    offsets=[ScreenHorizontal/3,ScreenVertical/8],
                    hasTitlebar = False,
                    hThickness=1,)
    
    control = DEGraphWin(defCoords = [-10,-10,10,10], 
                    title ="Main", 
                    width = 500, height = 300,
                    offsets=[ScreenHorizontal/3,ScreenVertical/8+500],
                    hasTitlebar = False,
                    hThickness=1,)
    control.setBackground(color_rgb(110,110,110))

    settings = DEGraphWin(defCoords = [-10,-10,10,10], 
                                title ="IFS LIST", 
                                width = 500, height = 400,
                                offsets=[6000,6000],
                                hasTitlebar = True,
                                hThickness=1,)
    settings.setBackground(color_rgb(210,210,210))
    
    # BUTTONS FOR CONTROL WINDOW 
    btnGraph = Button(control, Point(-2.5,0), width=5, height=2,
                edgeWidth = 2, label = 'Draw',
                buttonColors = ['lightgray', 'black', 'black'],
                clickedColors = ['white', 'red', 'black'],
                font=('courier',11), timeDelay = 0.25)
    btnGraph.activate()

    btnSettings = Button(control, Point(-9.75,9), width=1.5, height=2,
                edgeWidth = 2, label = '⚙︎',
                buttonColors = ['lightgrey', 'black', 'black'],
                clickedColors = ['white', 'red', 'black'],
                font=('courier',11), timeDelay = 0.25)
    btnSettings.activate()

    btnInstruct = Button(control, Point(-8,9), width=1.5, height=2,
                edgeWidth = 2, label = 'ⓘ',
                buttonColors = ['lightgrey', 'black', 'black'],
                clickedColors = ['white', 'red', 'black'],
                font=('courier',11), timeDelay = 0.25)
    btnInstruct.activate()

    btnQuit = Button(control, Point(8,-7), width=1.5, height=2,
                edgeWidth = 2, label = 'Quit',
                buttonColors = ['darkred', 'black', 'black'],
                clickedColors = ['white', 'red', 'black'],
                font=('courier',11), timeDelay = 0.25)
    btnQuit.activate()




    # BUTTONS FOR SETTINGS WINDOW
    btnDelete = Button(settings, Point(7.75, 9.5), width=2, height=2,
                edgeWidth = 2, label = 'Delete',
                buttonColors = ['red', 'black', 'black'],
                clickedColors = ['white', 'red', 'black'],
                font=('courier',11), timeDelay = 0.25)
    btnDelete.activate()

    btnEdit = Button(settings, Point(5.5, 9.5), width=2, height=2,
                edgeWidth = 2, label = 'Edit',
                buttonColors = ['yellow', 'black', 'black'],
                clickedColors = ['white', 'red', 'black'],
                font=('courier',11), timeDelay = 0.25)
    btnEdit.activate()

    btnAdd = Button(settings, Point(3.25, 9.5), width=2, height=2,
                edgeWidth = 2, label = 'Add',
                buttonColors = ['lightgreen', 'black', 'black'],
                clickedColors = ['white', 'red', 'black'],
                font=('courier',11), timeDelay = 0.25)
    btnAdd.activate()

    btnView = Button(settings, Point(1, 9.5), width=2, height=2,
                edgeWidth = 2, label = 'View',
                buttonColors = ['lightblue', 'black', 'black'],
                clickedColors = ['white', 'red', 'black'],
                font=('courier',11), timeDelay = 0.25)
    btnView.activate()

    btnClose = Button(settings, Point(6.5,-7), width=3, height=2,
                edgeWidth = 2, label = 'Close',
                buttonColors = ['darkred', 'black', 'black'],
                clickedColors = ['white', 'red', 'black'],
                font=('courier',11), timeDelay = 0.25)
    btnClose.activate()

    transDrop = DropDown(Point(0,3), choices=["Transformation 1"], bg = 'lightgrey')
    transDrop.draw(settings)

# TEXT AND INPUT FOR SETTINGS: 

    # X SCALE 
    xScale_Text = Text(Point(-8.5,-2), "xScale:")
    xScale_Text.setSize(10)
    xScale_Text.draw(settings)
    xScale_Text.setTextColor("black")

    xScale_Input = Entry(Point(-7, -2), 4)
    xScale_Input.setSize(11)
    xScale_Input.draw(settings)

    # Y SCALE 
    yScale_Text = Text(Point(-5,-2), "yScale:")
    yScale_Text.setSize(10)
    yScale_Text.draw(settings)
    yScale_Text.setTextColor("black")

    yScale_Input = Entry(Point(-3.5, -2), 4)
    yScale_Input.setSize(11)
    yScale_Input.draw(settings)

    # THETA 
    theta_Text = Text(Point(-2,-2), "theta:")
    theta_Text.setSize(10)
    theta_Text.draw(settings)
    theta_Text.setTextColor("black")

    theta_Input = Entry(Point(-0.5, -2), 4)
    theta_Input.setSize(11)
    theta_Input.draw(settings)

    # PHI 
    phi_Text = Text(Point(1,-2), "phi:")
    phi_Text.setSize(10)
    phi_Text.draw(settings)
    phi_Text.setTextColor("black")

    phi_Input = Entry(Point(2, -2), 4)
    phi_Input.setSize(11)
    phi_Input.draw(settings)

    # H
    h_Text = Text(Point(4,-2), "h:")
    h_Text.setSize(10)
    h_Text.draw(settings)
    h_Text.setTextColor("black")

    h_Input = Entry(Point(5, -2), 4)  
    h_Input.setSize(11)
    h_Input.draw(settings)

    # K
    k_Text = Text(Point(7,-2), "k:")
    k_Text.setSize(10)
    k_Text.draw(settings)
    k_Text.setTextColor("black")

    k_Input = Entry(Point(8, -2), 4)
    k_Input.setSize(11)
    k_Input.draw(settings)

    # PROBABILITY
    p_Text = Text(Point(-3.5,-4), "Probability:")
    p_Text.setSize(10)
    p_Text.draw(settings)
    p_Text.setTextColor("black")

    p_Input = Entry(Point(-1.5, -4), 4)
    p_Input.setSize(11)
    p_Input.draw(settings)

    # COLOR
    color_Text = Text(Point(1,-4), "Color:")
    color_Text.setSize(10)
    color_Text.draw(settings)
    color_Text.setTextColor("black")

    color_Input = Entry(Point(2.75, -4), 6)
    color_Input.setSize(11)
    color_Input.draw(settings)


    settingsClicked = False
    clickPt = control.getMouse()
    while not btnQuit.clicked(clickPt):
        if btnGraph.clicked(clickPt):
            win.clear()
            try: 
                plot(win, 10000)
            except:
                instructWinCall("There is an error in the transformations", 10, ScreenHorizontal/3-200, ScreenVertical/8+400)

        if btnInstruct.clicked(clickPt):
            instructWinCall("Click the draw button to draw the fractal. \nClick the settings button to change the transformations. \nClick the quit button to quit the program.", 10, ScreenHorizontal/3-200, ScreenVertical/8+400)
            instructWinCall("Click the add button to add a transformation. \nClick the delete button to delete a transformation. \nClick the edit button to edit a transformation. \nClick the view button to view a transformation. \nClick the close button to close the settings window.", 10, ScreenHorizontal/3-200, ScreenVertical/8+400)
            instructWinCall("Enter the xScale, yScale, theta, \nphi, h, k, probability, and color of the transformation. \nClick the save button to save the transformation after editing", 10, ScreenHorizontal/3-200, ScreenVertical/8+400)


        if btnSettings.clicked(clickPt):
            if settingsClicked == False:
                settings.moveTo(ScreenHorizontal/3+500, ScreenVertical/8, 500, 400)
                settingsClicked = True

            clickPt = settings.getMouse()
            while not btnClose.clicked(clickPt):
                options = 0
                if btnDelete.clicked(clickPt):
                    try: 
                        del transList[transDrop.choices.index(transDrop.getChoice())]
                        transDrop.removeChoice(transDrop.getChoice(), settings, options)

                    except:
                        instructWinCall("You cannot delete all elements of list", 10, ScreenHorizontal/3-200, ScreenVertical/8+400)

                if btnAdd.clicked(clickPt): 
                    try:
                        # CREATE LOCAL VARS FOR INPUT 
                        xScale = float(xScale_Input.getText())
                        yScale = float(yScale_Input.getText())
                        theta = float(theta_Input.getText())
                        phi = float(phi_Input.getText())
                        h = float(h_Input.getText())
                        k = float(k_Input.getText())
                        p = float(p_Input.getText())
                        color = color_Input.getText() 

                        # CREATE TRANSFORMATIONA AND ADD TO LIST
                        newTrans = IFS_Transform(xScale, yScale, theta, phi, h, k, p, color)
                        transList.append(newTrans)
                        transName = "Transformation " + str(len(transList))
                        transDrop.addChoice(transName, settings, options)
                    except:
                        instructWinCall("One of the elements is empty or non-numberic", 10, ScreenHorizontal/3-200, ScreenVertical/8+400)

                if btnEdit.clicked(clickPt):
                    # SHOW CURRENT 
                    currTrans = transDrop.choices.index(transDrop.getChoice())
                    xScale_Input.setText(transList[currTrans].getR())
                    yScale_Input.setText(transList[currTrans].getS())
                    theta_Input.setText(transList[currTrans].getTheta())
                    phi_Input.setText(transList[currTrans].getPhi())
                    h_Input.setText(transList[currTrans].getE())
                    k_Input.setText(transList[currTrans].getF())
                    p_Input.setText(transList[currTrans].getProb())
                    color_Input.setText(transList[currTrans].getColor())
                    # CHANGE BUTTON TO SAVE 
                    btnEdit.setCaption("Save")
                    
                    # Deactivate other buttons while editing so save must be pressed
                    btnDelete.deactivate()
                    btnAdd.deactivate()
                    btnView.deactivate()
                    btnClose.deactivate()

                    clickPt = settings.getMouse()
                    while not btnEdit.clicked(clickPt):
                        clickPt = settings.getMouse()
                    transList[currTrans].setR(float(xScale_Input.getText()))
                    transList[currTrans].setS(float(yScale_Input.getText()))
                    transList[currTrans].setTheta(float(theta_Input.getText()))
                    transList[currTrans].setPhi(float(phi_Input.getText()))
                    transList[currTrans].setHshift(float(h_Input.getText()))
                    transList[currTrans].setVshift(float(k_Input.getText()))
                    transList[currTrans].setProb(float(p_Input.getText()))
                    transList[currTrans].setColor(color_Input.getText())
                    
                    # TURN BUTTONS ON AGAIN AFTER SAVE IS PRESSED 
                    btnView.activate()
                    btnDelete.activate()
                    btnAdd.activate()
                    btnClose.activate()
                    
                    btnEdit.setCaption("Edit")

                if btnView.clicked(clickPt):
                    # SETS INPUTS TO CURRENT VAL
                    currTrans = int(transDrop.getChoice()[-1])-1
                    xScale_Input.setText(transList[currTrans].getR())
                    yScale_Input.setText(transList[currTrans].getS())
                    theta_Input.setText(transList[currTrans].getTheta())
                    phi_Input.setText(transList[currTrans].getPhi())
                    h_Input.setText(transList[currTrans].getE())
                    k_Input.setText(transList[currTrans].getF())
                    p_Input.setText(transList[currTrans].getProb())
                    color_Input.setText(transList[currTrans].getColor())


                clickPt = settings.getMouse()

            # When closed move window back to original off screen position
            settingsClicked = False
            settings.moveTo(6000, 6000, ScreenHorizontal, ScreenVertical)

            

        clickPt = control.getMouse()

    win.close()

main()