#-------------------------------------------------------------------------------
# Name:        hellrungj
# Purpose:
#
# Author:      hellrungj
#
# Created:     26/04/2014
# Copyright:   (c) hellrungj 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import turtle
import Tkinter
import sys
import random
import time
#===============================================================================
def left():
    Whale.setheading(0)
    Whale.backward(10)
    Events += 1
    GameStater(Plankton)
    global Events
    print Events
def right():
    Whale.setheading(0)
    Whale.forward(10)
    Events += 1
    GameStater(Plankton)
    global Events
    print Events
def Up():
    Whale.setheading(90)
    Whale.forward(10)
    Events += 1
    GameStater(Plankton)
    global Events
    print Events
def Down():
    Whale.setheading(270)
    Whale.forward(10)
    Events += 1
    GameStater(Plankton)
    global Events
    print Events
def Instructions():
    """Show the user the instructions"""
    display.setpos(0,170)
    display.write('Instructions',move=False,align='center',font=("Arial",30,("bold","normal")))
    display.setpos(0,100)
    display.write('''The goal of the game is live as long as you can
    without being killed by the Ekskamos.''',move=False,align='center',font=("Arial",15,("bold","normal")))
    display.setpos(0,50)
    display.write('Push the any arrow keys to begin.',move=False,align='center',font=("Arial",15,("bold","normal")))
    display.setpos(0,0)
    display.write('This message will last for 5 seconds.',move=False,align='center',font=("Arial",15,("bold","normal")))
    time.sleep(5)
    display.clear()
def Quit():
    GameStart.bye()
    sys.exit()
#===============================================================================
#Start and Finnish functions
def GameOver():
    """Game over! Displays game over and quits."""
    Display_Game_Over(display)
    time.sleep(5)
    Quit()
def Display_Game_Over(display):
    """Displays a GameOver Screen"""
    display.clear()
    display.setpos(0,100)
    display.write('GAME OVER',move=False,align='center',font=("Arial",50,("bold","normal")))
    display.setpos(0,50)
    display.write('Thank You for Playing.',move=False,align='center',font=("Arial",30,("bold","normal")))
    display.setpos(0,0)
    display.write('Score: '+str(Score),move=False,align='center',font=("Arial",30,("bold","normal")))
def StartScreen(display):
    """The the game with start screen"""
    if Events == 0:
        display.setpos(0,170)
        display.write('Welcome to Whale Game',move=False,align='center',font=("Arial",30,("bold","normal")))
        display.setpos(0,100)
        display.write('''The goal of the game is live as long as you can
        without being killed by the Ekskamos.''',move=False,align='center',font=("Arial",15,("bold","normal")))
        display.setpos(0,50)
        display.write('Push the any arrow keys to begin.',move=False,align='center',font=("Arial",15,("bold","normal")))
        display.setpos(0,0)
        display.write('Have fun.',move=False,align='center',font=("Arial",15,("bold","normal")))
    else:
        display.clear()
def GameStater(Plankton):
    """Starts the game"""
    StartScreen(display)
    time.sleep(0.2)
    if hit_by_Eskamos(Whale,Eskamo1) == True:
        print "GameOver"
        GameOver()
    elif hit_by_Eskamos(Whale,Eskamo2) == True:
        print "GameOver"
        GameOver()
    if hit_by_Eskamos(Whale,Eskamo3) == True:
        print "GameOver"
        GameOver()
    elif Plankton_has_been_hit(Plankton, Whale) == True:
        global Score
        Plankton.clear()
        Plankton.setposition(random.randrange(-230,230), random.randrange(-230,230))
        Score += 1
        print "Your Score is " + str(Score)
        return Score
    elif Hit_by_iceberg(Iceberg1, Eskamo1) == True:
        Eskamo.clear()
#===============================================================================
def move_Eskamos(E):
    E.forward(10)
    E.left(45)
    E.forward(10)
#===============================================================================
#Hit functions
def hit_by_Eskamos(Whale, E):
    """The Whale is by Eskamo"""
    xdistance = Whale.xcor() - E.xcor()
    ydistance = Whale.ycor() - E.ycor()
    if abs(xdistance) <= 20 and abs(ydistance) <= 20:
        return True
    else:
        return False

def Plankton_has_been_hit(Plankton, Whale):
    """The Plankton is by hit by the Whale"""
    xdistance = Whale.xcor() - Plankton.xcor()
    ydistance = Whale.ycor() - Plankton.ycor()
    if abs(xdistance) <= 20 and abs(ydistance) <= 20:
        return True
    else:
        return False
def Hit_by_iceberg(I, E):
    """The Eskamo hits a iceberg"""
    xdistance = E.xcor() - I.xcor()
    ydistance = E.ycor() - I.ycor()
    if abs(xdistance) <= 20 and abs(ydistance) <= 20:
        return True
    else:
        return False
#===============================================================================
Events = 0
Score = 0

GameStart = turtle.Screen()
GameStart.setup(500,500)
GameStart.bgcolor("lightblue")

