l=[]
n=int(input("Enter the number of student: "))
for i in range (n):
    name=input("Enter the name of student: ")
    l.append(name)
def linearsearch(l):
    name=input("Enter the name you want to search: ")
    for i in range(len(l)):
        if l[i]==name:
            print("Name present at ",i+1,"position")
            break
    
def binarysearch(l,name,start,end):
    if(start==end):
        return (start)
    mid=(start+end)//2
    if(name==l[mid]):
        return mid
    if(name>l[mid]):
        binarysearch(l,name,mid+1,end)
    if(name<l[mid]):
        binarysearch(l,name,start,mid-1)
    return -1
def bubblesort(l):
    la=len(l)
    for i in range (la):
        for j in range(0,la-i,1):
            if(l[j]>l[j+1]):
                temp=l[j]
                l[j]=l[j+1]
                l[j+1]=temp
def selectionsort(l):
    la=len(l)
    for i in range(la):
        min=i
        for j in range(i+1,la):
            if(l[j]<l[min]):
                min=j
        temp=l[min]
        l[min]=l[i]
        l[i]=temp
def insertionsort(l):
    la=len(l)
    for i in range (la):
        key=l[i]
        j=i-1
        while(j>=0 and key<l[j]):
            l[j+1]=l[j]
            j=j-1
        l[j+1]=key
    

