def return_digit(number:int):
    a=[]
    while(number>0):
        rem=number%10
        a.append(rem)
        number=number//10
    a.reverse()
    return (a)


num=int(input("Enter the number: "))
if(num>=10):
    print("digits are: ",return_digit(num))
else:
    print("Number is less than 10 cannot print the digits.")





