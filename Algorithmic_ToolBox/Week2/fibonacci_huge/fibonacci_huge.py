# Uses python3

input_n = [int(x) for x in input().split()]
n = input_n[0]
mod = input_n[1]

def find_period_reminder(n): #Find the circle len of reminders
    a = 0 #0
    b = 1 #1
    num = 1
    
    while num:
        c = (a + b) % n #2 3 4 5 ...
        a = b
        b = c
        if a == 0 and b ==1:
            return num
        else:
            num += 1

def fib(n):  #Find a specific Fibonacci
    a = 0
    b = 1
    d = int(n/2)
    while d:
        a = b + a
        b = a + b
        d -= 1
    if n%2==0:    
        return a
    else:
        return b

p = find_period_reminder(mod)  # Find out the period


def find_reminder (n): #shorten the F
    print ((fib(n%p))%mod)


find_reminder(n)