# Menu driven program to implement 
# linear search
# binary search
# bubble sort
# insertion sort
# selection sort

# Linear Search
def linearsearch(l):
    name=input("Enter the name you want to search: ")
    for i in range(len(l)):
        if l[i]==name:
            return i+1
    return -1
    
# Binary Search
def binarysearch(l,name,start,end):
    if(start==end):
        return (start)
    mid=(start+end)//2
    if(name==l[mid]):
        return mid
    if(name>l[mid]):
        return binarysearch(l,name,mid+1,end)
    if(name<l[mid]):
        return binarysearch(l,name,start,mid-1)
    return -1



# Bubble sort
def bubblesort(lst):
    la=len(lst)
    for i in range (la):
        for j in range(1,la-i,1):
            if(lst[j-1]>lst[j]):
                temp=lst[j-1]
                lst[j-1]=lst[j]
                lst[j]=temp
    return lst



# Selection sort
def selectionsort(lst):
    la=len(lst)
    for i in range(la):
        min=i
        for j in range(i+1,la):
            if(lst[j]<lst[min]):
                min=j
        temp=l[min]
        lst[min]=lst[i]
        lst[i]=temp
    return lst
# Insertion Sort
def insertionsort(lst):
    la=len(lst)
    for i in range (1,la):
        key=lst[i]
        j=i-1
        while(j>=0 and key<lst[j]):
            lst[j+1]=lst[j]
            j=j-1
        lst[j+1]=key
    return lst
    
l=[]
c="y"
c2="y"
while(c=="y" or c=="Y"):
    n=int(input("Enter the number of student: "))
    for i in range(0,n,1):
        name=input("Enter the student's name: ")
        l.append(name)
    while(c2=="y" or c2=="Y"):
        print("1. Linear Search\n2. Binary search\n3. Bubble Sort\n4. Insertion Sort\n5. Selection Sort\n")
        choice=int(input("Enter your choice: "))
        if(choice==1):
            print("Using Linear Search.......\n")
            k=linearsearch(l)
            if(k==-1):
                print("Name not found\n")
            else:
                print("Name Present at ",k," position")
        elif(choice==2):
            srt=insertionsort(l)
            print("Sorted Array: ",srt)
            nm=input("Enter the name: ")
            k=binarysearch(srt,nm,0,len(srt))
            if(k==-1):
                print("Name not found\n")
            else:
                print("Name Present at ",k," position")
        elif(choice==3):
            print("Array Sorted by Bubble Sort")
            sortedarray=bubblesort(l)
            print(sortedarray)
        elif(choice==4):
            print("Array Sorted by Insertion Sort")
            sortedarray=insertionsort(l)
            print(sortedarray)
        elif(choice==5):
            print("Array Sorted by Selection Sort")
            sortedarray=selectionsort(l)
            print(sortedarray)
        else:
            print("!@@!$@!Wrong Choice!@#@#$")
        c2=input("Do you want to continue the operations(Y/N): ")
    c=input("Dou want to enter a new list of name(Y/N): ")
