print("OPERATION ON LIST")
n=int(input("Enter the size of list: "))
l=[]
for i in range (n):
    x=int(input("Enter the element: "))
    l.append(x)
num=0
numstr=0
for i in l:
    if(type(i)==int or type(i)==float):
        num+=1
    if(type(i)==str):
        numstr+=1
if( num==len(l)):
    print("All numbers")
    odd=0
    for i in l:
        if(i%2!=0):
            odd+=1
    print("Number of odd numbers: ",odd)
if(numstr==len(l)):
    print("All Strings")
    largest=""
    for j in l:
        if(j>largest):
            largest=j
    print("Largest string is: ",largest)

l2=l[::-1]
print("Reverese of list: ",l2)
search=str(input("Enter the element you want ot search: "))
for i in l:
    if(str(i)==search):
        print("Element found at "+str(l.index(i)))


