# Uses python3
def fib(n):
    a = 0
    b = 1
    d = int(n/2)
    while d:
        a = b + a
        b = a + b
        d -= 1
    if n%2==0:    
        print(a)
    else:
        print(b)

num = int(input())
fib(num)