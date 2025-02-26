def even_numbers(n):
    return [x for x in range(n) if x % 2 == 0]
print(even_numbers(10))  # Output: [0, 2, 4, 6, 8]