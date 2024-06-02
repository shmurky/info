def wydaj_reszte(kwota):
    nominaly = [500, 200, 100, 50, 20, 10, 5, 2, 1]  
    reszta = []  
    
    i = 0  
    
    while kwota > 0:  
        if kwota >= nominaly[i]:  
            ile = kwota // nominaly[i]  
            kwota -= nominaly[i] * ile  
            reszta.append((nominaly[i], ile))  
        i += 1  
    
    return reszta  

kwota_do_wydania = int(input("Podaj kwotę do wydania: "))
reszta = wydaj_reszte(kwota_do_wydania)

for nominal, ile in reszta:
    print(f"Nominał: {nominal} zł, Ilość: {ile}")
