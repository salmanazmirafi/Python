# # # --------------Chapter -12 Calculator app in python------------------


# Create Function

def addition(nu1, nu2):
    result = nu1 + nu2
    print("{0}+{1}={2}".format(nu1, nu2, result))


def subtraction(nu1, nu2):
    result = nu1 - nu2
    print("{0}-{1}={2}".format(nu1, nu2, result))


def multiplication(nu1, nu2):
    result = nu1 * nu2
    print("{0}*{1}={2}".format(nu1, nu2, result))


def division(nu1, nu2):
    if nu2 == 0.0:
        print("Can't do dived by zero")
    else:
        result = nu1 / nu2
        print("{0}/{1}={2}".format(nu1, nu2, result))


# # Display
print("What do you want to do?")
print("1 for addition")
print("2 for subtraction")
print("3 for multiplication")
print("4 for division")

# # User input - 2 Digit number
choice = input("Enter Your Choice : ")

# taking a 2 nuber as an input for user
nu1 = float(input("Enter Nuber One : "))
nu2 = float(input("Enter Nuber Two : "))

# # condition
if choice == '1':
    addition(nu1, nu2)
elif choice == '2':
    subtraction(nu1, nu2)
elif choice == '3':
    multiplication(nu1, nu2)
elif choice == '4':
    division(nu1, nu2)
else:
    print("Invalid Choice")

