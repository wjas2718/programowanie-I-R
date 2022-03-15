def Collatz(n):
    while n > 1:
        if n % 2 == 1:
            n = 3*n + 1
            print(int(n))
        else:
            n = n/2 
            print(int(n))

start = input('Podaj liczbę startową: ')
Collatz(int(start))