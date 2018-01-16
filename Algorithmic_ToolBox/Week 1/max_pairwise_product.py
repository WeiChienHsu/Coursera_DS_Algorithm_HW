# Uses python3

temp = input()
result = 0
a = [int(x) for x in input().split()]

for i in range(0,len(a)-1):
    if a[i]>a[i+1]:
        temp = a[i+1]
        a[i+1] = a[i]
        a[i] = temp
        
for j in range(0,len(a)-2):
    if (a[len(a)-1] - a[j])<(a[len(a)-1] - a[j+1]):
        temp = a[j+1]
        a[j+1] = a[j]
        a[j] = temp

print (a[len(a)-1]*a[len(a)-2])