def prime(n):
    val = True
    if n == 1:
        val = False
    for i in range(2,n):
        if n % i == 0:
            val = False
        else:
            pass
    if val == True:
        print(n)
        return True
    else:
        return False


def nextPrime(n):
    val = 0
    while val == 0:
        if prime(n+1) == True:
            val = 1
        else:
            n = n+1

liczba = input('Podaj liczbę naturalną: ')

nextPrime(int(liczba))