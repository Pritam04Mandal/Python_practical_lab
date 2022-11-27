# Counting the frequency of each letter in string
def funccal(st:str):
    o={}
    for i in st:
        if(i==" "):
            continue
        o[i]=0                                   # initializing the dictionary with letters as index
    for i in st:
        if(i==" "):
            continue
        o[i]+=1                                  # Counting frequency for each letter
    return o

op={}
st=str(input("Enter the String: "))              # Entering a string 
op=funccal(st)                                   # Storing  the returned dictionary in main function
print("::Frequency::")
print(op)                                        # printing the frequency