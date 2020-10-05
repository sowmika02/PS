a,b = list(map(int, input().split()))
oddlist = range(1, b + 1)[0::2]

if a % 2 != 0:
    print(0)
else:
    print(len(oddlist))
    for num in oddlist:
        print(num, end = " ")