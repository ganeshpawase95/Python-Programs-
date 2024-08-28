def power(base, exponent):
    total = 1
    for i in range(exponent):
        total = base ** exponent
    return total

base = int(input("Enter a base: "))
exponent = int(input("Enter a exponent: "))
print("The power of the number is: ", power(base, exponent))