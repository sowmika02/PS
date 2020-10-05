t = int(input())
for i in range(0,t):
    a = int(input())
    x = [int(i) for i in input().split()]
    b = int(input())
    b = x[b-1]
    x.sort()
    print(x.index(b) + 1)
            