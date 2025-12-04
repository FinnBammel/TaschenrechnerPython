import tkinter as tk
from tkinter import font
from enum import Enum


class SelectOperation(Enum):
    NONE = 0
    ADD = 1
    SUB = 2
    MULT = 3
    DIV = 4


root = tk.Tk()

root.geometry("340x295")


# dynamic layout for columns
root.columnconfigure(0, weight = 1)
root.columnconfigure(1, weight = 1)
root.columnconfigure(2, weight = 1)
root.columnconfigure(3, weight = 1)


# dynamic layout for rows
root.rowconfigure(0, weight = 1)
root.rowconfigure(1, weight = 1)
root.rowconfigure(2, weight = 1)
root.rowconfigure(3, weight = 1)
root.rowconfigure(4, weight = 1)


# font
font_general = font.Font (size = 20, family = "arial")


# input field
eingabe = tk.Entry(root, font = font_general, borderwidth = 20)

eingabe.grid(row = 0, column = 0, columnspan = 4)


# entry the numbers
def addChar(char): 
    eingabe.insert(tk.END, char)


# specificate numbers and operations
first_Number = 0

Second_Number = 0

Result = 0

selectedOperation = SelectOperation.NONE

DoDIV = False


# button 'add' pressed and remember first number
def pressedADD_and_remember_FirstNumber():
    global first_Number
    first_Number = int(eingabe.get())
    eingabe.delete(0, tk.END)
    global selectedOperation
    selectedOperation = SelectOperation.ADD


# add numbers
def Addition():
    global Second_Number
    Second_Number = int(eingabe.get())
    eingabe.delete(0, tk.END)
    global ResultADD
    ResultADD = first_Number + Second_Number
    eingabe.insert(tk.END, ResultADD)
   

# button 'Subtract' pressed and remember first number
def pressedSUB_and_remember_FirstNumber():
    global first_Number
    first_Number = int(eingabe.get())
    eingabe.delete(0, tk.END)
    global selectedOperation
    selectedOperation = SelectOperation.SUB


# Subtract numbers
def Subtraktion():
    global Second_Number
    Second_Number = int(eingabe.get())
    eingabe.delete(0, tk.END)
    global ResultSUB
    ResultSUB = first_Number - Second_Number
    eingabe.insert(tk.END, ResultSUB)


# button 'Multiplicate' pressed and remember first number
def pressedMULT_and_remember_FirstNumber():
    global first_Number
    first_Number = int(eingabe.get())
    eingabe.delete(0, tk.END)
    global selectedOperation
    selectedOperation = SelectOperation.MULT


# Multiplicate numbers
def Multiplikation():
    global Second_Number
    Second_Number = int(eingabe.get())
    eingabe.delete(0, tk.END)
    result = first_Number * Second_Number
    eingabe.insert(tk.END, result)


# button 'Divide' pressed and remember first number
def pressedDIV_and_remember_FirstNumber():
    global first_Number
    first_Number = int(eingabe.get())
    eingabe.delete(0, tk.END)
    global selectedOperation
    selectedOperation = SelectOperation.DIV


# Divide numbers
def Division():
    global Second_Number
    Second_Number = float(eingabe.get())
    eingabe.delete(0, tk.END)
    if Second_Number == 0:
        eingabe.insert(tk.END, 'ERROR') # error after dividing with 0
    else:
        global ResultDIV
        ResultDIV = first_Number / Second_Number
        eingabe.insert(tk.END, ResultDIV)


# buttons for numbers
button1 = tk.Button(root, text = "1", font = font_general, command=lambda: addChar ('1'))
button2 = tk.Button(root, text = "2", font = font_general, command=lambda: addChar ('2'))
button3 = tk.Button(root, text = "3", font = font_general, command=lambda: addChar ('3'))
button4 = tk.Button(root, text = "4", font = font_general, command=lambda: addChar ('4'))
button5 = tk.Button(root, text = "5", font = font_general, command=lambda: addChar ('5'))
button6 = tk.Button(root, text = "6", font = font_general, command=lambda: addChar ('6'))
button7 = tk.Button(root, text = "7", font = font_general, command=lambda: addChar ('7'))
button8 = tk.Button(root, text = "8", font = font_general, command=lambda: addChar ('8'))
button9 = tk.Button(root, text = "9", font = font_general, command=lambda: addChar ('9'))
button0 = tk.Button(root, text = "0", font = font_general, command=lambda: addChar ('0'))


# buttons for calculate        
button_add = tk.Button(root, text = "+", font = font_general, command=lambda: pressedADD_and_remember_FirstNumber())
button_sub = tk.Button(root, text = "-", font = font_general, command=lambda: pressedSUB_and_remember_FirstNumber())
button_div = tk.Button(root, text = "/", font = font_general, command=lambda: pressedDIV_and_remember_FirstNumber())
button_mult = tk.Button(root, text = "*", font = font_general, command=lambda: pressedMULT_and_remember_FirstNumber())


# Result/Clear
button_clear = tk.Button(root, text = "clear", font = font_general, command=lambda: eingabe.delete(0, tk.END))
button_result = tk.Button(root, text = "=", font = font_general,command=lambda: difference_DIV_MULT_ADD_SUB())


# difference the operation(Div/Mult/Sub/Add)
def difference_DIV_MULT_ADD_SUB():   
    global selectedOperation
    match selectedOperation:
        case SelectOperation.NONE:
            return
        case SelectOperation.ADD:
            Addition()
            return
        case SelectOperation.SUB:
            Subtraktion()
            return
        case SelectOperation.MULT:
            Multiplikation()
            return
        case SelectOperation.DIV:
            Division()
            return
    selectedOperation = SelectOperation.NONE


# grid and layout 
button7.grid(row = 1, column = 0, padx = (0), pady = (0), sticky = 'NSWE')
button8.grid(row = 1, column = 1, padx = (0),pady = (0), sticky = 'NSWE')
button9.grid(row = 1, column = 2, padx = (0), pady = (0), sticky = 'NSWE')
button_clear.grid(row = 1, column = 3, padx = (0), pady = (0), sticky = 'NSWE')

button4.grid(row = 2, column = 0, padx = (0), pady = (0), sticky = 'NSWE')
button5.grid(row = 2, column = 1, padx = (0), pady = (0), sticky = 'NSWE')
button6.grid(row = 2, column = 2, padx = (0), pady = (0), sticky = 'NSWE')
button_add.grid(row =2, column = 3, padx = (0), pady = (0), sticky = 'NSWE')

button1.grid(row = 3, column = 0, padx = (0), pady = (0), sticky = 'NSWE')
button2.grid(row = 3, column = 1, padx = (0), pady = (0), sticky = 'NSWE')
button3.grid(row = 3, column = 2, padx = (0), pady = (0), sticky = 'NSWE')
button_sub.grid(row = 3, column = 3, padx = (0), pady = (0), sticky = 'NSWE')

button_mult.grid(row = 4, column = 0, padx = (0), pady = (0), sticky = 'NSWE')
button0.grid(row = 4, column = 1, padx = (0), pady = (0), sticky = 'NSWE')
button_div.grid(row = 4, column = 2, padx = (0), pady = (0), sticky = 'NSWE')
button_result.grid(row = 4, column = 3, padx = (0), pady = (0), sticky = 'NSWE')


# start the program
root.mainloop()


