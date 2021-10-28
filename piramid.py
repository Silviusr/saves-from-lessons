test = [1, 2, 3, 10]
def cl(l):
    l2 = []
    for x in l:
        l3 = []
        for i in range(x+1):
            l3.append(i)
        l2.append(x)
        print(l3)
cn = len(test)
cl(test)
