def is_armstrong_number(number):

    order = len(str(number))
    sum = 0
    temp = number
    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10
    return sum == number

def main():
    user_input = input("Enter a number: ")

    if not user_input.isdigit():
        print(f"Invalid input {user_input}. Please enter a positive integer.")


    number = int(user_input)
    if number < 0:
        print(f"Invalid input {user_input}. Please enter a positive integer.")
        return
    
    if is_armstrong_number(number):
        print(f"{number} is an Armstrong number.")
    else:
        print(f"{number} is not an Armstrong number.")
    
if __name__ == "__main__":
    main()
    