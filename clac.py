from art import logo
# Add function 
def add(n1, n2):
  return n1 + n2


#Subtract function
def subtract(n1, n2):
  return n1-n2


#Divide function
def devision(n1, n2):
  return n1/n2


#Multiplication function
def multiply(n1,n2):
  return n1*n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": devision
}
def calculator():
  print(logo)
  num1 = float(input("What is the first number: "))
  for symbols in operations:
    print(symbols)
  should_continue = True
  while should_continue:
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("what is the next number: "))
    calculation_function = operations[operation_symbol]
    result = calculation_function(num1, num2)
    print(num1, operation_symbol, num2, '=', result)
  
  
    if input(f"type y to continue calclualting the with answer {result}, or type n to start a new calculation ") == 'y':
      num1 = result
    else:
      should_continue = False
      calculator()
calculator()
      
    

