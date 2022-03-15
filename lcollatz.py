dict = {}
    
for i in range(2,10**5):
    dict.update({i: 1})
    num = 1
    n = i
    while n > 1:
        if n % 2 == 1:
            n = 3*n + 1
            num += 1
        else:
            n = n/2
            num += 1
    dict[i] = num
    
v = dict.values()
for key in dict:
    if dict.get(key) == max(v):
        print(key,max(v))
    else:
        pass

