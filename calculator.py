def calculator(symbol, num1, num2):
    if symbol == "+":
        return num1 + num2
    elif symbol == "-":
        return num1 - num2
    elif symbol == "*":
        return num1 * num2
    elif symbol == "/":
        return num1 / num2
    else:
        return "Invalid symbol"
    
symbol = input("Enter a symbol: ")
num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
print("The result is: ", calculator(symbol, num1, num2))