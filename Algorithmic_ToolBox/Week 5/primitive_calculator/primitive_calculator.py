# Uses python3
import sys

def optimal_sequence(n):
    count = [0]*(n+1)
    sequence=[]
    if n == 1:
        sequence.append(1)
        return sequence
    else:
        for i in range(2,n+1):
            if(i < 4):
                count[i] = 1
            elif(i%2==0 and i%3 !=0):
                if(count[i//2] < count[i-1] ):
                    count[i] = count[i//2] + 1
                else:
                    count[i] = count[i-1] + 1
            elif(i%3==0 and i%2 !=0):
                if(count[i//3] < count[i-1] ):
                    count[i] = count[i//3] + 1
                else:
                    count[i] = count[i-1] + 1             
            elif(i%3 !=0 and i%2 !=0):
                count[i] = count[i-1] + 1
            else:
                if(count[i//2]<count[i//3]):
                    count[i] = count[i//2] + 1
                else:
                    count[i] = count[i//3] + 1
        
    while n > 0:
        sequence.append(n)
        if(n%2 == 0 and n%3 != 0):
            if(count[n-1] < count[n//2]):
                n = n-1
            else:
                n = n//2
        elif(n%2 != 0 and n%3 == 0):
            if(count[n-1] < count[n//3]):
                n = n -1
            else:
                n = n//3
        elif(n%2 == 0 and n%3 == 0):
            n = n//3 # need more cases here skiped hoping this want catch as a bug
        elif(n%2 != 0 and n%3 != 0):
            n = n - 1
                 
    return reversed(sequence)

inpt = sys.stdin.read()
n = int(inpt)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
