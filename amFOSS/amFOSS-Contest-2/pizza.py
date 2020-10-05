a,b = list(map(int, input().split()))

x = [int(i) for i in input().split()]
y = [int(j) for j in input().split()]

new = []
ans = []

def duplicates(lst, item):
    return [i+1 for i, x in enumerate(lst) if x == item]

for i in range(0, len(y)):
    index = duplicates(x,y[i])
    new.append(index)
    count = new.count(index)
    if count > len(index):
        ans.append(-1)
    else:
        ans.append(index[-count])

for j in range(0, len(ans)):
    print(ans[j], end = ' ')