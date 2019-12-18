#2019-20 Fall Computer Science Principles Final Exam

#Ms. Haubold

#Name
#Caden Pawlak
#Date
#12-18-19


#### INSTRUCTIONS ####
#Create an etch a sketch turtle game
#The turtle should move with the arrow keys (up, down, left and right), and draw
#Space should clear the screen
#o and p should make the pen size bigger and smaller
#u should pick the pen up or put the pen down
#All code must be commented
import turtle as trtl
# imports turtle
#BONUS
#Add a feature to change colors
#

#import required libraries


#create turtle
Line = trtl.Turtle()
#Creates turtle
Line.goto(0,0)
#Tellsthe turtle where to start
Line.pensize(5)
# changes pensize of turtle to 1
#movement functions
def Up():
    Line.setheading(90)
    Line.forward(10)
# moves turtle up on Up keypress
def Down():
    Line.setheading(270)
    Line.forward(10)
# moves turtle down on Up keypress
def Left():
    Line.setheading(180)
    Line.forward(10)
# moves turtle left on Up keypress
def Right():
    Line.setheading(0)
    Line.forward(1)
# moves turtle right on Up keypress

#color/drawing functions
def clear():
    Line.clear()

def pensizeup():
    Line.pensize(10)
# changes pensize by +5 on O keypress
def pensizedown():
    Line.pensize(1)
# changes pensize by -5 on P keypress
def penup():
    Line.penup()
#Picks up pen on u keypress
def pendown():
    Line.pendown()
#drops pen on U keypress
def green():
    Line.pencolor("green")
    Line.fillcolor("green")
# changes the turtles color to green
def orange():
    Line.pencolor("orange")
    Line.fillcolor("orange")
def yellow():
    Line.pencolor("yellow")
    Line.fillcolor("yellow")

def red():
    Line.pencolor("red")
    Line.fillcolor("red")
#create screen
wn = trtl.Screen()
#Creates screen
#bind to keypresses
wn.onkeypress(Up, "Up")
wn.onkeypress(Down, "Down")
wn.onkeypress(Left,"Left")
wn.onkeypress(Right, "Right")
wn.onkeypress(clear, "space")
wn.onkeypress(pensizeup, "o")
wn.onkeypress(pensizedown, "p")
wn.onkeypress(penup, "u")
wn.onkeypress(pendown, "U")
wn.onkeypress(green, "1")
wn.onkeypress(orange, "2")
wn.onkeypress(yellow, "3")
wn.onkeypress(red, "4")


#tells the turtle on diffrent keypresses what to do

#listen
wn.listen()
#tells window to listen to commands
#mainloop
wn.mainloop()
#Crwates mainloop