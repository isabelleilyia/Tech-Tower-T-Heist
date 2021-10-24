# Hackathon 2021

# import tkinter -  allows us to create a GUI
from tkinter import *
import time
import random
import sys

i=True

# create a window, give it a title, define it's size, make it non resizeable
root = Tk()
root.title("The Tech Tower \'T\' Heist!")
root.geometry("850x600")
root.resizable(False,False)

###########################################################################

# define, lay a label for, and place the background image
background = PhotoImage(file = "Images/background.ppm")
backgroundLabel = Label(image = background, width = 850, height=600)
backgroundLabel.place(relx=0.5,rely=0.5,anchor=CENTER)

# define, lay a label for, and place logo image
logo = PhotoImage(file="Images/logo.ppm") 
logoLabel = Label(image=logo, width = 604, height = 190)
logoLabel.place(relx = 0.5, rely= 0.4, anchor=CENTER)


###########################################################################
#Toolbar and Toolbar items
###########################################################################
toolbar = PhotoImage(file="Images/toolbar.ppm")
toolbarLabel = Label(image=toolbar, width=416, height=31)

rope = PhotoImage(file="Images/rope.ppm")
ropeLabel = Label(image=rope, width=31, height=31)

wig = PhotoImage(file="Images/wig.ppm")
wigLabel = Label(image=wig, width=31, height=31)

flagpole = PhotoImage(file="Images/flagpole.ppm")
flagpoleLabel = Label(image=flagpole, width=31, height=31)

yogamat = PhotoImage(file="Images/yogamat.ppm")
yogamatLabel = Label(image=yogamat, width=31, height=31)

wig = PhotoImage(file="Images/wig.ppm")
wigLabel = Label(image=wig, width=31, height=31)

book = PhotoImage(file="Images/book.ppm")
bookLabel = Label(image=book, width=31, height=31)

football = PhotoImage(file="Images/football.ppm")
footballLabel = Label(image=football, width=31, height=31)

goggles = PhotoImage(file="Images/goggles.ppm")
gogglesLabel = Label(image=goggles, width=31, height=31)

key = PhotoImage(file="Images/key.ppm")
keyLabel = Label(image=key, width=31, height=31)

##ropeLabel.place(x = 215,rely=0.13,anchor=W)
##bookLabel.place(x = 270,rely=0.13,anchor=W)
##flagpoleLabel.place(x = 325,rely=0.13,anchor=W)
##footballLabel.place(x = 380,rely=0.13,anchor=W)
##gogglesLabel.place(x = 435,rely=0.13,anchor=W)
##keyLabel.place(x = 490,rely=0.13,anchor=W)
##wigLabel.place(x = 545,rely=0.13,anchor=W)
##yogamatLabel.place(x = 600,rely=0.13,anchor=W)


      
# define and place a 'start' button, alongside startgame function that runs the game

def startgame():
    logoLabel.destroy()
    startButton.destroy()
    e.place(relx = 0.5, rely = 0.85, anchor=CENTER,)
    telephone()
    
startButton = Button(root, text = "Start!", font = ("Roman",30,), command = startgame)
startButton.place(relx=0.5,rely=0.7,anchor=CENTER)
e = Entry(root,width=30, borderwidth=5, highlightbackground="lime",font=("Ayuthaya",15,"bold"))

###########################################################################

# Setting Up

###########################################################################

# PRINTLINE FUNCTION AND SUBFUNCTIONS- PRINTS TEXT LETTER BY LETTER

def printLine(text):
    global label
    try:
        label.destroy()
    except:
        pass
    label = Label(root, bg= "black", fg="lime", font =("Ayuthaya",18, "bold"), justify = CENTER)
    label.string = (text)
    label.place(relx = 0.5,rely=0.665, anchor=N) 
    update_label_letters()

def printLineUp(text):
    global label
    try:
        label.destroy()
    except:
        pass
    label = Label(root, bg= "black", fg="lime", font =("Ayuthaya",18, "bold"), justify = CENTER)
    label.string = (text)
    label.place(relx = 0.5,rely=0.2, anchor=N) 
    update_label_letters()
    
def update_label_letters():
    global label
    _last_char_index = 0
    _last_char_index = len(label['text'])
    if _last_char_index < len(label.string):
        label['text'] += label.string[_last_char_index] 
    else:
        return "Blank"
    label.after(30, update_label_letters)

###########################################################################

# Function that acts everytime user presses enter. Function will then direct the answer
# back to the original function using several if statements. 'relevant' variable
# informs us of which function we were operating it.

relevant = "blank"  
choice = ""  # filler values to prevent errors

def func(event):
    global relevant, e, choice
    choice = e.get().lower().strip()
    e.delete(0, 'end')
    if relevant == "telephone":
        telephone()
    if relevant == "techGreen1":
        techGreen1()
    if relevant == "techGreen2":
        techGreen2()
    if relevant =="techGreen3":
        techGreen3()
    if relevant == "mid":
        mid()
    if relevant == "klaus":
        klaus()
    if relevant == "klausQ1":
        klausQ1()
    if relevant == "klausQ2":
        klausQ2()
    if relevant == "klausQ3":
        klausQ3()
    if relevant == "klausWrong":
        klausWrong()
    if relevant == "klausVictory":
        klausVictory()
    if relevant == "culc":
        culc()

root.bind("<Return>",func) # binds enter key to func()

###########################################################################

# STAGE 1 : TELEPHONE

currentImage = PhotoImage(file = "Images/telephone1.ppm")
currentImageLabel = Label(image=currentImage, width = 550, height = 280, bg="black")
energy_points = 8

