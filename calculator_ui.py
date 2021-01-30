from tkinter import *
expression = ""
calc = Tk()

def click(num):
    global expression
    expression += str(num)
    equation.set(expression)

def enter():
    global expression
    ans = eval(expression)
    l1 = Label(calc, text = str(ans), height = 2, width = 8)
    l1.grid(row = 0, column = 3)
    equation.set(str(ans))
    expression = "" 

def clear():
    global expression
    expression = ''
    equation.set(expression)
equation = StringVar()
#Entry box
iobox = Entry(calc, textvariable = equation)
equation.set("Welcome !")
iobox.grid(row = 0, columnspan = 4)

#grid of no.
b1 = Button(calc, text = "1", command = lambda: click(1), height = 2, width = 8, activebackground = "sky blue", bg = "cyan")
b1.grid(row = 1, column = 0)

b2 = Button(calc, text = "2", command = lambda: click(2), height = 2, width = 8, activebackground = "sky blue", bg = "yellow")
b2.grid(row = 1, column = 1)

b3 = Button(calc, text = "3", command = lambda: click(3), height = 2, width = 8, activebackground = "sky blue", bg = "cyan")
b3.grid(row = 1, column = 2)

b4 = Button(calc, text = "4", command = lambda: click(4), height = 2, width = 8, activebackground = "sky blue", bg = "yellow")
b4.grid(row = 2, column = 0)

b5 = Button(calc, text = "5", command = lambda: click(5), height = 2, width = 8, activebackground = "sky blue", bg = "cyan")
b5.grid(row = 2, column = 1)

b6 = Button(calc, text = "6", command = lambda: click(6), height = 2, width = 8, activebackground = "sky blue", bg = "yellow")
b6.grid(row = 2, column = 2)

b7 = Button(calc, text = "7", command = lambda: click(7), height = 2, width = 8, activebackground = "sky blue", bg = "cyan")
b7.grid(row = 3, column = 0)

b8 = Button(calc, text = "8", command = lambda: click(8), height = 2, width = 8, activebackground = "sky blue", bg = "yellow")
b8.grid(row = 3, column = 1)

b9 = Button(calc, text = "9", command = lambda: click(9), height = 2, width = 8, activebackground = "sky blue", bg = "cyan")
b9.grid(row = 3, column = 2)

b0 = Button(calc, text = "0", command = lambda: click(0), height = 2, width = 8, activebackground = "sky blue", bg = "lawn green")
b0.grid(row = 4, column = 0)

#enter button & clear button 
enter = Button(calc, text = "Enter", command = enter, height = 2, width = 8, activebackground = "sky blue", bg = "orange")
enter.grid(row = 4, column = 2)

clear = Button(calc, text = "Clear", command = clear, height = 2, width = 8, activebackground = "sky blue")
clear.grid(row = 0)


#operators
multiply = Button(calc, text = "*", command = lambda: click("*"), height = 2, width = 8, activebackground = "sky blue", bg = "red")
multiply.grid(row = 1, column = 3)

divide = Button(calc, text = "/", command = lambda: click("/"), height = 2, width = 8, activebackground = "sky blue", bg = "red")
divide.grid(row = 2, column = 3)

add = Button(calc, text = "+", command = lambda: click("+"), height = 2, width = 8, activebackground = "sky blue", bg = "red" )
add.grid(row = 3, column = 3)

substract = Button(calc, text = "-", command = lambda: click("-"), height = 2, width = 8, activebackground = "sky blue", bg = "red")
substract.grid(row = 4, column = 3)

#.
dot = Button(calc, text = ".", command = lambda: click("."),height = 2, width = 8, activebackground = "orange", bg = "lawn green")
dot.grid(row = 4, column = 1)

calc.mainloop()

'''
HW - create button for clear, diplay the previous answer
'''
