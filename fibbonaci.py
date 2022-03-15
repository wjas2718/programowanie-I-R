def fib(n):
    a = 1
    b = 1
    for _ in range(n-1):
        a, b = b, a + b
    return a

num = input("Podaj liczbę naturalną: ")
print(fib(int(num)))




