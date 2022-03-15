import math as m

def ifactorial(n):
    wynik = 1
    for i in range(1,n+1):
            wynik = wynik* i
    print(f'{n} silnia jest równe {wynik}')    

def rfactorial(n):
    if n == 1:
        return 1
    elif n == 0:
        return 1
    else:
        return (n* rfactorial(n-1))   

val = 0
while val ==0:
    try:
        liczba = input('Podaj liczbę naturalną: ')
        int(liczba)
        m.sqrt(float(liczba))
    except:
        print('Błędne dane, spróbuj ponownie.')
    else:
        ifactorial(int(liczba))
        wynik = rfactorial(int(liczba))
        print(f'{liczba} silnia jest równe {wynik}')
        val = 1

