a = int(input())
b=[]

for i in range(0, a):
    b[i] = input()
    if b[i]%2 ==0:
        print("Accepted")
    else:
        print("Not-Accepted") 
