import tkinter as tk 
from tkinter import ttk
#Create a window for the calculator 
root = tk.Tk()
root.title("Calculator")
#Create a text input in the window
Tb = ttk.Entry(root,width= 27,font=('century 12',18))
Tb.grid(row=0,column=0,columnspan=4, padx=10, pady=10)


#Here we will define the functions
def button_click(number):
    """This function will insert the button clicked in the input box"""
    global current
    current = Tb.get()
    Tb.delete(0,tk.END)
    Tb.insert(0,current +  str(number))
def BClear():
    """This function will clear the input box and clear the previous calculation"""
    Tb.delete(0,tk.END)
def button_add ():
    pass 
def button_sub():
    pass
def button_div():
    pass
def button_prod():
    pass
def button_comma():
    pass

    

#Here we create the buttons
Bper = tk.Button(root, padx= 48, pady=25,text="%", command= button_click)
Bclear =tk.Button(root, padx= 99, pady=25,text="Clear", command= BClear)

B1 = tk.Button(root, padx= 50, pady=25,text="1", command= lambda: button_click(1))
B2 = tk.Button(root, padx= 50, pady=25,text="2", command=lambda: button_click(2))
B3 = tk.Button(root, padx= 50, pady=25,text="3", command=lambda: button_click(3))

B4 = tk.Button(root, padx= 50, pady=25,text="4", command=lambda: button_click(4))
B5 = tk.Button(root, padx= 50, pady=25,text="5", command=lambda: button_click(5))
B6 = tk.Button(root, padx= 50, pady=25,text="6", command=lambda: button_click(6))

B7 = tk.Button(root, padx= 50, pady=25,text="7", command=lambda: button_click(7))
B8 = tk.Button(root, padx= 50, pady=25,text="8", command=lambda: button_click(8))
B9 = tk.Button(root, padx= 50, pady=25,text="9", command=lambda: button_click(9))

B0 = tk.Button(root, padx= 50, pady=25,text="0", command=lambda: button_click(0))
Beq = tk.Button(root, padx= 49, pady=25,text="=", command= button_click, bg="gray")
Bneg = tk.Button(root, padx= 44, pady=25,text="+/-", command= button_click)

B_add = tk.Button(root, padx= 49, pady=25,text="+", command= button_add )
B_sub = tk.Button(root, padx= 50, pady=25,text="-", command= button_sub )
B_div = tk.Button(root, padx= 50, pady=25,text="/", command= button_div )
B_prod =tk. Button(root, padx= 50, pady=25,text="*", command= button_prod )
B_comma =tk.Button(root, padx= 50, pady=25,text=".", command= button_comma )





#This will place the items in the window
Bper.grid(row=2, column=0)
Bclear.grid(row=2, column=1, columnspan=2)

B1.grid(row=5, column=0)
B2.grid(row=5, column=1)
B3.grid(row=5, column=2)

B4.grid(row=4, column=0)
B5.grid(row=4, column=1)
B6.grid(row=4, column=2)

B7.grid(row=3, column=0)
B8.grid(row=3, column=1)
B9.grid(row=3, column=2)

B0.grid(row=6, column=1)
Beq.grid(row=6, column=2)
Bneg.grid(row=6, column=0)

B_add.grid(row=2, column=3)
B_sub.grid(row=3, column=3)
B_div.grid(row=4, column=3)
B_prod.grid(row=5, column=3)
B_comma.grid(row=6, column=3)
















#Create the mainloop
root.mainloop()
