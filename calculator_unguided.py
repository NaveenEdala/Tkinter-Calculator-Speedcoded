from tkinter import *

# Basic Window Configs
root = Tk()
root.title("Calculator")
root.configure(background="#363636")
root.maxsize(600, 460)

# Text containers for input and output labels. 
# The user will send input using buttons, so we need to display inputted and outputted content.
inputtext = ""
outputtext = ""

# Reusable functions to update input and output areas
def inputarea():
    global inputlabel
    global inputtext
    inputlabel = Label(root, text=inputtext, font="Helvetica 15", bg="#363636", fg="white")
    inputlabel.grid(row=0, columnspan=5, sticky="W")

def outputarea():
    global outputlabel
    global outputtext
    outputlabel = Label(root, text=outputtext, font="Calibri 50", bg="#363636", fg="white")
    outputlabel.grid(row=1, columnspan=5, sticky="W")

# Initialization of input and output areas
inputarea()
outputarea()

# Function to collect inputs from button and append to input data stream, and update display
def inpclick(i):
    global inputlabel
    inputlabel.destroy()
    global inputtext
    inputtext += i
    inputarea()
    resultout()

# Function Defining the DELETE button logic, and display update
def deleteprev():
    global inputlabel
    inputlabel.destroy()
    global inputtext
    inputtext = inputtext[:-1]
    inputarea()
    resultout()

# Function Defining the EQUAL button logic, Result calculation logic, and display update
def resultout():
    global outputlabel
    outputlabel.destroy()
    global outputtext
    global inputtext
    try:
        if (inputtext == ""):
            outputtext = ""
        else:
            outputtext = round(eval(inputtext), 15)
    except:
        outputtext = "ERR"
    outputarea()

# Function Defining the CLEAR button logic, and display reset
def clearall():
    global inputlabel
    inputlabel.destroy()
    global inputtext
    inputtext = ""
    inputarea()
    resultout()
    

"""

The plan of the layout grid. 6 Rows, 5 Columns.

+----------------------+
|      Input Label     |
+----------------------+
|      Output Label    |
+---+---+----+---+-----+
| 7 | 8 | 9  | / | DEL |
+---+---+----+---+-----+
| 4 | 5 | 6  | * | CLR |
+---+---+----+---+-----+
| 1 | 2 | 3  | + |     |
+---+---+----+---+-----+
| 0 | . | 00 | - |  =  |
+---+---+----+---+-----+

"""

# Button placement according to above grid

numSeven = Button(root, text=7, width=10, font="10", height=3, command = lambda: inpclick("7"))
numSeven.grid(row=2, column=0)

numEight = Button(root, text=8, width=10, font="10", height=3, command = lambda: inpclick("8"))
numEight.grid(row=2, column=1)

numNine = Button(root, text=9, width=10, font="10", height=3, command = lambda: inpclick("9"))
numNine.grid(row=2, column=2)

numFour = Button(root, text=4, width=10, font="10", height=3, command = lambda: inpclick("4"))
numFour.grid(row=3, column=0)

numFive = Button(root, text=5, width=10, font="10", height=3, command = lambda: inpclick("5"))
numFive.grid(row=3, column=1)

numSix = Button(root, text=6, width=10, font="10", height=3, command = lambda: inpclick("6"))
numSix.grid(row=3, column=2)

numOne = Button(root, text=1, width=10, font="10", height=3, command = lambda: inpclick("1"))
numOne.grid(row=4, column=0)

numTwo = Button(root, text=2, width=10, font="10", height=3, command = lambda: inpclick("2"))
numTwo.grid(row=4, column=1)

numThree = Button(root, text=3, width=10, font="10", height=3, command = lambda: inpclick("3"))
numThree.grid(row=4, column=2)

numZero = Button(root, text=0, width=10, font="10", height=3, command = lambda: inpclick("0"))
numZero.grid(row=5, column=0)

doubleZero = Button(root, text="00", width=10, font="10", height=3, command = lambda: inpclick("00"))
doubleZero.grid(row=5, column=2)

decimalPoint = Button(root, text=".", width=10, font="10", height=3, command = lambda: inpclick("."))
decimalPoint.grid(row=5, column=1)

plusSign = Button(root, text="+", width=10, font="10", height=3, command = lambda: inpclick("+"))
plusSign.grid(row=4, column=3)

minusSign = Button(root, text="-", width=10, font="10", height=3, command = lambda: inpclick("-"))
minusSign.grid(row=5, column=3)

divSign = Button(root, text="/", width=10, font="10", height=3, command = lambda: inpclick("/"))
divSign.grid(row=2, column=3)

mulSign = Button(root, text="*", width=10, font="10", height=3, command = lambda: inpclick("*"))
mulSign.grid(row=3, column=3)

backspace = Button(root, text="DEL", width=10, font="10", height=3, command = deleteprev)
backspace.grid(row=2, column=4)

equalSign = Button(root, text="=", width=10, font="10", height=3, command = resultout)
equalSign.grid(row=5, column=4)

clear = Button(root, text="CLR", width=10, font="10", height=3, command = clearall)
clear.grid(row=3, column=4)

# Disabled button to fill empty space
disabled = Button(root, text="", width=10, font="10", height=3, bg="grey", state=DISABLED)
disabled.grid(row=4, column=4)


# Main loop for window
root.mainloop()