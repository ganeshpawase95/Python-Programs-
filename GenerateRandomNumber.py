import random

def generate_unique_random_numbers(lower, higher, total):
    return [random.randint(lower, higher) for _ in range(total)]

def main():
    lower = int(input("Enter the lower limit:"))
    higher = int(input("Enter the higher limit:"))
    total = int(input("Enter total number number for generate random number:"))

    random_list = generate_unique_random_numbers(lower, higher, total)
    print("Generated Random List:", random_list)

if __name__ == "__main__":
    main()