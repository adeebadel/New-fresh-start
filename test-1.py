password = ""

while password != "goat123":
    password = input("Enter the password: ")
    
def greet(name):
    print("hello",name)
greet("Adeeb")

name = input("Enter your name: ")
days = int(input("Enter the number of days you have been training: "))

count = 1
while count<=days:
    print("days",count,"completed")
    count = count + 1
    
if days>=5:
    print("you have trained hard")
else:
    print("you need to train more")

def score_calc(days):
    return days * 10
score = score_calc(days)
print("score=",score)