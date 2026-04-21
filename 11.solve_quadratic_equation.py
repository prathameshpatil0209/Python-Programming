import math 
a=int(input("Enter the a coefficient "))
b=int(input("Enter the b coefficient "))
c=int(input("Enter the b coefficient "))
d=b*2*2 - 4*a*c
if d>0:
	root1 = (-b + math.sqrt(d)) / (2*a)
	root2 = (-b - math.sqrt(d)) / (2*a)
	print(f"Root 1: {root1}")
	print(f"Root 2: {root2}")
elif d == 0:

	root = -b / (2*a)
	print(f"Root: {root}")
else:

	real_part = -b / (2*a)
	imaginary_part = math.sqrt(abs(d)) / (2*a)
	print(f"Root 1: {real_part} + {imaginary_part}i")
	print(f"Root 2: {real_part} - {imaginary_part}i")
