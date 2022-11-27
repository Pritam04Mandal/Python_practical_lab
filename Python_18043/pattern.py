h=int(input("Enter the height of the triangle: "))
for i in range(0,h,1):
    for j in range(0,h-i-1):
        print(end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print()
for i in range(1,h,1):
    for j in range(0,i):
        print(end=" ")
    for j in range(h-i):
        print("*",end=" ")
    print()