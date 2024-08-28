def count_down(num):
    if num < 0:
        return
    print(num)
    count_down(num - 1)

number = int(input("Enter a number: "))
count_down(number)