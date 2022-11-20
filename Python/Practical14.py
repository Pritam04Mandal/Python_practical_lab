fopen = open("OLD.txt","r")
fwrite = open("NEW.txt","w")
oldfileonfo = fopen.readlines()
print(oldfileonfo)
for i in range(1,len(oldfileonfo),2):
    fwrite.write(oldfileonfo[i])
fwrite.close()
fopen.close()