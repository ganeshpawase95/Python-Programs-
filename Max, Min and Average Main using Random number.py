import random

def compute_min_max_sum_average(numbers):
    min_fn = lambda a, b: a if a < b else b
    max_fn = lambda a, b: a if a > b else b
    sum_fn = lambda a, b: a + b

    if not numbers:
        return None, None, 0, 0.0
    
    min_num = numbers[0]
    max_num = numbers[0]
    total = 0

    for number in numbers:
        min_num = min_fn(min_num, number)
        max_num = max_fn(max_num, number)
        total = sum_fn(total, number)

    average = total / len(numbers)
    return min_num, max_num, total, round(average, 2)

def generate_unique_random_sequence(lower, upper,total):
    if total > (upper - lower + 1):
        raise ValueError("Total number of random number requisted is more than the range available.")

    numbers = set()
    while len(numbers) < total:
        numbers.add(random.randint(lower, upper))
    return list(numbers)

def main():
    lower = int(input("Enter lower limit > 0 for random number: "))
    upper = int(input("Enter higher limit for random number: ")) 
    total = int(input("Enter total random number to generates: "))

    try:
        numbers = generate_unique_random_sequence(lower, upper, total)
        print(f"The random numbers are: {numbers}")
    except ValueError as ve:
        print(ve)
        return

    min_num, max_num, total, average = compute_min_max_sum_average(numbers)
    
    # Logic : Use Python built-in function min(), max() and sum()
    builtin_min = min(numbers)
    builtin_max = max(numbers)
    builtin_sum = sum(numbers)
    builtin_avg = round(builtin_sum / len(numbers), 2)

    print(f"Computed Maximum: {max_num} And builtIn Maximum: {builtin_max}")  
    print(f"The computed Maximum is {'correct' if max_num == builtin_max else 'not correct'}.\n")

    print(f"Computed Minimum: {min_num} And builtIn Minimum: {builtin_min}")
    print(f"The computed Minimum is {'correct' if min_num == builtin_min else 'not correct'}.\n")

    print(f"Computed Total: {total} and builtIn Total: {builtin_sum}")
    print(f"The computed Total is: {'correct' if total == builtin_sum else 'not correct'}.\n")

    print(f"The computed Average is: {average}")

if __name__ == "__main__":
    main() 


