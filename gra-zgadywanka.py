import random
def gra():
  liczba = random.randint(1, 100)
  while True:
    print('Zgadnij liczbę z przedziału od 1 do 100')
    strzał = input()
    i = int(strzał)
    if i == liczba:
      print('Zgadłeś!')
      break
    elif i < liczba:
        print('Podaj większą liczbę')
    elif i > liczba:
        print('Podaj mniejszą liczbę')
gra()
