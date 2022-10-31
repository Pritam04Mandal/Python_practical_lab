side1=float (input("Enter the first side: "))
side2=float (input("Enter the second side: "))
side3=float (input("Enter the third side: "))
perimeter=side1+side2+side3
s=(side1+side2+side3)/2
area=(s*(s-side1)*(s-side2)*(s-side3))**(1/2)
tu=(perimeter,area)
print("Perimeter,Area")
print(tu)
print("Assert the sum of any two side is greater thean third")
if(((side1+side2)>side3)&((side3+side1)>side2)&((side3+side2)>side1)):
    print("Triangle is possible. Assertion is true")