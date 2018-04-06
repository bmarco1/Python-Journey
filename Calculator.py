import math
import cmath
print("""Choose from
        1. Perform basic BODMAS
        2. Find squareroot
        3. Solve quadratic equation
        4. Find Trignometric values
        5. Find logarithms""")
choose = input("enter required number \n")

if choose == '1':

    def bodmas():
        num1 = float(input("Enter number 1 \n"))
        num2 = float(input("Enter number 2 \n"))
        op= input("Enter add,sub,mul,div \n")
        if op == "add":
            res = num1+num2
        elif op == "sub":
            res = num1 - num2
        elif op == "mul":
            res = num1*num2
        elif op == "div":
            res = num1/ num2
        else:
            res = print("Error")
        return res
    print(bodmas())

elif choose == '2':

    def sqrt_n():
        num1 = float(input("Enter number"))
        res = math.sqrt(num1)
        return res
    print(sqrt_n())

elif choose =='3':

    def quad_s():
        print("Standard form of Quadratic equation (Ax^2 + Bx + C)")
        A = int(input("Enter coefficient A: "))
        B = int(input("Enter coefficient B: "))
        C = int(input("Enter coefficient C: "))
        D = (B**2)-(4*A*C)  # Calculate Discriminant

        sol1 = (-B-cmath.sqrt(D))/(2*A)
        sol2 = (-B+cmath.sqrt(D))/(2*A)

        z =print("The solutions are {0} and {1}" .format(sol1 ,sol2))
        return z
    print(quad_s())
elif choose == '4':

    choice = input("Choose sin,cos,tan: ")
    if choice == "sin":
        ang = float(input("Enter angle: "))
        x = math.sin(math.radians(ang))
        print (x)
    elif choice == "cos":
        ang = float(input("Enter angle: "))
        x = math.cos(math.radians(ang))
        print (x)
    elif choice == "tan":
        ang = float(input("Enter angle: "))
        x = math.tan(math.radians(ang))
        print (x)
    else:
        print("Error")

elif choose == "5":
    z = int(input("Enter Value: "))
    res = math.log10(z)
    print (res)
else:
    print("Error")
