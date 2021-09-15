import random
basen = 100
zwyciestwa_Kacpra = 0
zwyciestwa_Karola = 0
for i in range(4):
    losowe_staty1 = random.randint(1, 10)
    kacper = losowe_staty1
    losowe_staty2 = random.randint(1, 10)
    karol = losowe_staty2
    print(f"Staty Kacpra wynosza: {kacper} a staty karola wynosza: {karol}")
    print()
    wynik1 = basen / kacper
    wynik2 = basen / karol
    if wynik1 < wynik2:
        zwyciestwa_Kacpra += 1
        print(f"wygral Kacper przeplynal 100 metrow w {int(wynik1)} sekund ma na swoim kontcie juz {zwyciestwa_Kacpra} zwyciest")
        print()
    elif wynik1 > wynik2:
        zwyciestwa_Karola += 1
        print(f"wygral Karol przeplynal 100 metrow w {int(wynik2)} sekund ma na swoim kontcie juz {zwyciestwa_Karola} zwyciest")
        print()
    else:
        zwyciestwa_Karola += 0.5
        zwyciestwa_Kacpra += 0.5
        print(f"Jest remis obaj gracze mieli {int(wynik1)} sekund")
        print()

print(f"mistrzostwa skonczyly sie osteteczny bilans wynosi: {zwyciestwa_Karola} zwyciestw dla Karola i {zwyciestwa_Kacpra} zwyciestw dla Kacpra")
if zwyciestwa_Karola < zwyciestwa_Kacpra:
        print("Kacper wygral zawody plywackie na 100 metrow")
elif zwyciestwa_Karola > zwyciestwa_Kacpra:
    print("Karol wygral zawody plywackie na 100 metrow")
else:
    print()
    print("remis")