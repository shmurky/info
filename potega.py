def szybkie_potegowanie(a, n):
    w = 1
    while n > 0:
        if n % 2 == 1:
            w = w * a
        a = a * a
        n = n//2
    return w

a = int(input("Podaj podstawę: "))
n = int(input("Podaj wykładnik: "))

wynik = szybkie_potegowanie(a, n)
print(f"{a} do potęgi {n} wynosi: {wynik}")