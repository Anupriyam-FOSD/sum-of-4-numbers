print("Welcome !!!")
print("This app allows you to enter 4 number and find sum of it")
print("Press enter to continue")
input("")

try:
    num1 = float(input("Enter the first number :"))
    num2 = float(input("Enter the second number :"))
    num3 = float(input("Enter the third number :"))
    num4 = float(input("Enter the fourth number :"))
    sum = num1 + num2 + num3 + num4
except ValueError:
    print("There was an error while calculating!")
else:
    print(sum)
