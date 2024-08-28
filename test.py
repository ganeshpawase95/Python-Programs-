# test.py

# problem space: Find Prime Factors of a Number using prime factorization
# Logical block 1: Define function to find prime factors of a number
def get_prime_factors(num):
    # Step 1: prime_factors_list = []
    prime_factors = []

    # Step 2: validate the type of input number and check if it is less than 2
    if type(num) != int or num < 2:
        return prime_factors 
    
    # Step 3: Loop till all the factor of 2 are removed
    while num % 2 == 0:
        prime_factors.append(2)
        num = num // 2

    # Step 4: Check if the num is 1 then the number is completely divided by 2 and return the list 
    if num == 1:
        return prime_factors

    # Step 5: Set the range starting from 3 till square root of the number with step 2
    start = 3
    end = int(num ** 0.5) + 1
    step = 2

    # Step 6: Loop through the range and devide the number to find the prime factors
    for prime_number in range(start, end, step):
        while num % prime_number == 0:
            prime_factors.append(prime_number)
            num = num // prime_number
    
    # step 7: If the number is still greater than 2 then add the number to the list
    if num > 2:
        prime_factors.append(num)

    return prime_factors

# step 1: Take user input for a number to find its prime factors
user_input = input("Enter a number: ")

# step 2: validate the user input and convert it to integer
num = user_input.isdigit() and int(user_input) or None

# step 3: ckeck the number is valid and call the get_prime_factors function
if num is not None:
    print(f"The prime factor of {num} is: {get_prime_factors(num)}")
else:
    print("Invalid input")