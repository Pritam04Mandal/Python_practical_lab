from Practical3 import Factorial as fact
import tkinter as tk
import tkinter.simpledialog as sp
x=0
n=0
if __name__=="__main__":
    font1=("Arial Black",10,"bold")
    font2=("Calibri(Header)",10,"bold","italic")
    root=tk.Tk()
    root.title("Sum of the series")
    root.geometry("400x100")
    l1=tk.Label(root,font=font1,text="Series: 1-x^2/2!+x^4/4!-x^6/6!+........x^n/n!")
    l1.pack()
    x=sp.askinteger("Input","Enter the value of x",parent=root)
    n=sp.askinteger("Input","Enter the value of n",parent=root)
    sum=0
    for i in range(n):
        if(i%2==0):
            sum+=((x**(i*2))/fact(i*2))
        else:
            sum-=((x**(i*2))/fact(i*2))
    l2=tk.Label(root,font=font2,text="Sum: "+str(sum))
    l2.pack()
    # print("Sum of series: ",sum)
    root.mainloop()