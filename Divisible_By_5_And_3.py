list = [3, 10, 65, 15, 45, 50, 60, 90, 95]

divisible_by_3_and_5 = [num for num in list if num % 3 ==0 and num % 5 == 0]
print("Number divisible by 3 and 5 is:", divisible_by_3_and_5)

def sum(divisible_by_3_and_5):
    total = 0
    for num in divisible_by_3_and_5:
        total += num
    return  total
print("The addition of divisible by 3 and 5 is:",sum(divisible_by_3_and_5))