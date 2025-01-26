def checknums(num1, num2):
    if((num1^num2)!=0):
        print("Both the numbers are not the same...")
    else:
        print("Both the numbers are the same...")

num1=int(input("Enter the first number to compare: "))
num2=int(input("Enter the second number to compare: "))
checknums(num1, num2)