# 1. ADD
# 2. SUBTRACT
# 3. MULTIPLY
# 4. DIVIDE 
print("Welcome To A Simple Caculator")
print()
print("1. for ADDING")
print("2. for SUBTRACTING")
print("3. for MULTIPLYING")
print("4. FOR DIVING")
print()
choice = int(input("Select an operation to perform: "))
print()
while choice < 1 or choice > 4:
    print("That is an invalid selection.")
    choice = int(input("Enter 1, 2, 3, 4: "))

if choice == 1:
    num1 = int(input("Enter First Number: "))
    num2 = int(input("Enter Second Number: "))
    add_answer = str(num1 + num2) 
    print("The sum is " + add_answer)
elif choice == 2:
    num1 = int(input("Enter First Number: "))
    num2 = int(input("Enter Second Number: "))
    sub_answer = str(num1 - num2) 
    print("The difference is " + sub_answer)
elif choice == 3:
    num1 = int(input("Enter First Number: "))
    num2 = int(input("Enter Second Number: "))
    multiply_answer = str(num1 * num2) 
    print("The product is " + multiply_answer)
elif choice == 4:
    num1 = int(input("Enter First Number: "))
    num2 = int(input("Enter Second Number: "))
    divide_answer = str(num1 / num2) 
    print("The result is " + divide_answer)
else:
    print("Invalid Entry")
    print("Please Select Correct Entry")

   