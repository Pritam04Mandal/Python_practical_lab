
def highestpercentage(a:dict)->str:
    percentage=0
    highest=list()
    names=list(a.keys())
    for j in names:
        for k in a[j]:
            percentage+=k
        percentage=percentage/4
        highest.append(percentage)
        percentage=0
    h=highest[0]
    for i in highest:
        if(i>h):
            h=i
    index=highest.index(h)
    return names[index]
    
data=dict()
n=int(input("Enter the number of studemt: "))
for i in range(n):
    name=input("Enter your name: ")
    maths=int(input("Enter marks in math: "))
    Physics=int(input("Enter marks in Physics: "))
    chemistry=int(input("Enter marks in Chemistry: "))
    English=int(input("Enter marks in English: "))
    marks=[maths,Physics,chemistry,English]
    data[name]=marks
print("Student with highes percenage is: ",highestpercentage(data))
