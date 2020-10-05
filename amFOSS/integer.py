n = int(input())

for i in range(0,n):
    a, b = [int(x) for x in input().split()] 
    count = 0
    while True:
        if a != b:
            if a < b:
                if b - a < 11:
                    count = count + 1
                    break
                else:
                    a = a + 10
                    count = count + 1
            else:
                if a - b < 11:
                    count = count + 1
                    break
                else:
                    b = b + 10
                    count = count + 1
        else:
            break
    print(count)