def fibonacci_iterative(start, n):
    if n <= 0:
        return None
    elif n == 1:
        return start
    elif n == 2:
        return start + 1
    
    f0 = start
    f1 = start + 1
    
    for i in range(2, n):
        f = f0 + f1
        f0, f1 = f1, f
        print(f)
    
    return f

# Przykładowe użycie:
start = int(input("Podaj cyfrę od której chcesz rozpocząć generację ciągu Fibonacciego: "))
n = int(input("Podaj ilość liczb ciągu Fibonacciego do wygenerowania: "))
print(f"n-ta liczba ciągu Fibonacciego dla n={n}: {fibonacci_iterative(start, n)}")
