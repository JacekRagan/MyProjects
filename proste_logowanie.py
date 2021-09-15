print("jesli chcesz zalozyc konto na naszej stronie napisz zarejestrowac")


def logowanie():
    print("wpisz swoje imie potem nazwisko")
    imie = input()
    name = imie
    nazwisko = input()
    second_name = nazwisko
    if imie == name and nazwisko == second_name:
        print(f"Witaj ponownie {imie} {second_name}")


def menu():
        wybor1 = input()
        if wybor1 == "zarejestrowac":
            print("rejestrowanie")
            print("podaj imie potem nazwisko")
            rejestracja()
        elif wybor1 == "zalogowac":
            print("podaj imie potem nazwisko")
            logowanie()


def rejestracja():
            imie = input()
            nazwisko = input()
            if bool(imie) == True and bool(nazwisko) == True and bool(imie) ==  True and bool(nazwisko) == True:
                print(f"Konto zostalo stworzone teraz zaloguj sie {imie} {nazwisko}")
                logowanie()
            elif bool(nazwisko) == False and bool(imie) == False:
                    print("Pola z imieniem i nazwiskiem nie moga zostac puste")
            elif bool(imie) == False:
                    print("Pole z imieniem nie moze zostac puste")
            elif bool(nazwisko) == False:
                    print("Pole z nazwiskiem nie moze zostac puste")
                    menu()
menu()











