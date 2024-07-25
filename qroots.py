import math

def find_roots(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        print("No real roots")
    else:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        print("Roots: {:.2f}, {:.2f}".format(root1, root2))

# test the function
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))
find_roots(a, b, c)