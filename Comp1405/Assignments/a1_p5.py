import math
a=float(input('Enter side length a: '))
b=float(input('Enter side length b: '))
c=float(input('Enter side length c: '))
x=((a+b+c)/2)

area=math.sqrt(x*(x-a)*(x-b)*(x-c))

print(f'A triangle with side lengths {a}, {b}, and {c} has an area of {area}')