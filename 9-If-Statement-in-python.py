# # # --------------Chapter -09 If Statement in python------------------

# Condition মানে হয় এটা করো নয়তো ঐটা কর
x = 40
y = 20

# if Statement
if x < y:
    # if Statement Body
    print(x, "smaller then", y)
elif x > y:
    # els if Statement Body
    print(x, "is getter then", y)
else:
    # Else Statement Body
    print("The value of x is equal to y")


# Program to find out the user is eligible for driving license or not
user = input("Enter Your Age : ")

if 18 <= int(user) <= 30:
    print("You are eligible in driving license")
elif 31 <= int(user) <= 60:
    print("Your age is very high")
else:
    print("Sorry your age is to young")
