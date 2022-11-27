# Storing the total sales and earned commission and remark for a particular employee in tuple 
# commission and remark given according to the sales
# Excellent:Sales>=80000; Commission: 5% 
# Good:Sales>=60000and<80000; Commission: 5%
# Average:Sales>=40000and<60000; if (sales>=50000)==> Commission=5%
#                                else ==> Commission=0%
# WorkHard:Sales<40000 
def sales()->tuple:
    name=input("Enter the name: ")
    week1=float(input("Enter the sales in first week: "))
    week2=float(input("Enter the sales in second week: "))
    week3=float(input("Enter the sales in third week: "))
    week4=float(input("Enter the sales in forth week: "))
    Sales=week1+week2+week3+week4                                   #Calculating total sales
    remarks=""
    if(Sales>=80000):
        remarks="Excellent"                                         #Assigning Remark
        commission=(5*Sales)/100                                    #calculating Commission
        t=(name,Sales,commission,remarks)                           #Storing the data in tuple
    elif(Sales>=60000 and Sales<80000):
        remarks="Good"                                              #Assigning Remark
        commission=(5*Sales)/100                                    #calculating Commission
        t=(name,Sales,commission,remarks)                           #Storing the data in tuple
    elif(Sales>=40000 and Sales<60000):
        remarks="Average"                                           #Assigning Remark
        if(Sales>=50000):                                           #calculating Commission
            commission=(5*Sales)/100
        else:
            commission=0
        t=(name,Sales,commission,remarks)                           #Storing the data in tuple
    elif(Sales<40000):
        remarks="Work Hard"                                         #Assigning Remark
        commission=0                                                #calculating Commission
        t=(name,Sales,commission,remarks)                           #Storing the data in tuple
    return t


if __name__=="__main__": 
    n=int(input("Enter the number of workers: "))                   #taking Number of workers as input
    l=[]
    for i in range(0,n,1):                                          #Running loop for all workers
        print("WORKERS ",i+1,':')
        l.append(sales())                                           # Printing returned tuple for the worker
    print("(NAME,SALES,COMMISSION,REMARK)")
    for i in range (0,n,1):
        print(l[i])
