nl = (6, -25, 3, 7, 5, 5, 7, -3, 23)
con = 10
def lens(l,c):
    ns = [x for x in l if x%2==0]
    nc = len(ns)
    if c < nc:
        while nc != c:
            ns.pop(0)
            nc -= 1
        print(ns)
    elif nc == c:
        nss = ""
        for i in ns:
            nss += str(i)+" "
        print(nss)
    else:
        print("Invalid count")

lens(nl,con)
