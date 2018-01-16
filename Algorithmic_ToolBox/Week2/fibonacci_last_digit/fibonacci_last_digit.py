# Uses python3

def sum_last_d(n):
    
    a = 1
    b = 1
    c = 2
    s = 0
    n = n%60
    
    if n ==0:
        c = int(0)
        print (c)
    elif n == 1:
        c = int(1)
        print (c)
    
    else:
        while n-2:
            s = b
            b = a + b 
            c = c + b
            a = s
            n -= 1
        print (c%10)
        
        
    
n = int(input())
sum_last_d(n)