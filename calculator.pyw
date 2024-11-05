#import modules
import tkinter as tk
from tkinter import messagebox

import os
import sys

#define width and height for window
width = 250
height = 380

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
    
    fullString = f"{numberString1}{mode}{numberString2}"
    
    if len(fullString) > 30:
        return

    if calculated:
        clear()
        calculated = False
    
    if mode == "":
        if numberString1 == "" and number != ".":
            numberString1 = str(number)
            label.config(text=f"{numberString1}{mode}")
        else:
            if numberString1[-1] == "." and number == ".":
                return
            else:
                numberString1 += str(number)
                label.config(text=f"{numberString1}{mode}")
    else:
        if numberString2 == "" and number != ".":
            numberString2 = str(number)
            label.config(text=f"{numberString1}{mode}{numberString2}")
        else:
            if numberString2[-1] == "." and number == ".":
                return
            else:
                numberString2 += str(number)
                label.config(text=f"{numberString1}{mode}{numberString2}")


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
    
    calculated = True
    
    if mode == "": 
        return

    if numberString1 == "" or numberString2 == "":
        return
    
    match mode:
        case "+":
            result = float(numberString1) + float(numberString2)
        case "-":
            result = float(numberString1) - float(numberString2)
        case "*":
            result = float(numberString1) * float(numberString2)
        case "/":
            result = float(numberString1) / float(numberString2)
        case _:
            return
        
    if result.is_integer():
        result = int(result)
        
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
    if mode == "":
        numberString1 = numberString1[:-1]
        label.config(text=f"{numberString1}{mode}")
    else:
        numberString2 = numberString2[:-1]
        if numberString2 == "":
            mode = ""
        label.config(text=f"{numberString1}{mode}{numberString2}")

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

def close():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        window.destroy()

window.bind("<BackSpace>", lambda _: removeOne())
window.bind("<Escape>", lambda _: close())
window.bind("<Key>", keyHandler)

#define row positions
firstRow = 80
secondRow = 140
thirdRow = 200
fourthRow = 260
fithRow = 320

#define collum positions
firstCol = 20
secondCol = 70
thirdCol = 120
fourthCol = 170

#define buttons
clearButton = tk.Button(window, text="C", width = 5, height = 3, command = lambda: clear())
clearMostButton = tk.Button(window, text="CE", width = 5, height = 3, command = lambda: clearMost())
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
removeOneButton.place(x=thirdCol, y=firstRow)

oneButton.place(x=firstCol, y=secondRow)
twoButton.place(x=secondCol, y=secondRow)
threeButton.place(x=thirdCol, y=secondRow)

fourButton.place(x=firstCol, y=thirdRow)
fiveButton.place(x=secondCol, y=thirdRow)
sixButton.place(x=thirdCol, y=thirdRow)

sevenButton.place(x=firstCol, y=fourthRow)
eightButton.place(x=secondCol, y=fourthRow)
nineButton.place(x=thirdCol, y=fourthRow)

zeroButton.place(x=secondCol, y=fithRow)
decimalButton.place(x=thirdCol, y=fithRow)
equalButton.place(x=firstCol, y=fithRow)

addButton.place(x=fourthCol, y=secondRow)
subtractButton.place(x=fourthCol, y=thirdRow)
multiplyButton.place(x=fourthCol, y=fourthRow)
divideButton.place(x=fourthCol, y=fithRow)

tk.mainloop()
