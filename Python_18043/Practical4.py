# returning the digits of a number as a set 
def return_digit(number:int)->list:
    a=[]
    while(number>0):
        rem=number%10            #finding the last digit
        a.append(rem)            #inserting the last digit in the list
        number=number//10        #removing the last digit permanently
    a=a[::-1]                    #reversing the list to make it in sequence
    return (a)                   #returning the list


num=int(input("Enter the number: "))
flag=True
while(flag):
    try:
        assert num>=10
        print("digits are: ",return_digit(num))
        flag=False
    except AssertionError:
        print("Number is less than 10 cannot print the digits.")
        print("Enter the number again......")
        num=int(input("Enter the number: "))




