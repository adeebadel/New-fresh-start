password = ""
while password != "super123":
    password = input("enter the password: ")
def greet(name):
    print("hello",name)
greet("Adeeb")

name = input("Enter your name : ")
days = int(input("Number of training days : "))

count = 1
while count<10:
    print("days",count,"completed")
    count = count + 1
    
if days>=5:
    print("you worked hard")
else:
    print("nope do again")
    
def score_calc(days):
    return days * 10
score = score_calc(days)
print("score",score)    

    
    
    