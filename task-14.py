for _ in range(10,0,-1):
    print(_)
print("blast off")

num = int(input("Enter a number: "))
total = 0
for _ in range(1,num+1):
    total = total +_
    print("sum=",total)
    
for _ in range(1,6):
    print("*" * _)
    
for _ in range(5,0,-1):
    print("*" * _)
    
days = int(input("How many training days? "))
for _ in range(1, days + 1):
    print("Day", _, ": Train")
    
for _ in range(1,10,2):
    print("*" * _)