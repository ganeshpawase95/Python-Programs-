def element_fibonacci_indices(list):
    fib_indices = [0, 1]
    a, b = 0, 1
    while b < len(list):
        fib_indices.append(b)
        a, b = b, a + b
    return [list[i] for i in fib_indices if i < len(list)]

print("The number of fibonacci indices is:", element_fibonacci_indices([10, 1, 20, 45, 12, 40, 95]))