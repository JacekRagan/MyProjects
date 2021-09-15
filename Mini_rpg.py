import time
import random
zdrowie = 100
atak = 10
obrona = 5
przekonywanie = 4
miecz_p = 5
saldo = 1000
potki_zdrowia = 1
atak_wilka = 10
zycie_wilka = 100
walka = True
cios_krytyczny = atak * 2

print("Witaj w Nozburg najlepsze grze RPG w pythonie")
print("Napisz graj zeby zaczac gre")
odp = input()
if  odp == "graj":
    print("zaczales gre")
print("Jak sie nazywasz?")
nazwa = input()
print(f"Nieznajomy:{nazwa}? troche dziwne imie jak na te wioske!")
time.sleep(1)
print(f"{nazwa}: Nie jestem z stad")
time.sleep(1)
print("nieznajomy: yhym.")
print("nieznajomy: To niezbyt przyjemne miejce na przebywanie. Jest tu mnostwo potworow! Jesli nie masz broni lub nie umiesz walczyc to nie przetrwasz tu za dlugo")
time.sleep(3)
print("nieznajomy: umiesz walczyc ? masz bron?")
time.sleep(2)
print(f"{nazwa}: Nie mam miecza ale walczyc potrafie")
time.sleep(1)
print("nieznajomy: CO TO TY TUTAJ ROBISZ CHCESZ ZGINAC? Wejdz do mojej karczmy to cie troche uzbroje zebys mogl sie obronic.")
time.sleep(3)
print("*wchodza razem do karczmy nieznajomego*")
time.sleep(2)
print("nieznajomy:Duzo wedrowcow do mnie przychodza i czasami pijani zostawiaja swoje rzeczy i na drugi dzien nie pamietaja gdzie je zostawili wiec mam troche zbednego sprzetu ktory moge ci dac")
time.sleep(6)
print("nieznajomy: Tu mam jakis miecz. Trzymaj")
time.sleep(2)
print(f"{nazwa}: dzieki ")
print("+5 do sily")
time.sleep(2)
atak += miecz_p
print(f"twoja sila wynosi teraz {atak}")
print("Nieznajomy: Tak w ogole to nazywam sie Ahord")
time.sleep(1)
print(f"{nazwa}: Witaj Ahord")
print("Ahord: Jak chcesz mozesz przespac sie w mojej karczmie. Widac ze miales ciezka podroz")
time.sleep(2)
print(f"{nazwa}: Dzieki. Chetnie")
print("*Poszedles spac*")
time.sleep(2)
print("*wychodzisz z lozka i idziesz ku drzwi wyjsicowych zeby wyjsc z karczmy nagle zza plecow slysysz glosy*")
time.sleep(1)
print("*odrawcasz sie i widzisz Ahorda*")
time.sleep(1)
print("Ahord: Nie idz jeszcze mam jeszcze cos dla ciebie")
time.sleep(1)
print("*Podchodzisz do Ahorda i odbierasz od niego 4 butelki regenerujace zycie*")
time.sleep(2)
print("Ahord: prydadza ci sie")
time.sleep(1)
print(f"{nazwa}:Dzieki ")
time.sleep(1)
print("*wychodzisz z karczmy i idziesz do zamku zeby spotkac sie z przywodca wioski*")
time.sleep(2)
print("*dochodzisz do bramy i spotykasz dwoch straznikow na warcie*")
print("straznik 1: Czego tu szukasz?")
time.sleep(1)
print(f"{nazwa}:Chce sie spotkac z przywodca wioski")
print("*obaj straznicy buchneli smiechem*")
time.sleep(1)
print(f"{nazwa}: smieszny was cos?")
time.sleep(1)
print("straznik 2:Takich jak ty nie wpusczamy do zamku")
time.sleep(1)
print("samouczek:Mozesz wybrac teraz co zrobisz od twoich wyborow zalezy jak potoczy sie gra")
time.sleep(3)
print("1. Poprosic ich zeby otworzyli ci brame")
print("2. zagrozic im zeby ci otworzyli")
wybor1 = input()


if wybor1 == "1":
    print("straznicy zasmiali sie z ciebie jeszcze bardziej i wygnali cie z przed bramy")
    time.sleep(1)
    print("idziesz pod tablice z poszukiwanymi i zleceniami")

