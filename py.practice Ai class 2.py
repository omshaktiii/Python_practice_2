# Check whether a number is even or odd

num = int(input("Enter a number :"))

if num % 2 == 0:
    print("It is even number")

else:
    print("It is odd number")

# Check whether a number is positive,negative or zero

a = int(input("Enter your number :"))

if a > 0:
    print("It is positive")

elif a < 0:
    print("It is negative")

else:
    print("It is zero")

#Find the largest between two number

a = int(input("Enter your first number :"))
b = int(input("Enter your second number :"))

if a > b:
    print("A is largest")

else:
    print("B is largest")

#Find the largest among three number

a = int(input("Enter your first number :"))
b = int(input("Enter your second number :"))
c = int(input("Enter your third number :"))

if a > b and a > c:
    print("A is largest ")

elif b > a and b > c:
    print("B is greater ")

else:
    print("C is greater")
    

# find the smallest among three number

a = int(input("Enter your first number :"))
b = int(input("Enter your second number :"))
c = int(input("Enter your third number :"))

if a < b and a < c:
    print("A is smallest ")

elif b < a and b < c:
    print("B is smallest ")

else:
    print("C is smallest")


#Check whethher a person eligible to vote

age = int(input("Enter your age number :"))

if age > 18:
    print("You are eligible")

else:
    print("You are not eligible")

# Check wheter a number is divisible by 5

num = int(input("Enter your number :"))

if num % 5 == 0:
    print("A number is divisible by 5")

else:
    print("A number is not devisible by 5 ")

#Check whether a year is a leap

year = int(input("Enter your year :"))

if year % 400==0 or year % 4 ==0 and year % 100 != 0:
    print("Leap year")

else:
    print("Not leap year")

#check whether student pass or fail (pass mark = 40)

mark = int(input("Enter student  marks :"))

if mark > 40:
    print("pass")

else:
    print("fail")
    

#creat a simple calculator using if,elif,else(+,-,*,/)


num1 = float(input("Enter first number :"))
operator = input("Enter operators(+,-,*,/):")
num2 = float(input("Enter second number:"))

if operator == "+":
    result = num1 + num2
    print("Result :", result)

elif operator == "-":
    result = num1 - num2
    print("Result :",result)

elif operator ==  "*":
    result = num1 * num2
    print("Result :", result)

elif operator == "/":
    if num2 != 0:
        result = num1 / num2
        print("Result :", result)

    else:
        ("Cannot divided by zero")

else:
    ("Operator invalid")
    


    

    
    
    
    
    
