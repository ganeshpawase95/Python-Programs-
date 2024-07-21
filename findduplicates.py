# PROG 2.2: Generate Random List Function
import random

def find_duplicates(numbers):
   duplicates = []
   for i in range(len(numbers)):
       for j in range(i+1, len(numbers)):
           if numbers[i] == numbers[j]:
               duplicates.append(numbers[i])
   return duplicates

def create_random_list(lower, higher, total):
  return [random.randint(lower, higher) for _ in range(total)]

def main():
  lower_input = input("Enter lower limit > 0 for random number: ")
  higher_input = input("Enter higher limit for random number: ")
  total_input = input("Enter total random number to generate: ")

  if not (lower_input.isdigit() and higher_input.isdigit() and total_input.isdigit()):
        print("Invalid input. Please enter valid numbers.")
        return

  lower = int(lower_input)
  higher = int(higher_input)
  total = int(total_input)

  if lower > higher:
    print("Lower should be less than or equal to higher")
    return

  random_list = create_random_list(lower, higher, total)
  print(f"Random List Generated: {random_list}")

  print(f"Duplicates: {find_duplicates(random_list)}")

if __name__ == "__main__":
  main()
