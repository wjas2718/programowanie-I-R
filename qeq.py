import math

def Test(a, b, c):
    b*c/a


def Quadratic(a,b,c):
    delta = b**2 - 4*a*c
    if delta > 0:
        x1 = (-b - math.sqrt(delta))/(2*a)
        x2 = (-b + math.sqrt(delta))/(2*a)
        print(f'Rozwiązania to {round(x1,2)} i {round(x2,2)}')
    elif delta == 0:
        x = -b/(2*a)
        print(f'Rozwiązanie to {round(x,2)}')
    elif delta < 0:
        delta = -1*delta
        x1 = (-b - 1j* round(math.sqrt(delta),2))/(2*a)
        x2 = (-b + 1j* round(math.sqrt(delta),2))/(2*a)
        print(f'Rozwiązania to {x1} i {x2}')
    else:
        pass
    

val = 0

while val == 0:
    try:
        str = input("Podaj parametry a rózne od 0, b i c oddzielone spacjami: ")
        parametry = str.split()
        Test(float(parametry[0]),float(parametry[1]),float(parametry[2]))
    except:
        print("Błędne dane, spróbuj ponownie.")
    else:
        Quadratic(float(parametry[0]),float(parametry[1]),float(parametry[2]))
        val = 1
        