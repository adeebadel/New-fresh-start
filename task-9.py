weight = float(input("Enter your weight in kg : "))
height = float(input("Enter your height in meters : "))

bmi = weight / (height ** 2)

print("Your BMI is : ", bmi)

age = int(input("Enter your age : "))
days = age * 365
print("You have lived for approximately", days, "days.")

num1 = int(input("Enter the first number : "))
num2 = int(input("Enter the second number : "))

print("addition=", num1 + num2)
print("subtraction=", num1 - num2)
print("multiplication=", num1 * num2)
print("division=", num1 / num2)
print("modulus=", num1 % num2)
print("remainder=", num1 // num2)
print("power=", num1 ** num2)

monthly_income = float(input("Enter your monthly income : "))
monthly_expenses = float(input("Enter your monthly expenses : "))

savings = monthly_income - monthly_expenses
print("Your monthly savings are : ", savings)