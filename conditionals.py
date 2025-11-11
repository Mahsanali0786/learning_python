# Practice Questions
# 1). number is even or odd
number = int(input("Enter a number: "))

if number % 2  == 0:
    print("Number is Even")
else:
    print("Number is Odd")

# 2). Greatest of three numbers
number1 = float(input("Enter First Number: "))
number2 = float(input("Enter Second Number: "))
number3 = float(input("Enter Third Number: "))
number4 = float(input("Enter Third Number: "))


if(number1 >= number2) and (number1 >= number3) and (number1 >= number4):
    greatest = number1
elif(number2 >= number1) and (number2 >= number3) and (number2 >= number4):
    greatest = number2
elif(number3 >= number1) and (number3 >= number2) and (number3 >= number4):
    greatest = number3
else:
    greatest = number4

print("Greatest Number is:", greatest)

# 3). if number is multiple of 7

num = int(input("Enter a number: "))

if num % 7 == 0:
    print("Number is multiple of 7")
else:       
    print("Number is not multiple of 7")



#marks = float(input("Enter your marks: "))
marks = 65

if marks>=90:
    grade = 'A'
elif marks>=80:
    grade = 'B'
elif marks>=70:
    grade = 'C'
elif marks>=60: 
    print("Marks are between 60 and 69")
    grade = 'D'
else:
    grade = 'F'

print("Grade:", grade)