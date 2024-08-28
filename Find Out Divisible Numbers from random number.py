import random 

def generate_unique_random_numbers(lower, upper, total):
    if total > (upper - lower + 1):
        raise ValueError("Total cannot be greater than the range of numbers")
    
    numbers = set()
    while len(numbers) < total:
        numbers.add(random.randint(lower, upper))
    return list(numbers)

def main():
    lower = int(input("Enter the lower bound: "))
    upper = int(input("Enter the upper bound: "))
    total = int(input("Enter the total number of random numbers to generate: "))
    
    try:
        # Generate unique random numbers
        numbers = generate_unique_random_numbers(lower, upper, total)
        print (f"The random numbers are:  {numbers}")
    except ValueError as e:
        print(e)
        return
    
    is_divisible_by_2_and_3 = lambda x: x % 6 == 0

    divisible_numbers = [num for num in numbers if is_divisible_by_2_and_3(num)]

    print(f"Number divisible by both 2 and 3 in: {divisible_numbers}")

    
if __name__ == "__main__":
    main()
