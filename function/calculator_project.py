def add(num1,num2):
    return num1 + num2

def subtract(num1,num2):
    return num1 - num2

def multiply(num1,num2):
    return num1 * num2

def divide(num1,num2):
    return num1 / num2

operation={"+":add,
           "-":subtract,
           "*":multiply,
           "/":divide
          }

'''choose=input("CHOOSE YOUR OPERATION :")
if choose=="+":
    print(operation["+"](num1=float(input("enter any number : ")),num2=float(input("enter any number : "))))
elif choose=="-":
    print(operation["-"](num1=float(input("enter any number : ")),num2=float(input("enter any number : "))))
elif choose=="*":
    print(operation["*"](num1=float(input("enter any number : ")),num2=float(input("enter any number : "))))
elif choose=="/":
    print(operation["/"](num1=float(input("enter any number : ")),num2=float(input("enter any number : "))))
else:
    print("Invalid Choice")'''

num1=float(input("ENTER FIRST NUMBER : "))
for symbol in operation:
    print(symbol)
o_symbol=input("ENTER YOU CHOICE : ")
num2=float(input("ENTER SECOND NUMBER : "))
result=operation[o_symbol](num1,num2)
print(f"{num1}{o_symbol}{num2}={result}")





