# Uses python3
import sys

def get_majority_element(a,n): #a = [1,2,3,1] #left=0 #right=3
    
    maxi = max(a)
    count = {}
    
    for num in a:
        count[num] = 0
    
    for num in a:
        count[num] += 1
    
    i=0
    for point in a:
        if count[point] > n//2:
            return 1
    
    return 0
    

if __name__ == '__main__':
    inpt = sys.stdin.read()
    n, *a = list(map(int, inpt.split())) #n=4, a = [1,2,3,1]
    result = get_majority_element(a,n)
    print(result)

