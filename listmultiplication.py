def multiplication(list):
    total = 1
    for num in list:
        total *= num
    return total

user_input = input("Enter a list of numbers: ").split(",")
user_input = [int(num) for num in user_input]
print("The multiplication of the list is: ", multiplication(user_input))