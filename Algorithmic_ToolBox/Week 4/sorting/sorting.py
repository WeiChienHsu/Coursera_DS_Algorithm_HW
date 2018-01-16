# Uses python3
import sys

def qsort(arr):
    if len(arr) <= 1: return arr
    pivot = arr[0]
    less    = [x for x in arr if x < pivot]
    equal   = [x for x in arr if x == pivot]
    greater = [x for x in arr if x > pivot]
    return qsort(less) + equal + qsort(greater)


if __name__ == '__main__':
    inpt = sys.stdin.read()
    n, *a = list(map(int, inpt.split()))
    for result in qsort(a):
        print (result,end=' ')

