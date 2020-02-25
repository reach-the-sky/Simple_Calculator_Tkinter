from tkinter import *
a,b,z=0,0,0
root = Tk()
root.title("Calculator designed by krishna")
Label(root,text="Enter your number here")
Input_numbers = Entry(root,width=35,borderwidth = 5,fg="Blue",bg="#C6AEC7")
Label(root,text="       ").grid(column=0)
Input_numbers.grid(row=0,column=1,columnspan=2)
root.geometry("300x350")
def Input_add():
    global a,z
    z=1
    a = float(Input_numbers.get())
    Input_numbers.delete(0, 'end')
def Input_sub():
    global a,z
    z=2
    a = float(Input_numbers.get())
    Input_numbers.delete(0,'end')
def Input_mul():
    global a,z
    z=3
    a = float(Input_numbers.get())
    Input_numbers.delete(0,'end')
def Input_div():
    global a,z
    z=4
    a = float(Input_numbers.get())
    Input_numbers.delete(0,'end')
def Input_enter():
    b = int(Input_numbers.get())
    if z==1:
        sum = a+b
        Input_numbers.delete(0, END)
        Input_numbers.insert(0,sum)
    elif z==2:
        sub = a-b
        Input_numbers.delete(0, END)
        Input_numbers.insert(0,sub)
    elif z==3:
        mul = a*b
        Input_numbers.delete(0, END)
        Input_numbers.insert(0,mul)
    elif z==4:
        div = a/b
        Input_numbers.delete(0, END)
        Input_numbers.insert(0, div)
def Input_clear():
    Input_numbers.delete(0,END)



Benter = Button(root, text=" Enter ",command = Input_enter,bg = "#C2DFFF",width=20,height=3)
Benter.grid(row=3,column=1,columnspan=2)
Badd = Button(root, text=" + ",command = Input_add,bg = "#52D017",width=15,height=5)
Badd.grid(row=1,column=1)
Bsub = Button(root, text=" - ",command = Input_sub,bg = "#FFF380",width=15,height=5)
Bsub.grid(row=1,column=2)
Bdiv = Button(root, text=" / ",command = Input_div,bg = "#E67451",width=15,height=5)
Bdiv.grid(row=2,column=1)
Bmul = Button(root, text=" * ",command = Input_mul,bg = "#C48793",width=15,height=5)
Bmul.grid(row=2,column=2)
Button(root,command = Input_clear,width=20,height=3,text="Clear").grid(row=4,column=1,columnspan=2)
root.mainloop()