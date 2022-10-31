from fibonacci import factorial as fact


x=int(input("Enter the value of x: "))
n =int(input("Enter the number till you want to see sum: "))
sum=1
for j in range(1,n,2):
    if(j%2!=0):
        sum-=((x**(j*2))/fact(j*2))
    else:
        sum+=((x**(j*2))/fact(j*2))
print(sum)
