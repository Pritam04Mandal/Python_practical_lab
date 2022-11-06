def areaperimeter(a,b,c):
    area=a*b*c
    perimeter=a+b+c
    return(area,perimeter)
def side(a,b,c):
    if((a+b>c)or(b+c>a)or(c+a>b)):
        return True
    else:
        return False

side1=int(input("Enter side 1: "))
side2=int(input("Enter side 2: "))
side3=int(input("Enter side 3: "))
ap=areaperimeter(side1,side2,side3)
print("Area: ",ap[0],"Perimeter: ",ap[1])
p=side(side1,side2,side3)
if(p):
    print("Sum of two side is greater than third")
else:
    print("Did not satisfy the conditions")