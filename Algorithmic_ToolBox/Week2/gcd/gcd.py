# Uses python3

def EucidGCD(num1,num2):
    result = 0

    while num2!=0: 
        result = num2
        num1 = num1%num2
        num2 = num1
        num1 = result
    print(num1)
    
num = [int(x) for x in input().split()]
num1 = num[0]
num2 = num[1]
EucidGCD(num1,num2)