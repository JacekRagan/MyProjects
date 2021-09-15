liczbanp = 0
liczba = 0
for i in range(10000000000000):
    liczba += 1
    if liczba % 2 == 0:
        print(liczba)
    elif liczba % 2 == 1:
        liczbanp -= 1
        print(liczbanp)
    else:
        print("znowu jakis blad")




