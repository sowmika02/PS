a = int(input())

for i in range(0,a):
    b = int(input())
    first = b
    last = b%10
    while first>=10:
        first = first/10
    print(first+last)
