#import tkinter
import tkinter as tk
from tkinter import messagebox

#define width and height for window
width = 250
height = 375

#create window
window = tk.Tk()
window.geometry(f"{width}x{height}")
window.minsize(width,height)
window.maxsize(width,height)
window.title("Calculator")

#set window icon
window.iconbitmap("icon.ico")

#global variables
numberString1 = "0"
numberString2 = ""
result = 0
mode = ""

#label to display numbers
label = tk.Label(window, text=f"{numberString1}{mode}")
label.place(x=20, y=20)

#define addNumber function
def addNumber(number):
    global numberString1
    global numberString2
    global mode
    
    if mode == "":
        if numberString1 == "0" and number != ".":
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
        label.config(text=f"{numberString1}{mode}{numberString2} = {format(result, '.2e')}")
    else:
        label.config(text=f"{numberString1}{mode}{numberString2} = {result}")

#define clear function
def clear():
    global numberString1
    global numberString2
    global mode
    numberString1 = "0"
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
        if numberString1 == "":
            numberString1 = "0"
        label.config(text=f"{numberString1}{mode}")
    else:
        numberString2 = numberString2[:-1]
        if numberString2 == "":
            mode = ""
        label.config(text=f"{numberString1}{mode}{numberString2}")

def keyHandler(event):
    match event.char:
        case "1":
            addNumber(1)
        case "2":   
            addNumber(2)
        case "3":
            addNumber(3)
        case "4":
            addNumber(4)
        case "5":
            addNumber(5)
        case "6":
            addNumber(6)
        case "7":
            addNumber(7)
        case "8":
            addNumber(8)
        case "9":
            addNumber(9)
        case "0":
            addNumber(0)
        case ".":
            addNumber(".")
        case "+":
            setMode("+")
        case "-":
            setMode("-")
        case "*":
            setMode("*")
        case "/":
            setMode("/")
        case "=":
            equal()
        case "\r":
            equal()
        case "c":
            clear()
        case _:
            return

window.bind("<BackSpace>", lambda _: removeOne())
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
