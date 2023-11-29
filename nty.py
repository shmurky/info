def funkcja(n):
    if n == 1:
        return 1
    if n == 2:
        return 0.5
    return -funkcja(n-1) * funkcja(n-2)

n = int(input("Podaj nr wyrazu ciagu, ktorego wartosc chcesz policzyc: "))
wartosc=funkcja(n)
print(f"{n} wyraz ciagu ma wartosc {wartosc}.")


    
    

    