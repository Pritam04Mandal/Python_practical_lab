choice="y"
while(choice=="Y" or choice=="y"):
    print("1. length of entered string..\n2. Return maximum of three string\n3. replace all vowels with #\n4. number of words in string\n5. Check palindrome\n")
    ch=int(input("Enter your choice: "))
    if(ch==1):
        s=input("Enter the string: ")
        print(s," is of length ",len(s))
    elif(ch==2):
        s1=input("Enter the string: ")
        s2=input("Enter the string: ")
        s3=input("Enter the string: ")
        if(len(s1)>len(s2) and len(s1)>len(s3)):
            print(s1," is Maximum ")
        elif(len(s2)>len(s1) and len(s2)>len(s3)):
            print(s2," is Maximum ")
        elif(len(s1)==len(s2)==len(s3)):
            print("All string are same.")
        else:
            print(s3," is Maximum ")
    elif(ch==3):
        s=input("Enter the string: ")
        s1=""
        for i in range(len(s)):
            if(s[i]=='a' or s[i]=='e' or s[i]=='i' or s[i]=='o' or s[i]=='u' or s[i]=='A' or s[i]=='E' or s[i]=='I' or s[i]=='O' or s[i]=='U'):
                s1+="#"
            else:
                s1+=s[i]
        print("New String: ",s1)
    elif(ch==4):
        words=1
        s=input("Enter the string: ")
        for i in range(len (s)):
            if(s[i]==" "):
                words+=1
        print("Number of words: ",words)
    elif(ch==5):
        s=input("Enter the string you want to enter: ")
        s1=""
        for i in range(len(s)-1,-1,-1):
            s1+=s[i]
        if(s1==s):
                print(s1," is palindrome....\n")
        else:
            print(s," is not palindrome....\n")
    else:
        print("You entered Wrong choice!@!@#!#!23")
    choice=input("Do you want to continue(Y/N): ")

