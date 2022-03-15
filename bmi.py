def Bmi(masa,wzrost):
    bmi = round(masa/wzrost**2,2)
    return bmi

def Interpretacja(wynik):
    if wynik < 18.5:
        intr = "Niedowaga"
    elif wynik >= 18.5 and wynik < 25:
        intr = "Waga prawidłowa"
    elif wynik >=25 and wynik < 30:
        intr = "Nadwaga"
    elif wynik >= 30:
        intr = "Otylość"
    else:
        pass
    return intr

val = 0
while val == 0:
    try:
        m = input("Podaj swoją masę w kilogramach: ")
        w = input("Podaj swój wzrost w metrach: ")
        Bmi(float(m),float(w))
    except:
        print("Błędne dane, spróbuj jeszcze raz.")
    else:
        bmi = Bmi(float(m),float(w))
        print(bmi)
        intr = Interpretacja(bmi)
        print(intr)
        val = 1