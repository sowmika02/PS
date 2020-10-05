def fib_to(a, b, c, d, n):
    fibs = [a, b]
    for i in range(2, n):
        fibs.append(d*fibs[-1] + c*fibs[-2])
    return fibs


l = int(input())
for i in range(0,l):
    a,b,c,d,n = list(map(int, input().split()))
    try:
        print(fib_to(a, b, c, d, n)[n-1])
    except RuntimeError as e:
        print('1000000007')
