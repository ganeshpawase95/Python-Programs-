def list_average(list):
    total = 0
    for num in list:
        total += num
    return total / len(list)

user_input = input("Enter a number of list: ").split(",")
user_input = [int(num) for num in user_input]
print("The average of the list is: ", list_average(user_input))
