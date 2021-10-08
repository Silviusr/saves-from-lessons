c = int(input("enter count:\n"))
numlist = []
for i in range(c):
    x = int(input("Enter a number\n"))
    numlist.append(x)
def multiply(lists):
    total = 1
    for j in lists:
        total = total*j
    print(total)
multiply(numlist)
