t1=(1,2,5,7,9,2,4,6,8,10)
t2=(11,13,15)
max=0
min=0
length=len(t1)
T=list()
for i in t1:
    if(i%2==0):
        T.append(i)
T=tuple(T)
L2=list()
L2.append(t1)
L2.append(t2)
L2=tuple(L2)
print("After concatenating t2 to t1: ",L2)
for j in L2:
    if(j>max):
        max=j
    if(j<min):
        min=j
    
print("Maximum element in concatenated list: ",max)
print("Minimum element in concatenated list: ",min)
