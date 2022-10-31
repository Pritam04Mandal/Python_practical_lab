a=list()
def factorial(num):
    factorial=1
    for i in range(1,num+1):
        factorial*=i
    return factorial
def fibonacci(num:int,first=0,second=1):
    for i in range(num-1):
        temp=first
        first=second
        second=temp+second
    a.append(first)
    a.append(factorial(num))
    return (a)

k=int(input("Enter the nth term for fibonacci series and factorial: "))
li=fibonacci(k)
print(li)