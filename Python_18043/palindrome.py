def palindrome(n):
    for i in range(n+1):
        n1=i
        rev=0
        while(n1>0):
            rev=(rev*10)+(n1%10)
            n1=n1//10
        if(rev==i):
            print(rev," is palindrome")


num=int(input("Enter the range till which you want to see palindrome number: "))
palindrome(num)