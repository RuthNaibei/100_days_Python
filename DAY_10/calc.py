def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

num1= int(input("Enter first number:"))
for symbol in operations:
  print(symbol)
operation_symbol=input("Enter an operation: ") 
num2= int(input("Enter first number:"))
calculation_function= operations[operation_symbol]

answer=calculation_function(num1,num2)
print(f"{num1} {operation_symbol} {num2} = {answer}")

