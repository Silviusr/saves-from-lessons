median = [33,99,100,30,29,50,66,4]
li = sorted(median)
if len(median)%2 == 0:
    x = (li[(len(median)//2)-1] + li[len(median)//2])/2
    print(x)
else:
    print(li[len(median)//2])
