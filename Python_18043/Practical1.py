def areaperimeter(a:int,b:int,c:int)->tuple:
    try:
        assert ((a+b>c) or (b+c>a) or (a+c>b))
        area=a*b*c
        perimeter=a+b+c
        return(area,perimeter)
    except AssertionError:
        print("Triangle is not a valid triangle")
        
def areaperimeter(a:float,b:float,c:float)->tuple:
    try:
        assert ((a+b>c) or (b+c>a) or (a+c>b))
        area=a*b*c
        perimeter=a+b+c
        return(area,perimeter)
    except AssertionError:
        print("Triangle is not a valid triangle")

side1=float(input("Enter side 1: "))
side2=float(input("Enter side 2: "))
side3=float(input("Enter side 3: "))
flag=True
while(flag):
    try:
        assert (int(side1)>0 and int(side2)>0 and int(side3)>0)
        print("Area, Perimeter")
        print(areaperimeter(side1,side2,side3))
        flag=False
    except AssertionError:
        print("Sides should be numeric and cannot be negative or zero")
        print("Enter the side again.......")
        side1=int(input("Enter side 1: "))
        side2=int(input("Enter side 2: "))
        side3=int(input("Enter side 3: "))
        
