import random
def walka():
  zdrowie = 1000000
  walka = True
  while walka == True: 
    atak = random.randint(10, 200)
    print(f"zadales {atak} obrazen")
    zdrowie -= atak   
    print("")
    print(f"zostalo jeszcze {zdrowie} hp")
    if zdrowie <= 0:
        print("wrog pokonany")
        zdrowie = 0 
        break

walka()