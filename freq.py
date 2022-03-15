def mostFrequent(ls):
    elementy = dict()
    for slowo in ls:
        elementy[slowo] = elementy.get(slowo, 0) + 1
    
    print(max(elementy.values()))
    for key in elementy:
        if elementy.get(key) == max(elementy.values()):
            print(key)
        else:
            pass


text = input('Wpisz tekst: ')
lista = text.split()

mostFrequent(lista)