import matplotlib.pyplot as plt

def plothistogram(l):
    xlabel=input("Enter the label for x: ")
    ylabel=input("Enter the label for y:" )
    plt.hist(l)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()


l=[]
t=True
while(t):
    x=int(input("Enter the value to plot histogram(to exit enter [-99]): "))
    if(x==-99):
        break
    l.append(x)
plothistogram(l)