def telephone():
    global choice, label,relevant
    currentImageLabel.place(relx = 0.5, rely=  0.41, anchor = CENTER)
    relevant = "telephone"
    printLine("You awaken to the ring of the telephone. \n Do you pick up or ignore?")
    if choice == "pick up" or choice =="yes" or choice == "y":
        techGreen1()

locations_east = ["Bobby Dodd", "Sorority House", "Towers", "Tech Green"]
locations_west = ["Burger Bowl", "Flag Building", "CRC", "Tech Green"]
locations_mid = ["Klaus", "CULC", "Tech Green"]


def techGreen1():
    global choice, label, relevant
    relevant = "techGreen1"
    printLine("You have been brought to Tech Green. Your goal is to\nsteal the 'T' from Tech Tower. Enter 'Y' if you understand.")
    currentImage.configure(file = "Images/techgreen.ppm")
    if choice == "y":
        techGreen2()

def techGreen2():
    global choice, label, relevant
    relevant = "techGreen2"
    currentImage.configure(file = "Images/black.ppm")
    printLineUp("Here are some things to keep in mind:\n\n1. You must go around campus collecting items\nin order to pull off this heist.\n\n2. Whenever you arrive at a new location, you may\neither press enter to explore said location, or\ntype 'Tech Tower' to attempt the heist.\n\n3. You must have all items in order to pull off\nthe heist. If you don't have them,\nCabrera will catch you! \n\nPress enter once you're ready to continue.")
    if choice == "":
        techGreen3()

def techGreen3():
    global choice, label, relevant
    relevant = "techGreen3"
    toolbarLabel.place(rely=0.13, relx=0.5,anchor=CENTER)
    currentImage.configure(file = "Images/techgreen.ppm")
    printLine("You can now choose to go to east campus, west campus,\nor stay on mid-campus\nEnter 'East', 'West', or 'Mid' to make your choice.")
    if choice == "east":
        east()
    if choice == "west":
        west()
    if choice == "mid":
        mid()

klausValue = 1
culcValue = 1
def mid():
    global choice, label, relevant, klausValue, culcValue
    relevant = "mid"
    currentImage.configure(file = "Images/mid.ppm")
    printLine("You can go to the following locations:\n" + "Tech Green,"+ " Klaus, "*klausValue + " Culc,"*culcValue +"\nType the location you would like to visit next.")
    if choice == "tech green":
        techGreen3()
    if choice == "klaus" and klausValue ==1:
        klaus()
    elif choice == "culc" and culcValue ==1:
        culc()

def klaus():
    global choice, label, relevant, klausValue
    relevant = "klaus"
    currentImage.configure(file = "Images/klaus.ppm")
    printLine("Welcome to the Klaus Center for Advanced Computing!\nIf you want to succeed at Georgia Tech, you must be able\nto code (even as a business major). Press enter to continue.")
    if choice == "":
        klausQ1()

def klausQ1():
    global choice, label, relevant
    relevant = "klausQ1"
    currentImage.configure(file = "Images/black.ppm")
    printLineUp("Here's a short three question quiz to test your\nknowledge of Python.\n\n\nQuestion 1: Write a line of code that prints\n'yellow jackets' to the console, without\nthe apostrophes.\n\nWrite you answer in the box below.")
    if choice == "print(\"yellow jackets\")":
        klausQ2()
    elif choice != "" and choice != "print(\"yellow jackets\")":
        klausWrong()

def klausWrong():
    global choice, label, relevant
    relevant = "klausWrong"
    currentImage.configure(file="Images/klausWrong.ppm")
    printLine("Oops, you didn't pass the quiz.\nHopefully you aren't considering a computer science degree!\nType 'try again' to give it another go, or 'Mid' to exit.")
    if choice == "try again":
        klaus()
    elif choice == "mid":
        mid()


def klausQ2():
    global choice, label, relevant
    relevant = "klausQ2"
    currentImage.configure(file = "Images/black.ppm")
    printLineUp("Nice job!\n\n\nQuestion 2: What is the output of the following code?\n for i in range (10,0,-2):\n\tprint(i)\n\nSeperate lines by a spacebar.\nWrite you answer in the box below.")
    if choice == "10 8 6 4 2":
        klausQ3()
    elif choice != "10 8 6 4 2" and choice != "print(\"yellow jackets\")":
        klausWrong()

def klausQ3():
    global choice, label, relevant
    relevant = "klausQ3"
    currentImage.configure(file = "Images/black.ppm")
    printLineUp("You're on a streak! Keep it up!\nJust one last question left!\n\nQuestion 3: What is printed by the following code?\na=True\nb=False\nc=False\nif a or b and c:\n\t\t\tprint(\"victory\")")
    if choice == "victory":
        klausVictory()
    if choice != "10 8 6 4 2" and choice !="victory":
        klausWrong()

def klausVictory():
    global choice, label, relevant, klausValue
    relevant = "klausVictory"
    gogglesLabel.place(x = 435,rely=0.13,anchor=W)
    klausValue = 0
    currentImage.configure(file = "Images/klaus.ppm")
    printLine("WOW! Congrats on acing that test. As a reward, your professor\ngave you a pair of night vision goggles. These'll surely\nbe helpful for stealing the Tech Tower T...")
    if choice == "":
        mid()

def culc():
    global choice, label, relevant
    relevant = "culc"
    currentImage.configure(file = "Images/culc.ppm")
    printLine("Sorry! The CULC is under renovation currently. Come back later!")
    if choice == "":
        mid()

#def culc():
   # global choice, label, relevant
    #relevant = "culc"
    #currentImage.configure(file = "Images/culc.ppm")
    #printLine("Sorry! The CULC is under renovation currently. Come back later!")
    #if choice == "":
       # mid()





# end bit of code
root.mainloop()
