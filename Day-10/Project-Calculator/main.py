#Calculator

#Add
def add(n1, n2) :
  return n1 + n2

#Subtract
def subtract(n1, n2) :
  return n1 - n2

#Multiply
def multiply(n1, n2) :
  return n1 * n2

#Divide
def divide(n1, n2) :
  return n1 / n2

#Dictionary of operators
operations = {
  "+" : add,
  "-" : subtract,
  "*" : multiply,
  "/" : divide
}

import art

print(art.logo)

def calculator() :
  response = True
  num1 = float(input("Please enter the first number : "))
  
  for operators in operations :
    print(operators)
  
  while response : 
    operation_symbol = input("Pick an operation to perform from the line above : ")
    
    num2 = float(input("Please enter the next number : "))
    
    calculator_fn = operations[operation_symbol]
    answer = calculator_fn(num1, num2)
    
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    can_run = input("If you want to continue, type 'y' or type 'n' to terminate and start from beginning : ").lower()
    if can_run == 'y' :
      num1 = answer
    else : 
      response = False
      calculator()

calculator()
