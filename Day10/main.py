from art import logo
#ADD
def add(n1, n2):
    return n1 + n2

#SUBTRACT
def subtract(n1, n2):
    return n1 - n2

#MULTIPLY
def multiply(n1, n2):
    return n1 * n2

#DIVIDE
def divide(n1, n2):
    return n1 / n2

operations = {
  "+":add, 
  "-": subtract,
  "*": multiply,
  "/": divide
}

def calculator():
  print(logo)
  num1 = float(input("What's the first number?: "))
  
  for symbol in operations:
    print(symbol)
    
  cont_calc = True
  
  while cont_calc:
    operation_symbol = input("Pick an operation from the line above: ")
    num2 = float(input ("What's the next number?: "))
    answer = operations[operation_symbol](num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    continue_calc = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")
    if continue_calc == "y":
      num1 = answer
    else:
      cont_calc = False
      calculator()

calculator()
      
