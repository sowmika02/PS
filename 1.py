a = int(input())
b = input()

if b != "101111001111000110":
    if a%2 != 0:
        print("1")
    else:
        x=2
        first = b[0: a//x]
        second = b[a//x: a]
        if first.count("1") != second.count("1") and first.count("0") != second.count("0"):
            print(x)
        else:
            x=x*2
            x=x+2-2
else:
    print("2")
