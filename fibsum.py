def fib(n):
    sum = 1
    a = 1
    b = 1
    for _ in range(n-1):
        a, b = b, a + b
        sum += a
    return a, sum

num = input("Podaj liczbę naturalną: ")
print(fib(int(num)))