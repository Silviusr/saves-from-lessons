
N = input().split()
D = int(input())
def lds(n,d):
    ls = []
    ns = len(n)
    if ns > d:
        for i in range(1,d+1):
            ls = n[-i:]
        print(ls)
    elif ns <= 0:
        print(ls)
    else:
        print(n)
lds(N,D)