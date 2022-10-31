def cal():
    sales=0
    saleslist=[]
    for i in range(4):
        # j=i+1
        print("Enter sales for the week",(i+1),end=": ")
        w=int(input())
        sales+=w
    saleslist.append(sales)
    if(sales>=50000):
        commission=((5/100)*sales)
    else:
        commission=0
    saleslist.append(commission)
    if(sales>=80000):
        saleslist.append("Excellent")
    elif(sales>=60000 & sales<80000):
        saleslist.append("Good")
    elif(sales>=40000 & sales<60000):
        saleslist.append("Average")
    else:
        saleslist.append("Work Hard")
    
    return saleslist




n=int(input("Enter the number of employees"))
for i in range(n):
    print("For Employee ",(i+1),': ')
    print(cal())
