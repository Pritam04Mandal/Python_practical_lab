s=input("Enter the string you want to enter: ")
length=0
for i in s:
    length+=1
s1=""
for i in range(length-1,-1,-1):
    s1+=s[i]
if(s1==s):
    print(s1," is palindrome....\n")
else:
    print(s," is not palindrome....\n")
