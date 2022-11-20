def funccal(st:str):
    o={}
    for i in st:
        if(i==" "):
            continue
        o[i]=0
    for i in st:
        if(i==" "):
            continue
        o[i]+=1
    return o

op={}
st=str(input("Enter the String: "))
op=funccal(st)
print("::Frequency::")
print(op)