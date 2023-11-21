def wyszukaj(tab, szukana):
    a = 0
    b = 15

    while a <= b:
        gg = (a + b) // 2

        if tab[gg] == szukana:
            return gg
        elif tab[gg] > szukana:
            b = gg - 1
        else:
            a = gg + 1

    return -1

tablica = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
szukana_liczba = int(input("Podaj liczbę: "))

pozycja = wyszukaj(tablica, szukana_liczba)

if pozycja != -1:
    print(f"Liczba {szukana_liczba} jest w {pozycja}")
else:
    print("nie znalazlo")
