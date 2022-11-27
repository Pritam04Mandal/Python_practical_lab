# Global list for entering output
a=[]
# Function to find the factorial of the entered number
def Factorial(num:int)->int:
    factorial=1
    if(num==0):
        return factorial
    for i in range(1,num+1):
        factorial*=i
    return factorial
# Function to find the nth term of the fibonacci series
def fibonacci(num:int,first:int=0,second:int=1):
    for i in range(num):
        temp=first
        first=second
        second=temp+second
    a.append(Factorial(num))
    a.append(first)
if __name__=="__main__":
    k=int(input("Enter the nth term for fibonacci series and factorial: "))
    fibonacci(k)                                                 #calling fibonacci series to find nTH term
    print("[FACTORIAL,nTH TERM OF THE FIBONACCI SERIES]")        
    print(a)                                                     # print the result as list