display = turtle.Turtle()
display.penup()
display.hideturtle()

StartScreen(display)

Whale = turtle.Turtle()
Whale.color("yellow")
Whale.shape("square")
Whale.penup()

Eskamo1 = turtle.Turtle()
Eskamo1.color("red")
Eskamo1.shape("arrow")
Eskamo1.penup()

Eskamo2 = turtle.Turtle()
Eskamo2.color("red")
Eskamo2.shape("arrow")
Eskamo2.penup()

Eskamo3 = turtle.Turtle()
Eskamo3.color("red")
Eskamo3.shape("arrow")
Eskamo3.penup()

Eskamo4 = turtle.Turtle()
Eskamo4.color("red")
Eskamo4.shape("arrow")
Eskamo4.penup()

Eskamo5 = turtle.Turtle()
Eskamo5.color("red")
Eskamo5.shape("arrow")
Eskamo5.penup()

Eskamo6 = turtle.Turtle()
Eskamo6.color("red")
Eskamo6.shape("arrow")
Eskamo6.penup()

Eskamo7 = turtle.Turtle()
Eskamo7.color("red")
Eskamo7.shape("arrow")
Eskamo7.penup()

Eskamo8 = turtle.Turtle()
Eskamo8.color("red")
Eskamo8.shape("arrow")
Eskamo8.penup()

Eskamo1.setpos(-200,190)
Eskamo1.right(45)

Eskamo2.setpos(-190,200)
Eskamo2.right(45)

Eskamo3.setpos(200,-190)
Eskamo3.right(225)

Eskamo4.setpos(190,-200)
Eskamo4.right(225)

Eskamo5.setpos(-200,-190)
Eskamo5.left(45)

Eskamo6.setpos(-190,-200)
Eskamo6.left(45)

Eskamo7.setpos(200,190)
Eskamo7.left(225)

Eskamo8.setpos(190,200)
Eskamo8.left(225)

Plankton = turtle.Turtle()
Plankton.color("green")
Plankton.shape("circle")
Plankton.penup()
Plankton.setposition(random.randrange(-230,230), random.randrange(-230,230))

Iceberg1 = turtle.Turtle()
Iceberg1.penup()
Iceberg1.shape("arrow")
Iceberg1.color("White")
Iceberg1.left(90)

Iceberg2 = turtle.Turtle()
Iceberg2.penup()
Iceberg2.shape("arrow")
Iceberg2.color("White")
Iceberg2.left(90)

Iceberg3 = turtle.Turtle()
Iceberg3.penup()
Iceberg3.shape("arrow")
Iceberg3.color("White")
Iceberg3.left(90)

Iceberg4 = turtle.Turtle()
Iceberg4.penup()
Iceberg4.shape("arrow")
Iceberg4.color("White")
Iceberg4.left(90)

Iceberg5 = turtle.Turtle()
Iceberg5.penup()
Iceberg5.shape("arrow")
Iceberg5.color("White")
Iceberg5.left(90)

Iceberg6 = turtle.Turtle()
Iceberg6.penup()
Iceberg6.shape("arrow")
Iceberg6.color("White")
Iceberg6.left(90)

Iceberg7 = turtle.Turtle()
Iceberg7.penup()
Iceberg7.shape("arrow")
Iceberg7.color("White")
Iceberg7.left(90)

Iceberg8 = turtle.Turtle()
Iceberg8.penup()
Iceberg8.shape("arrow")
Iceberg8.color("White")
Iceberg8.left(90)

Iceberg9 = turtle.Turtle()
Iceberg9.penup()
Iceberg9.shape("arrow")
Iceberg9.color("White")
Iceberg9.left(90)

Iceberg10 = turtle.Turtle()
Iceberg10.penup()
Iceberg10.shape("arrow")
Iceberg10.color("White")
Iceberg10.left(90)

Iceberg11 = turtle.Turtle()
Iceberg11.penup()
Iceberg11.shape("arrow")
Iceberg11.color("White")
Iceberg11.left(90)

Iceberg12 = turtle.Turtle()
Iceberg12.penup()
Iceberg12.shape("arrow")
Iceberg12.color("White")
Iceberg12.left(90)

Iceberg1.setpos(-70,50)
Iceberg2.setpos(-60,40)
Iceberg3.setpos(-60,60)

Iceberg4.setpos(70,-50)
Iceberg5.setpos(60,-40)
Iceberg6.setpos(60,-60)

Iceberg7.setpos(-70,-50)
Iceberg8.setpos(-60,-40)
Iceberg9.setpos(-60,-60)

Iceberg10.setpos(70,50)
Iceberg11.setpos(60,40)
Iceberg12.setpos(60,60)

#===============================================================================
#===============================================================================

GameStart.onkey(Instructions, "?")
GameStart.onkey(Up, "Up")
GameStart.onkey(left, "Left")
GameStart.onkey(right, "Right")
GameStart.onkey(Down, "Down")
GameStart.onkey(Quit, "q")

GameStart.listen()
Tkinter.mainloop()