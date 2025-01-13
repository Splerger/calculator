#import modules
import tkinter as tk
from tkinter import messagebox

import os
import sys

#define width and height for window
width = 250
height = 375

#create window
window = tk.Tk()
window.geometry(f"{width}x{height}")
window.minsize(width,height)
window.title("Calculator")

#set window icon
if getattr(sys, 'frozen', False):  #Check if running in a PyInstaller bundle
    #Use the temporary directory created by PyInstaller
    icon_path = os.path.join(sys._MEIPASS, 'icon.ico')
else:
    #Use the regular path for development
    icon_path = 'icon.ico'

window.iconbitmap(icon_path)

#global variables
numberString1 = ""
numberString2 = ""
result = 0
calculated = False
mode = ""

#label to display numbers
label = tk.Label(window, text=f"{numberString1}{mode}")
label.place(x=20, y=20)

#define addNumber function
def addNumber(number):
    global numberString1
    global numberString2
    global mode
    global calculated

    #check if calculated is True
    if calculated:
        #clear results and set calculated to False
        clear()
        calculated = False

    #check if the mode isn't defined yet to determine what field you are trying to type in
    if mode == "":
        #if the first thing is empty and the input is a .
        if numberString1 == "" and number != ".":
            #replace numberString1 with the next inputted number
            numberString1 = str(number)
            label.config(text=f"{numberString1}{mode}")
        else:
            #if the last char of numberString1 is . and the next inputted number is also a . do nothing
            if numberString1[-1] == "." and number == ".":
                return
            else:
                numberString1 += str(number)
                label.config(text=f"{numberString1}{mode}")
    else:
        #if numberString2 is empty and the inputted number is a . 
        if numberString2 == "" and number != ".":
            #replace numberString2 with the next inputted number
            numberString2 = str(number)
            label.config(text=f"{numberString1}{mode}{numberString2}")
        else:
            #if the last char of numberString2 is . and the next inputted number is also a . do nothing
            if numberString2[-1] == "." and number == ".":
                return
            else:
                numberString2 += str(number)
                label.config(text=f"{numberString1}{mode}{numberString2}")

#define addAnswer function
def addAnswer():
    global numberString1
    global numberString2
    global mode
    global result

    #check if result is zero
    if result != 0:
        addNumber(result)
        
    
#define setMode function
def setMode(newMode):
    global mode
    mode = newMode
    label.config(text=f"{numberString1}{mode}{numberString2}")
    

#define equal function
def equal():
    global numberString1
    global numberString2
    global result
    global mode
    global calculated

    #check if the mode is nothing
    if mode == "": 
        return

    #check if either of the input strings are nothing
    if numberString1 == "" or numberString2 == "":
        return

    #determine the correct mathematical operation depending on the mode variable 
    match mode:
        case "+":
            result = float(numberString1) + float(numberString2)
            calculated = True
        case "-":
            result = float(numberString1) - float(numberString2)
            calculated = True
        case "*":
            result = float(numberString1) * float(numberString2)
            calculated = True
        case "/":
            result = float(numberString1) / float(numberString2)
            calculated = True
        case _:
            return

    #remove extra .0 at end of result
    if result.is_integer():
        result = int(result)

    #if result is longer than 10 characters format to scientific notation
    if len(str(result)) > 10:
        label.config(text=f"{format(result, '.2e')}")
    else:
        label.config(text=f"{numberString1}{mode}{numberString2} = {result}")

#define clear function
def clear():
    global numberString1
    global numberString2
    global mode
    numberString1 = ""
    numberString2 = ""
    mode = ""
    label.config(text=f"{numberString1}{mode}")
    
#define clearMost function
def clearMost():
    global numberString1
    global numberString2
    global mode
    numberString2 = ""
    label.config(text=f"{numberString1}{mode}")
    
#define removeOne function
def removeOne():
    global numberString1
    global numberString2
    global mode
    #check if mode is empty
    if mode == "":
        #remove last character of numberString1
        numberString1 = numberString1[:-1]
        label.config(text=f"{numberString1}{mode}")
    else:
        #remove last character of numberString2
        numberString2 = numberString2[:-1]
        #if numberString2 is empty reset mode 
        if numberString2 == "":
            mode = ""
        label.config(text=f"{numberString1}{mode}{numberString2}")

