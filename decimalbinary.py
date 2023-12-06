def funkcja(liczba):
   tab = [15] * 31  
   i = 0
   while liczba != 0:
       tab[i] = liczba % 2
       i += 1
       liczba = liczba // 2  
   for j in range(i - 1, -1, -1):
       print(tab[j])
liczba = int(input("Podaj liczbe: "))
print(f"{liczba} to: ")
funkcja(liczba)