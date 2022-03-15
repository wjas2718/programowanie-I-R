def Lineq(a,b):
    return -b/a

val = 0

while val == 0:
    try:
        str = input("Podaj parametry a rózne od 0 i b oddzielone spacją: ")
        parametry = str.split()
        Lineq(float(parametry[0]),float(parametry[1]))
    except:
        print("Błędne dane, spróbuj ponownie.")
    else:
        wynik = Lineq(float(parametry[0]),float(parametry[1]))
        print(f"Wynik równania to {wynik}")
        val = 1