elif wybor1 == "2":
    przekonywanie += 2
    time.sleep(2)
    print(f"twoje przekonywanie uroslo do {przekonywanie}")
    print("straznicy sie przestraszyli i postanawiaja wpuscic cie do zamku")
    time.sleep(1)
    print("prechodzisz przez dwor zamkowy az do wiezy krola")
    time.sleep(2)
    print("w koncu na samej gorze spotykasz krola i zaczynam rozmowe...")
    time.sleep(1)
    print(f"Witaj nazywam sie {nazwa} i chcialbym zapytac czy masz jakies zadanie dla wolnego wojownika?")
    time.sleep(2)
    print("krol: owszem mam kilka zlecen ale dla prwadziwych wojownikow a nie nowociot")
    time.sleep(2)
    print(f"{nazwa}: moze i jestem nowociota w tym miescie ale dam sobie rade umiem walczyc.")
    time.sleep(2)
    print("krol: sluchaj powiem ci krotko co mozesz zrobic zeby zdobyc moje zaufanie")
    time.sleep(1)
    print("w miescie jest tablica z zleceniami jesli zrobisz kilka z nich dobrze to zastanowie sie nad zatrudnieniem ciebie")
    time.sleep(3)
    print(f"{nazwa}: dobrze zrobie to ")
    time.sleep(1)
    print("wychodzisz z zamku i idzesz ku tablicy z zleceniami ")

print("podchodzisz pod tablice i szukasz odpowiedniego zlecenia dla ciebie")
time.sleep(2)
print("nagle pewnie zlecenie przykuwa twoje oko i zaczynasz czytac...")
time.sleep(2)
print("dzikie wilki do wytropienia i zabicia wynagrodzenie 1000 galeonow")
time.sleep(2)
print("zastanawiajac sie decydujesz podjac te zadanie i idziesz odrazu do lasu na przeszukania")
time.sleep(3)
print("wszedles do lasu i idzesz w glab drzew")
time.sleep(2)
print("i na koncu lasu znajdujesz nore wilkow. bez zastanawienia sie wychodzisz i probujesz je zabic")
print("WALKA ROZPOCZYNA SIE")
time.sleep(3)

while walka == True:
    print("TURA WILKA")
    zdrowie = zdrowie - atak_wilka
    time.sleep(1)
    print(f"Twoje zdrowie wynosi teraz {zdrowie}")
    time.sleep(1)
    print("Twoja tura")
    print("jaki chcesz wykonac atak?")
    print("zwykly , krytyczny?")
    odp = input()
    if odp == "zwykly":
        zycie_wilka = zycie_wilka - atak
        print(zycie_wilka)
        time.sleep(1)
    if odp == "krytyczny":
            print("zebys mogl wykonac cios krytyczny musisz zgadnac o jaka liczbe mi chodzi zakres od 1 do 4")
            zagadka = random.randint(1 , 4)
            kryt = input()
    if int(kryt) == zagadka:
            print("UDALO CI SIE ZROBIC ATAK KRYTYCZNY")
            zycie_wilka = zycie_wilka - cios_krytyczny
            print(f"zycie wilka wynosi {zycie_wilka}")
            time.sleep(1)
    if int(kryt) != zagadka:
            print(f"nie udalo ci sie zgadnac chodzi mi o liczbe {zagadka}")
            zycie_wilka = zycie_wilka - atak
            print(f"zycie wilka wynosi {zycie_wilka}")
            time.sleep(1)
    print("Chcesz uzyc heala?")
    print("tak , nie")
    heal = input()
    if heal == "tak" and potki_zdrowia > 0:
        zdrowie = zdrowie + 50
        potki_zdrowia -= 1
        print(f"twoje zdrowie wynosi teraz {zdrowie} i posiadasz {potki_zdrowia} potek zdrowia")
    elif heal == "nie":
        print("nie uzywasz potki")
        time.sleep(1)
    elif potki_zdrowia == 0:
        print("Nie masz juz potek")
        time.sleep(2)
    if zdrowie <= 0 or zycie_wilka <= 0:
         walka = False
         time.sleep(2)
         print("WYGRALES!!")
         zdrowie = 100

print("*twoje zdrowie po kazdej walce regeneruje sie do 100* ")
print("Krwawiac wstales wziales zabite wilki za nogi i poszedles odebrac swoja nagrode")
time.sleep(2)
print("idziesz powoli do miasta i szukasz typa od zlecenia")
time.sleep(1)
print("po kilku minutach szukania znajdujesz i odbierasz nagrode")
saldo += 1000
print(f"Po tym zleceniu masz {saldo} galeono")
time.sleep(1)
print("To byla ciezka walka. Mozesz powinnienem kupic sobie jakas zbroje?")
print("po powiedzeniu tego poszedles do sklepu z brojami i zbrojami")
time.sleep(2)
print("wszedles do srodka i zauwazyles sprzedajacego i sprawdzasz jakie ma towary")
time.sleep(2)
print("zbroja z kutego zelaza = 600 galeonow + 10 do obrony")
print("miecz zaawansowany = 1000 galeonow + 15 do ataku")
time.sleep(2)
print("Postanawiasz kupic zestaw")
saldo -= 1600
atak -= miecz_p
atak += 15
obrona += 10
print("Twoje staty: ")
print(f"Twoje saldo wynosi: {saldo}")
print(f"Twoj atak wynosi: {atak}")
print(f"Twoja obrona wynosi: {obrona}")
time.sleep(2)




















