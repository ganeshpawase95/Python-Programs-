import random

def create_random_list(lower, higher, total):
  return [random.randint(lower, higher) for _ in range(total)]

def main():
  is_even = lambda x: x % 2 == 0

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

  even_seq_loop = []
  odd_seq_loop = []
  for num in random_list:
      if is_even(num):
          even_seq_loop.append(num)
      else:
          odd_seq_loop.append(num)

  # Logic 4: Method 2 - Create Even and Odd Sequences using List Comprehension
  even_seq_comp = [num for num in random_list if is_even(num)]
  odd_seq_comp = [num for num in random_list if not is_even(num)]

  # Logic 5: Check if the Even and Odd Sequences are identical for Method 1 and Method 2
  even_identical = set(even_seq_loop) == set(even_seq_comp)
  odd_identical = set(odd_seq_loop) == set(odd_seq_comp)

  if even_identical and odd_identical:
      print("Even Sequences (Unique):", sorted(set(even_seq_loop)))
      print("Odd Sequences (Unique):", sorted(set(odd_seq_loop)))
  else:
      print("The Even and Odd sequences are not identical between the two methods.")

if __name__ == "__main__":
  main()