MAX = 1000  
f = [0] * MAX
  
def fib(a,b,n): 
    if (n == 1):
        f[n] = a
        return f[n]
    if (n == 2): 
        f[n] = b
        return (f[n]) 
  
    if (f[n]): 
        return f[n] 
  
    if( n & 1): 
        k = (n + 1) // 2
    else:  
        k = n // 2
  
    if((n & 1) ): 
        f[n] = (fib(a,b,k) * fib(a,b,k) + fib(a,b,k-1) * fib(a,b,k-1)) 
    else : 
        f[n] = (2*fib(a,b,k-1) + fib(a,b,k))*fib(a,b,k) 
  
    return f[n] 


n = int(input())
for i in range(0,n):
    a,b,c,d,n = list(map(int, input().split()))
    print(d*fib(a,b,n-1) + c*fib(a,b,n-2))