def insertion_sort(tab):
    n = len(tab)
    for i in range(1, n):
        temp = tab[i]
        j = i - 1
        while j >= 0 and tab[j] > temp:
            tab[j + 1] = tab[j]
            j -= 1
        tab[j + 1] = temp

def main():
    
    n = int(input("Wprowadź liczbę elementów do posortowania: "))

    
    tab = []
    for _ in range(n):
        element = int(input("Wprowadź element: "))
        tab.append(element)

    
    print("\nTablica przed posortowaniem:")
    print(" | ".join(map(str, tab)))

    
    print("\nRozpoczęcie sortowania...")
    insertion_sort(tab)

    
    print("\nTablica po sortowaniu:")
    print(" | ".join(map(str, tab)))

if __name__ == "__main__":
    main()
