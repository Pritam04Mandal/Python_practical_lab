
import tkinter as tk
from tkinter import simpledialog as sp
root=tk.Tk()
root.title("Some Operations on given list")
t1=(1,2,5,7,9,2,4,6,8,10)
t2=(11,13,15)
font1=("Arial Black",10,"bold")
l1=tk.Label(root,font=font1,text="Given Tuple: "+str(t1))
l1.pack()
max=t1[0]
min=t1[0]
length=len(t1)
T=list()
for i in t1:
    if(i%2==0):
        T.append(i)
l2=tk.Label(root,font=font1,fg="red",text="Even Elements from the tuple: "+str(T))
l2.pack()
T=tuple(T)
L2=list()
for i in range(len(t1)):
    L2.append(t1[i])
for i in range(len(t2)):
    L2.append(t2[i])
L2=tuple(L2)
l4=tk.Label(root,font=font1,text="Tuple t2 = "+str(t2))
l4.pack()
l3=tk.Label(root,font=font1,fg="red",text="After concatenating t1 and t2: "+str(L2))
l3.pack()
for j in L2:
    if(j>max):
        max=j
    if(j<min):
        min=j
l5=tk.Label(root,font=font1,fg="red",text="Max = "+str(max)+", Min = "+str(min))
l5.pack() 
root.mainloop()