#define keyHandler function
def keyHandler(event):
    match event.char:
        case "1" | "2" | "3" | "4" | "4" | "5" | "6" | "7" | "8" | "9" | "0":
            addNumber(int(event.char))
        case "+" | "-" | "*" | "/":
            setMode(event.char)
        case "\r" | "=":
            equal()
        case ".":
            addNumber(".")
        case "c":
            clear()
        case _:
            return

#define close function
def close(event):
    #ask user if they want to quit
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        window.destroy()

#setup keybinds
window.bind("<BackSpace>", lambda _: removeOne())
window.bind("<Escape>", close)
window.bind("<Key>", keyHandler)

#define row positions
firstRow = 75
secondRow = 135
thirdRow = 195
fourthRow = 255
fithRow = 315

#define collum positions
firstCol = 20
secondCol = 70
thirdCol = 120
fourthCol = 170

#define buttons
clearButton = tk.Button(window, text="C", width = 5, height = 3, command = lambda: clear())
clearMostButton = tk.Button(window, text="CE", width = 5, height = 3, command = lambda: clearMost())
answerButton = tk.Button(window, text="Ans", width = 5, height = 3, command = lambda: addAnswer())
removeOneButton = tk.Button(window, text="⌫", width = 5, height = 3, command = lambda: removeOne())

oneButton = tk.Button(window, text="1", width = 5, height = 3, command = lambda: addNumber(1))
twoButton = tk.Button(window, text="2", width = 5, height = 3, command = lambda: addNumber(2))
threeButton = tk.Button(window, text="3", width = 5, height = 3, command = lambda: addNumber(3))

fourButton = tk.Button(window, text="4", width = 5, height = 3, command = lambda: addNumber(4))
fiveButton = tk.Button(window, text="5", width = 5, height = 3, command = lambda: addNumber(5))
sixButton = tk.Button(window, text="6", width = 5, height = 3, command = lambda: addNumber(6))

sevenButton = tk.Button(window, text="7", width = 5, height = 3, command = lambda: addNumber(7))
eightButton = tk.Button(window, text="8", width = 5, height = 3, command = lambda: addNumber(8))
nineButton = tk.Button(window, text="9", width = 5, height = 3, command = lambda: addNumber(9))

zeroButton = tk.Button(window, text="0", width = 5, height = 3, command = lambda: addNumber(0))
decimalButton = tk.Button(window, text=".", width = 5, height = 3, command = lambda: addNumber("."))
equalButton = tk.Button(window, text="=", width = 5, height = 3, command = lambda: equal())

addButton = tk.Button(window, text="+", width = 5, height = 3, command = lambda: setMode("+"))
subtractButton = tk.Button(window, text="-", width = 5, height = 3, command = lambda: setMode("-"))
multiplyButton = tk.Button(window, text="*", width = 5, height = 3, command = lambda: setMode("*"))
divideButton = tk.Button(window, text="/", width = 5, height = 3, command = lambda: setMode("/"))

#place buttons
clearButton.place(x=firstCol, y=firstRow)
clearMostButton.place(x=secondCol, y=firstRow)
answerButton.place(x=thirdCol, y=firstRow)
removeOneButton.place(x=fourthCol, y=firstRow)

oneButton.place(x=firstCol, y=secondRow)
twoButton.place(x=secondCol, y=secondRow)
threeButton.place(x=thirdCol, y=secondRow)
addButton.place(x=fourthCol, y=secondRow)

fourButton.place(x=firstCol, y=thirdRow)
fiveButton.place(x=secondCol, y=thirdRow)
sixButton.place(x=thirdCol, y=thirdRow)
subtractButton.place(x=fourthCol, y=thirdRow)

sevenButton.place(x=firstCol, y=fourthRow)
eightButton.place(x=secondCol, y=fourthRow)
nineButton.place(x=thirdCol, y=fourthRow)
multiplyButton.place(x=fourthCol, y=fourthRow)

zeroButton.place(x=secondCol, y=fithRow)
decimalButton.place(x=firstCol, y=fithRow)
equalButton.place(x=thirdCol, y=fithRow)
divideButton.place(x=fourthCol, y=fithRow)

#start main loop
tk.mainloop()
