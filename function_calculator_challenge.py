from function_calculator_challenge_logo import logo
print(logo)
def add(n1, n2):
    return n1 + n2
def substract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide
}
num1 = int(input("What is the first number?: "))
for operators in operations:
    print(operators)
picked_operator = input("Pick an Operations from the line above: ")
num2 = int(input("What is the second number?: "))
calc_func = operations[picked_operator]
output = calc_func(num1, num2)

print(f"{num1} {picked_operator} {num2} = {output}")