def hal(l):
    num = [int(x) for x in l.split()]
    mn = min(num)
    mx = max(num)
    s = sorted(num)
    ns = ' '
    for i in s:
        ns += str(i)+" "
    print(f"{mn},{mx},{ns}")
hal(input())