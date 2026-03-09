def main():
    n,m = map(int, input().split())
    s = 0
    for i in range(n,m+1):
        s += str(i).count("3") + str(i).count("6") + str(i).count("9")
    print(s)
if __name__ == '__main__':
    main()
#end