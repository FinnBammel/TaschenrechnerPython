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
root.geometry("500x500")

font_general = font.Font (size=20, family="arial")

eingabe = tk.Entry(root, font=font_general, borderwidth=20)

eingabe.grid(row=0, column=0, columnspan=4)

#Eingabe der Zahlen
def addChar(char): 
    eingabe.insert(tk.END, char)

#Angabe Zahlen
first_Number = 0

Second_Number = 0

Result = 0

selectedOperation = SelectOperation.NONE

#Zahlen nach Eingabe merken
def add_numbers():
    global first_Number
    first_Number = int(eingabe.get())
    eingabe.delete(0, tk.END)
    global selectedOperation
    selectedOperation = SelectOperation.ADD

#Zahlen Addieren
def addition():
    global Second_Number
    Second_Number = int(eingabe.get())
    eingabe.delete(0, tk.END)
    global ResultADD
    ResultADD = first_Number + Second_Number
    eingabe.insert(tk.END, ResultADD)
   

#Subtraktion
def SUB_Numbers():
    global first_Number
    first_Number = int(eingabe.get())
    eingabe.delete(0, tk.END)
    global selectedOperation
    selectedOperation = SelectOperation.SUB


#Zahlen Subtrahieren
def Subtraktion():
    global Second_Number
    Second_Number = int(eingabe.get())
    eingabe.delete(0, tk.END)
    global ResultSUB
    ResultSUB = first_Number - Second_Number
    eingabe.insert(tk.END, ResultSUB)

# Button 'Multiplikation' gedrückt
def MULT_Numbers():
    global first_Number
    first_Number = int(eingabe.get())
    eingabe.delete(0, tk.END)
    global selectedOperation
    selectedOperation = SelectOperation.MULT

# Zahlen multiplizieren
def Multiplikation():
    global Second_Number
    Second_Number = int(eingabe.get())
    eingabe.delete(0, tk.END)
    result = first_Number * Second_Number
    eingabe.insert(tk.END, result)


#Zahlentasten
button1 = tk.Button(root, text="1", font=font_general,command=lambda: addChar ('1'))
button2 = tk.Button(root, text="2", font=font_general,command=lambda: addChar ('2'))
button3 = tk.Button(root, text="3", font=font_general,command=lambda: addChar ('3'))
button4 = tk.Button(root, text="4", font=font_general,command=lambda: addChar ('4'))
button5 = tk.Button(root, text="5", font=font_general,command=lambda: addChar ('5'))
button6 = tk.Button(root, text="6", font=font_general,command=lambda: addChar ('6'))
button7 = tk.Button(root, text="7", font=font_general,command=lambda: addChar ('7'))
button8 = tk.Button(root, text="8", font=font_general,command=lambda: addChar ('8'))
button9 = tk.Button(root, text="9", font=font_general,command=lambda: addChar ('9'))
button0 = tk.Button(root, text="0", font=font_general,command=lambda: addChar ('0'))

#Rechentasten        
button_plus = tk.Button(root, text="+", font=font_general, command=lambda: add_numbers ())
button_minus = tk.Button(root, text="-", font=font_general,command=lambda: SUB_Numbers ())
button_div = tk.Button(root, text="/", font=font_general,command=lambda: addChar ('/'))
button_mult = tk.Button(root, text="*", font=font_general,command=lambda: MULT_Numbers())

#Ergebnis/Löschen
button_clear = tk.Button(root, text="clear", font=font_general, command=lambda: eingabe.delete(0, tk.END))
button_result = tk.Button(root, text="=", font=font_general,command=lambda: Total())

#Unterschied Addition/Subtraktion
def Total():   
    global selectedOperation
    match selectedOperation:
        case SelectOperation.NONE:
            return
        case SelectOperation.ADD:
            addition()
        case SelectOperation.SUB:
            Subtraktion()
        case SelectOperation.MULT:
            Multiplikation()
        case SelectOperation.DIV:
            return
            #Division
    selectedOperation = SelectOperation.NONE

#Aufteilung
button7.grid(row=1,column=0)
button8.grid(row=1,column=1)
button9.grid(row=1,column=2)
button_clear.grid(row=1,column=3)

button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)
button_plus.grid(row=2,column=3)

button1.grid(row=3,column=0)
button2.grid(row=3,column=1)
button3.grid(row=3,column=2)
button_minus.grid(row=3,column=3)

button_mult.grid(row=4,column=0)
button0.grid(row=4,column=1)
button_div.grid(row=4,column=2)
button_result.grid(row=4,column=3)

root.mainloop()
