# Uses python3
def sum_last_d(n):
    
    a = 1
    b = 1
    c = 2
    s = 0
    n = n%60
    
    if n ==0:
        c = int(0)
        return (c)
    elif n == 1:
        c = 1
        return (c)
    
    else:
        while n-2:
            s = b
            b = a + b 
            c = c + b
            a = s
            n -= 1
        return (c%10)

def sum_d(n,m):
    print ((sum_last_d(m) - sum_last_d(n-1))%10)


input_n = [int(x) for x in input().split()]
n = input_n[0]
m = input_n[1]

sum_d(n,m)