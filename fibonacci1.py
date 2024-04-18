def fibonacci_recursive(n):
    if n < 3:
        return 1
    else:
        return fibonacci_recursive(n - 2) + fibonacci_recursive(n - 1)

n = int(input("Podaj nr wyrazu ciągu: "))
result = fibonacci_recursive(n)
print(f"{n} wyraz ciągu ma wartość {result}")
