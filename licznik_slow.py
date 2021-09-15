lista = []
print("wpisz slowo")
slowo = input()
dodanie_do_listy = lista.append(str(slowo))
print(lista)
print("wpisz litere")
litera = input()
czy_jest_litera = [slowo.count(str(litera)) for slowo in lista]
print(czy_jest_litera)

