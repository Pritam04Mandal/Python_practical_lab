# Use dictionary to store marks of the students in 4 subjects . Write a function to find the name of the student 
# securing highest percentage. (Hint: Names of students are unique).
def highestpercentage(a:dict)->str:                                    #passing a dictionary as parameter
    percentage=0
    highest=list()
    names=list(a.keys())                                               #creating a list of indexs of the dictionary
    for j in names:
        for k in a[j]:
            percentage+=k                                              #Calculating the percentage for a student
        percentage=percentage/4
        highest.append(percentage)                                     #Storing the percentage in a list
        percentage=0                                              #Reseting the percentage variable for futher calculation    
        h=highest[0]
    for i in highest:
        if(i>h):                                                  #Finding the highest percentage
            h=i
    index=highest.index(h)                                        
    return names[index]                                           #Returning the name according to the highest percentage
    
data=dict()
n=int(input("Enter the number of studemt: "))                           #Taking number of student as input
for i in range(n):
    name=input("Enter your name: ")
    maths=int(input("Enter marks in math: "))
    Physics=int(input("Enter marks in Physics: "))
    chemistry=int(input("Enter marks in Chemistry: "))
    English=int(input("Enter marks in English: "))
    marks=[maths,Physics,chemistry,English]                             #creating a list of marks of a student
    data[name]=marks                                                #using name as index storing the list in dictionary
print("Student with highes percenage is: ",highestpercentage(data))     #calling the function while printing
