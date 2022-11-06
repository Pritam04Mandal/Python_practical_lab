import Practical3
if __name__=="__main__":
    x=int(input("Enter the value of x: "))
    n=int(input("Enter the number of terms: "))
    sum=0
    i=0
    while((i*2)<=n):
        if(i%2==0):
            sum+=((x**(i*2))/Practical3.Factorial(i*2))
        else:
            sum-=((x**(i*2))/Practical3.Factorial(i*2))
    print("Sum of series: ",sum)