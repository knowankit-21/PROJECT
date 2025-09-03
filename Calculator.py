# Using function build calculator in python...

# Feature:-
# 1.Add
# 2.Subtract
# 3.Multiple
# 4.Divide
# 5.Square root
# 6.Under root
# 7.percentage
# 8.Reciprocal
# 9.Cube
# 10.BMI calculate 


import math
from fractions import Fraction

print("Basic python Calculator")
print()


def _Add():
    num1 = int(input("Enter your 1st Number:"))
    num2 = int(input("Enter your 2nd Number:"))
    return print("Addition of", num1, "+", num2, "is =", num1 + num2)


def _Subtract():
    x = int(input("Enter your 1st Number:"))
    y = int(input("Enter your 2nd Number:"))
    return print("Subtraction of", x, "-", y, "is =", x - y)


def _Multi():
    x = int(input("Enter your 1st Number:"))
    y = int(input("Enter your 2nd Number:"))
    return print("Multiplication of", x, "*", y, "is =", x * y)


def _Division():
    x = int(input("Enter your 1st Number:"))
    y = int(input("Enter your 2nd Number:"))
    if y == 0:
        print("Y=Denominator is zero")
    else:
        return print("Division of", x, "/", y, "is =", int(x / y))


def _sqroot():
    x = int(input("Enter your Number:"))
    return print("Square root of", x, "is=", x**2)


def _underroot():
    x = int(input("Enter your 1st Number:"))
    return print("Under root of", x, "is =", (math.sqrt(x)))


def _percantage():
    x = int(input("Enter your 1st Number:"))
    y = int(input("Enter your 2nd Number:"))  # x = How much marks obtained
    # y = Total marks
    return print("Overall percantage is =", (x / y) * 100)


def _reciprocal():
    x = int(input("Enter your 1st Number:"))
    if x == 0:
        print("undefined value")
    else:
        return print("Reciprocal of", x, "is =", Fraction(1, x))


def BMI_Calculator():
    x=int(input("Enter Your Age:"))
    y=input("Enter Your Gender:")
    z=int(input("Enter Your Height:"))
    w=int(input("Enter Your Weight:"))

    if x==15 or 16 or 17 or 18 or 19 or 20 and y=='male' and z==160 or 161 or 162 or 163 or 164 or 165 and w==65 or 66 or 67 or 68 or 69 or 70:
        print("Your are fit in condition:")
    else:
        print("plz enter valid value:")

def cube():
    num1=int(input("Enter your Number:"))
    print("The cube of",num1,"is:",num1**3)

while True:
    print("1.ADD")
    print("2.SUBTRACT")
    print("3.MULTIPLICATION")
    print("4.DIVISION")
    print("5.SQUARE ROOT")
    print("6.UNDERROOT")
    print("7.PERCANTAGE")
    print("8.RECIPROCAL")
    print("9.BMI calculator")
    print("10.Cube")
    print("11.EXIT")

    try:

     choise = int(input("chose your operation number:"))

     if choise == 1:
        print(_Add())
     elif choise==2:
        print(_Subtract())
     elif choise==3:
        print(_Multi())
     elif choise==4:
        print(_Division)
     elif choise==5:
        print(_sqroot())
     elif choise==6:
        print(_underroot())
     elif choise==7:
        print(_percantage())
     elif choise==8:
        print(_reciprocal())
     elif choise==9:
         print(BMI_Calculator())
     elif choise==10:
         print(cube())
     else:
         if choise==11:
             print("Close the calculator!")
             print("Thank you ")
             break

    except:
        print("Please write valid number like 1 to 11:")

