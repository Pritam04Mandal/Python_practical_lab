#Operation on list 
#Check if all elements in list are numbers or not.
# If it is a numeric list, then count number of odd values in it.
# If list contains all Strings, then display largest String in the list
# Display list in reverse form.
# Find a specified element in list.
# Remove the specified element from the list.
# Sort the list in descending order.
# accept 2 lists and find the common members in them
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
        ind=l.index(i)
        flag=True
        break
if(flag==True):
    print("Element found at: "+str(ind))
else:
    print("Element not found")
rem=str(input("Enter the element you want to delete: "))
for i in l:
    if(str(i)==rem):
        l.remove(i)
        break
print("Afterremoving the specified element")
print(l)
la=len(l)
for i in range (la):
    key=l[i]
    j=i-1
    while(j>=0 and key>l[j]):
        l[j+1]=l[j]
        j=j-1
    l[j+1]=key
n1=int(input("Enter the length of list 1: "))
lt1=[]
for i in range(n1):
    x=int(input("Enter data: "))
    lt1.append(x)
n2=int(input("Enter the length of list 2: "))
lt2=[]
ce=[]
for i in range(n2):
    x=int(input("Enter data: "))
    lt2.append(x)
for i in range(n1):
    for j in range(n2):
        if(lt1[i]==lt2[j]):
            ce.append(lt1[i])
print("Common Elements in list 1 and list 2")
for i in ce:
    print(i)


