import tkinter as tk
from tkinter import simpledialog as sp
from tkinter import messagebox as msg

def areaperimeter(a:int,b:int,c:int)->tuple:
    try:
        assert ((a+b>c) or (b+c>a) or (a+c>b))
        s=(a+b+c)/2
        area=(s*(s-a)*(s-b)*(s-c))**(0.5)
        perimeter=a+b+c
        return(area,perimeter)
    except AssertionError:
        msg.showerror("ERROR",message="Triangle is not a valid triangle")
root=tk.Tk()
root.title("Printing the AREA and PERIMETER")
root.geometry("500x500")
side1=sp.askfloat(parent=root,title="Enter Side",prompt="Enter side 1",initialvalue=0,minvalue=0)
side2=sp.askfloat(parent=root,title="Enter Side",prompt="Enter side 2",initialvalue=0,minvalue=0)
side3=sp.askfloat(parent=root,title="Enter Side",prompt="Enter side 3",initialvalue=0,minvalue=0)
font1=("Arial",15,"bold","italic")
flag=True
l1=tk.Label(master=root,font=font1,fg="blue",text="(Area, Perimeter)")
l1.pack()
l2=tk.Label(master=root,font=font1,fg="red",text=str(areaperimeter(side1,side2,side3)))
l2.pack()
flag=False
root.mainloop()
